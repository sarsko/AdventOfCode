## Day 23

Playing games with the crab has been fun, I must say.

Very happy with not picking a "hatløsning" for part 1, as I (correctly) assumed that
we would scale up the numbers for part two(as was the case for day 15, which also had
non-standard input).

Turns out Rust [lacks](https://internals.rust-lang.org/t/whats-the-status-of-std-linkedlist-maybe-deprecate-in-rust-2018/8068)
proper [linkedlists](https://rust-unofficial.github.io/too-many-lists/),
or at least an implementation which would suffice for my needs.

Since making a one-to-one mapping from the input to a vector is trivial(+ size is known),
implementing a linked list using vectors where the value is the next node is quite
straightforward. Running time ended up being around 300 ms, there are probs some
low-hanging optimizations I could do to gain more speed.

I also tested with a somewhat more general-purpose linked list implementation using
HashMaps, as Lars said on Monday that the only datastructure you need is maps(perhaps
with a thoroughly optimizing compiler, yes). It ended up running in 4.9s with hashbrown
and 6.4s with std, which is not *terrible* but still not great. It works for any
hashable value, so it will be fine for most uses.

With how easy implementing linkedlists is in C, I feel that either I must be missing
something, or Rust is seriously lacking a proper linkedlist implementaion.

To run:
```
cargo aoc -d 23
```
Oh yeah, the solution is specific to my input, adding a function that transforms any input
should be quite straight forward(basically just do the opposite of pretty print).

