## Day 1

### 1-1
```
kotlinc day01.kt && cat input1.txt | Kotlin Day01Kt
```

The naive solution here is O(n^2) - just double for-loop.

There are a few "good" solutions(the task is naively O(n^2) and input
is 200 numbers between 0 and 2020 - all solutions are good lol)

Anyways some of the better ones:
- While reading, hash and store 2020 - input. If you read a number that is
stored, output that number and 2020 - number(and break).
- The set solution where you build up a total set and a difference set and
output the intersection between these. Sets are usually either based on
hashing or binary trees(afaik) so this is quite efficent. This is the
one I opted for.
- Sort(radix) the input and run a pointer from each end towards the middle
and compare. If sum less than 2020, move left pointer to the right, if sum
larger than 2020, move right pointer to the left. I believe this is the
best solution if input is sorted. I also like this one because it doesn't
require auxillary data structures(no extra space needed) which also makes
it viable in pretty much all programming languages(= easy to write in C)

### 2-2
```
kotlinc day01_2.kt && cat input1.txt | Kotlin Day01_2Kt
```

Here naive jumps to O(n^3) and the best I can do is O(n^2). The set solution
is pretty easy to scale up. The hashing solution is very similar, so it
should be simple as well. The pointer solution becomes a little more tricky,
but I believe it will be even faster on average case. Again, you run two
pointers inwards, but also run a third pointer "to make up" the difference.
Also, the left pointer(small pointer) gets moved left every time you move
right pointer. Then again, I haven't implemented it, so I dunno.
