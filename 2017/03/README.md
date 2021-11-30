## Day 3

Ah, a nocode day. I feel like a double nocode is quite rare, but last year had a
couple where one of the parts could be nocoded.

### Part 1

Realized the bottom-right tiles were perfect square. Calulated `sqrt(2893269)`
and got `537`. `2893269 - 537 * 537 = 957`, so I "walked" `537` up and then `420`
to the left. Then I started fumbling with the fact that you go "plus one" to the
right and to the top, and that had to be accounted for, so I guessed `418` which
was too low. Increased guess to `425` to give myself a wide range in case I had
messed up more than I thought. That was too high, so I redid the calculation
from earlier and got `419`.

### Part 2

I felt like this sequence had to be either partially or wholly described
somewhere. Googled for "known sequences" and ended up on
[OEIS](https://oeis.org/), which I remember to have seen either last year or
some Kattis/Euler stuff. Wrote up the the first numbers and searched, and sure
enough. OEIS good. Thanks to Klaus Brockhaus, I guess.

