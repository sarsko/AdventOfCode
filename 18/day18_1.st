out := 0.
"
SmallInteger extend [
    myMeth: param [
        ^(self * param).
    ]
]
"
stdin linesDo: [ :line |
    out := out + (Behavior evaluate: line).
].
Transcript show: (out asString).
