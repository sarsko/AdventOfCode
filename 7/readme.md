## Day 7

Not the greatest(but not terrible by any means) solution today. Realized I haven't
really solved a graph problem in over a year(other than linked list stuff).

The solution to part one was okay, but things got ugly when I introduced pairs and
stuff in part two.

Couldn't be bothered to do all the parsing in Kotlin so i did the following in Vim
to input.txt:

```
:%s/bags/bag/g
:%s/\.//g
:%s/ contains/,/g
```

Some proper problem solving right there.

Anyways, the solution to the first part is done by iterating a fixpoint for the
transitive closure of the graph. This could be done more efficiently by having a worklist
instead of iterating over all the nodes, but it only runs like 5 iterations anyways.

Also, having this work with the new representation of the graph was really unnecessary,
the first solution which just requires
```
:%s/[0-9] //g
```
in Vim is better.

So yeah, need to do more graph stuff, but a solution is a solution.

To run:
```
kotlinc day07.kt && Kotlin Day07Kt
```
and:
```
kotlinc day07_02.kt && Kotlin Day07_02Kt
```
