## Day 11

Ah, good to be back. Had an exam(it went fine, thanks for asking) and had to correct some exams + visited dad in Sulis so I have more than a week of AoC to catch up on. Nice.

Friendship ended with Kotlin, now Rust is my new best friend.

The plan is to write a compiler in Rust with [Dan Banana](https://github.com/danbanan) next semester, so I might as well learn it through AoC.
It will also be useful for my thesis.

Most importantly: it is fun to learn new stuff - especially programming languages.

My APL endeavors has been temporarily halted, as I am behind on AoC, and learing Rust is more important.
Perhaps I will revisit APL if I have time.


### The solution

To be honest, I am not too dissatisfied with my solution, being my first Rust program and all.
I also did not struggle _too_ much.

I used the [AoC template](https://github.com/gobanos/aoc-runner) by Gobanos. I'm still undecided whether that was a correct decision or not.
Probably correct in the long run, but there are aspects with files(among other things) I will have to learn later.

The template follow a different ordering scheme than I have followed this far - all my Rust code resides in the `src` folder, and each day
is symlinked into its respective folder(folder `11` for today), where the `readme.md` also resides. Hopefully it works OK.

### Actually the solution

The "problem" with reading compiler stuff is that you end up solving things in complier ways. My solution is a sort of recursive decent solution, where I
iterate through the seating arrangement, and let each position solve itself by letting all the neighbours solve themselves(and adding together).
This solution scaled very easily for part two, as I only had to change `4` to `5` and do minor changes to the solvers(`count` and `value` - yes, I know,
aptly named).

Also, yes, I know, I could make the solvers(and the recurisve solver-parts) generic, but there is really _no point_

To run:
```
cargo aoc -d 11
```

### Possible improvements

I think there is room for improvement in the flow of `solve_part1/2`, possibly not using for-loops, and not doing `.clone()`, or, in other words, doing a
"functional", "all at once", transformation of the seating arrangement. I do not know how to do that. Please tell me if you know.

Also, using vectors is not really necessarry, using arrays should be faster, but I haven't really used vectors before(thing to learn) and the parsing example
I based my solution on used vectors and I couldn't be bothered to change.

In my solution, I use that `.get()` wraps the result in an `Option`, and then check bounds with pattern matching. It is an all right solution(the code becomes
readable), but I don't really like going out of bounds when I can prevent it. It could be checked or the soltion could be padded. I actually like padding a fair
bit, as you can do `[i][j]`-indexing safely(and add the results - a solution which lends itself very well to a functional approach).

There is probably something else I could do better. I am trying to learn Rust, so feel free to tell me.
