## Day 5

When I saw the task, I immediately thought:

"This is a task for APL!"

Now, the problem is, I don't know APL, so I have spent far more time than I would like to admit
on solving todays task, but I must say: it was a lot of fun:)

I have no idea if my solution is even vaguely idiomatic, but it solves the problem,
and is quite succinct, so I am happy.

If you would like to run it, or try out APL yourself(which I recommend), then I used
[dyalog](https://www.dyalog.com/)
and added
```
alias dyalog="/Applications/Dyalog-18.0.app/Contents/Resources/Dyalog/dyalog"
```
to my rc-file(this is probably not the correct way to do it, but it works), and
then I ran my file with
```
dyalog -script day05.dyalog
```
I did development in the Dyalog REPL thingy.

Also, I would really recommend [aplcart](https://aplcart.info/), it is the best resource
I have found.

### The code explained
APL is absolutely unreadable the first time you see it(and I think it remains partly
unreadable for a while). I case anybody are interested(or if I return here in the future),
I thought I might explain the code while it is still fresh.

On a high level, my code does the following:
- Open a file and bind it to `tn`
- Generate the values 0, 11, 22, 33 .. 11*844. This is due to each line being 11 chars(10 + "\n") long, and there being 845 lines
- For each of those values(offsets):
- - Read the first 7 chars and compare it to `'BBBBBBB'` -> this will result in a 7 digit binary number(row)
- - Convert this to decimal and multiply it with 8
- - Read the next 3 chars and compare them to `'RRR'` -> this will result in a 3 digit binary number(column)
- - Convert this to decimal and add the two numbers together.
- Take the ceiling(max) of all of these values and output it.

For task 2:
- Generate the values between the floor and ceiling of the previous values
- - This works because you know the seat 1 more and 1 less than your's exist(but not the global tops and bottoms)
- Print the values that are unique for either set(this should have been intersection)

```
tn ← 'input.txt'⎕NTIE 0
```
Here 'input'.txt is tied(NTIE) with the number 0 and the result is bound to `tn`. I think.
Think of file descriptors in languages like C.

```
task1←{((2⊥'BBBBBBB'=(⎕NREAD tn 80 7 ⍵)) × 8) + (2⊥'RRR'=(⎕NREAD tn 80 3 (7 + ⍵)))}
```
Here there is quite a lot happening.
```
⎕NREAD tn 80 7 ⍵)
```
Read 7(units of type) of type 80(8 bits character - see [here](http://help.dyalog.com/13.0/index.html?page=html%2Fnative%20file%20read.htm))
starting from offset specified by ⍵. ⍵ is the "Right argument of a defn", which will be the parameter we call
our function abstraction with(0, 11, 22 ...).
```
(2⊥'BBBBBBB'=(⎕NREAD tn 80 7 ⍵))
```
Compare the 7 characters just read to `'BBBBBBB'`. In other languages, you would probably expect to get something
like True/False, #t/#f, 0/1 etc, but in APL, as things are matrixes, we do a matrix comparison and get either
0 or 1 for each index - `'BBBBBBB'='FBFBFBF'` would become `0 1 0 1 0 1 0`. The result of this comparison is then
decoded(`⊥`) from base 2 to base 10 (`2⊥`)
```
((2⊥'BBBBBBB'=(⎕NREAD tn 80 7 ⍵)) × 8)
```
Here we just multiply the result(the base 10 number) with 8. Note that we use `×`(times) and not i.e
`*` which one might be used to from other languages.
```
+ (2⊥'RRR'=(⎕NREAD tn 80 3 (7 + ⍵)))}
```
The right part is the same, just for the next three characters. Note that we here read from offset (7 + ⍵). Then
this number is added to the previous number

```
task1←{((2⊥'BBBBBBB'=(⎕NREAD tn 80 7 ⍵)) × 8) + (2⊥'RRR'=(⎕NREAD tn 80 3 (7 + ⍵)))}
```
We specify that this is a function abstraction with `{}` and bind it to task1.

```
⌈/values←(task1)¨(0,11×⍳844) ⍝ "map the task1 function over 0,11,22..11*844"
```
`¨` is map/for-each and `⌈` is the ceiling function. In
```
(0,11×⍳844)
```
We concatenate 0 (comma is concatenate) with 11 * (the range 1..844) (iota is the index generator)

Note that we in this line bort assign to value and print out the ceiling.

```
values(∪~∩)(⌊/values-1)↓⍳(⌈/values) ⍝ "find uniques of values and floor values..ceil values"
```
This line should be manageable when you realize `⌈` is ceiling and `⌊` is floor. iota is again
the index generator. Also `↓` is the "drop"-function. We generate the values up to ceiling of values,
then drop the values that are less than the floor of the values. Then we get the uniques(∪~∩)(union negation
intersection) of this generated matrix and our list of values from before.


Thats pretty much it. Pretty neat tbh.
