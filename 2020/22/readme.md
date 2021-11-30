## Day 22

Quite liked today's problem.

Definitely on the easier side, but still had to learn some new Rust stuff - both Deques and hashing was
new to me. I must say I really like `match`-statements, it is probably one of the features I'll miss in
languages that don't have them. Only thing I would have liked them to have is something along the lines of:

```Rust
match played{
    (Some(X),Some(y)) => "DoStuff",
    (Some(x),Some(Y)) => "DoOtherStuff",

}
```
instead of

```Rust
match played{
    (Some(x),Some(y)) if x > y => "DoStuff",
    (Some(x),Some(y)) if x < y => "DoOtherStuff",
}
```


To run:

```
cargo aoc -d 22
```

