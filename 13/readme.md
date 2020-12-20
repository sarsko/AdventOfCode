## Day 13

Today's solution went quickly.

I guess there is a decent possibility of over-complicating this, and getting the complete solution with no manual input would probably take some time.
Also, either implementing a constraint solver or the chinese remnainder theorem (or linking to a solver properly) would probably be a fair bit of work.

### Part 1

Just iterate through and print each bus number and how long you have to wait. Multiplying lowest wait with bus number has to be done manually.

### Part 2

Prints each bus number and how long after t = 0 it has to depart. This is then used to (manually) generate a set of constraints - (x mod 37 = 0), ((x+27) mod 41 = 0)
etc. which I then put into [Wolfram Alpha](https://www.wolframalpha.com/input/?i=%28x+mod+37%3D0%29+%CE%9B+%28%28x%2B27%29+mod+41%3D+0%29+%CE%9B+%28%28x%2B37%29+mod+587+%3D+0%29+%CE%9B+%28%28x%2B42%29+mod+13+%3D+0%29%CE%9B+%28%28x%2B56%29+mod+19+%3D+0%29%CE%9B+%28%28x%2B60%29+mod+23+%3D+0%29+%CE%9B+%28%28x%2B66%29+mod+29+%3D+0%29+%CE%9B+%28%28x%2B68%29+mod+733+%3D+0%29%CE%9B+%28%28x%2B85%29+mod+17+%3D+0%29)
The solution is the constant part.

Quick and easy.

To run:
```
cargo aoc -d 13
```

