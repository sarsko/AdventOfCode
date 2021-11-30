tn ← 'input.txt'⎕NTIE 0
task1←{((2⊥'BBBBBBB'=(⎕NREAD tn 80 7 ⍵)) × 8) + (2⊥'RRR'=(⎕NREAD tn 80 3 (7 + ⍵)))}
⌈/values←(task1)¨(0,11×⍳844) ⍝ "map the task1 function over 0,11,22..11*844"
values(∪~∩)(⌊/values-1)↓⍳(⌈/values) ⍝ "find uniques of values and floor values..ceil values"
