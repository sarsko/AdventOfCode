## Day 08

Really a problem that lends itself to being solved in an imperative language, at least if
done naively. The solution described by [lasagnaman](https://www.reddit.com/r/adventofcode/comments/k8zdx3/day_8_part_2_without_bruteforce/gf19rwx/)
is much nicer, and there is a theoretical possibility that I will try implementing it later.

Also, [voidhawk42](https://www.reddit.com/r/adventofcode/comments/k8zdx3/day_8_part_2_without_bruteforce/gf1cmm0?utm_source=share&utm_medium=web2x&context=3)
chimes in with a nice APL solution which I definitely will take a look at when I have time
to look at some more APL stuff.

I think an overall quite pretty solution could be done in a lisp, as the flow is to just read
`car`, then evaluate the symbol(`+`/`-`), accumulate the value, and then recurse. For `nops` you
just recurse directly, and for `jmps` you `cdr` some amount of times, either from the top(for negatives)
or from current position(for positives).

To run:
```
kotlinc day08.kt && Kotlin Day08Kt
```

