## Day 14


### Preprocessing

One of the nice things about AoC is that if you do not like the way the input is formatted, you can just change it. As such, I did the following in Vim.

```
:%s/\[/ /g
:%s/\] =//g
```

### The solution

Part 1 went quite fast, but I struggled a bit with figuring a nice solution for part2. I feel like sending a mutable reference to the HashMap is a decent enough
solution, but that my code is somewhat un-idiomatic and that I would be able to find a slightly better solution if I knew Rust better. Also, code could be made
generic, but really no point. Quite happy with how much part1-code I could use in part2.


To run:
```
cargo aoc -d 14
```
(after doing the preprocessing)
