## Day 24

Ah, what a bunch of nerds we are, doing AoC on Christmas Eve.

Today was quite fun. Some parsing and some cellular automaton without either being too cumbersome.

### My solution

I guess there is a challenge in choosing the correct representation for the flooring. After looking a bit
on the picture at [the Wikipedia](https://en.wikipedia.org/wiki/Hexagonal_tiling) article, I realized that
a good representation is to keep track of north and east and that each "move"(se, sw, nw, ne, e, w) moves
exactly one(e, w = ±1, se,sw, ne,sw = ±0.5, ±0.5). Floats and HashMaps don't go well together(besides, one
should generally stay away from floats if one can(10 and 5 is "better" than 1 and 0.5)), so I multiplied
everything with 2.

My parser(with a pseudolexer inside) could be beautified(and generalized) quite a bit, but it works. Just
read one symbol and then if it is 's' or 'n', read another. After a line is parsed, the (east, north) is
added to the HashMap. If there already is an entry in the map, "flip" the value(1 is black, 0 is white).

When all lines have been parsed, getting the value for part 1 is as easy as adding all the values in the
map.

My part 2 solution is algorithmically fairly straight forward, it just looks ugly. I pad(yes, this
is not very efficient) the map with new white tiles(the tmpmap stuff). I then iterate through, inserting
in the new map based on the count(just count neighbours). Again, the value for part 2 is given by just
adding all the values in the map.

To run:
```
cargo aoc -d 24
```
