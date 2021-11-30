import java.io.File
fun main(){
    val input = File("input.txt").readText().split("\n").dropLast(1).map{it.toInt()}.sorted()
    var onecount = 0
    var threecount = 1
    var last = 0
    for (e in input){
        onecount += if (e-last == 1) 1 else 0
        threecount += if (e-last == 3) 1 else 0
        last = e
    }
    println(onecount*threecount)

    var waysTo = LongArray(input.takeLast(1)[0]+1) {0}
    waysTo[0] = 1
    waysTo[input.take(1)[0]] = 1
    waysTo[input.drop(1).take(1)[0]] = if (input.drop(1).take(1)[0] == 4) 1 else 2
    for (e in input.drop(2)){
        waysTo[e] = waysTo[e-3] + waysTo[e-2] + waysTo[e-1]
    }
    println(waysTo.takeLast(1)[0])

}


