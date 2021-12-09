## Day 18

### Part 1

There is no point in reinventing the wheel - this one is solved by default evaluation in Smalltalk(and [Rebol](http://www.rebol.com/r3/docs/guide/code-functions.html)

I used [this](https://www.tutorialspoint.com/execute_smalltalk_online.php) online interpreter for GNU Smalltalk.

### Part 2

Not done yet.

I thought that going from a working Smalltalk solution for part 1 to a working Smalltalk solution for part 2 could not be too hard - turns out it is.

My thought was that I could wrap * in a function(or whatever it is called in Smalltalk) and replacing * with that funcition in the input, the Smalltalk
interpreter would do the rest for me. I think there is something in [this](https://stackoverflow.com/questions/31897553/chaining-keyword-messages) that I
do not understand. I could not get it to work.

Also, programming in Smalltalk has been thoroughly unenjoyable. Like yeah, I get it, smart people designing the purest object-oriented programming language
there is, but the error messages are completely useless, the vocabulary is occult and finding an answer to your question is damn near impossible.

0/10 would not reccommend.

### Part 2 second time

I am really happy with this solution. It is short, easy to understand, and easy
to implement. No need to do a bunch of parsing or adding parantheses. I first
swap `+` with `*` and vice versa, then wrap all the numbers in a `Num` class,
before using `eval` to do all the lifting for me. Did `:%s/(/( /g` and `:%s/)/) /g` in
in Vim on the input file beforehand, but this could have been done in Python as
well.
