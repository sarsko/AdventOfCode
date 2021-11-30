## Day 3

### 3-1

Pretty straightforward solution. I think this is the most naive non-naive solution(the really naive
solutions are the ones where you replicate input or have an array or check out of bounds etc.)

Tbh, the good Java solution is to instead of using modulo, just using try and catch(and not storing
the line length), and in the catch block, try-catching repeatedly (and increasing a counter) until you get
a valid index. Actually that is such a terrible idea I might actually try it.

```
kotlinc day03.kt && cat input3.txt | Kotlin Day03Kt
```

EDIT:

Okay, so I had to make the terrible Java version. It works. It is quite terrible(but less terrible
than expected).

I like it quite a lot.

### 3-2

Here I just changed parameters and hacked it together for each rule(XR YD) - that's the code in 03_old.

Dissatisfied I sorta-generalized it. An okay solution.
```
kotlinc day03_02.kt && cat input3.txt | Kotlin Day03_02Kt
```
