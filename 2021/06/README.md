## Day 6

Did it first in Haskell. That version was too naïve for part 2, and I couldn't
be bothered making the fast version, so I just hacked together something in
Python. Fairly happy about my Python solution, it is fast enough and uses a
generator. I might be missing something, but I don't understand why getting the
nth value of a generator is so cumbersome. Like sure, one could import
something, or wrap the generator in i.e. another generator, but it would be
really nice to be able to say `calcFishies(fishies).nth(80)` and
`calcFishies(fishies).nth(256)` or something like it.

To run:
```
runhaskell 06.hs
```
for the very slow Haskell version

```
python3 06.py
```
for the not so slow Python version

