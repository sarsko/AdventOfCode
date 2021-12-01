## Day 1

### Python

Did it quick and dirty with Python so that I could spend as much time as I
wanted in Haskell(not that it mattered as I started late). I really like the
god-awful `try-except`-block in part 2.

### Haskell

#### Part 1

It isn't too bad, but it isn't great either. I don't like the overcounting and
`(-1 +)` in the end.

#### Part 2

There does probably exist nicer solutions, but I am overall not too dissatisfied
with this one. Would have liked it to be able to work with any size window, I
guess I have to learn how to do that. I like the reuse of `solveA`.

#### Edit

After looking at [Sondres
solution](https://github.com/sondresl/AdventOfCode/blob/master/2021/Haskell/src/Day01.hs),
I realized that I could use `tail` to remove the need to do `(-1 +)` in the end,
and similarily not have to `drop` for part 2. A small improvement, but an
improvement nonetheless.
