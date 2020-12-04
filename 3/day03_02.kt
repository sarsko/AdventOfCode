fun main(){
    // R1 D1 = 60
    // R3 D1 = 225
    // R5 D1 = 57
    // R7 D1 = 58
    // R1 D2 = 25
    var rightArray = arrayOf(1, 3, 5, 7, 1)
    var crashArray = Array<Int>(5){0}
    var posArray = Array<Int>(5){0}
    var divArray = arrayOf(1, 1, 1, 1, 2)
    val fline = readLine()!!
    var width = fline.length
    var depth = 0
    for (i in 2..323){
        val line = readLine()!!
        depth++
        for (j in 0..posArray.size-1){
            if ((depth % divArray[j]) == 0){
                posArray[j] = (posArray[j] + rightArray[j]) % width
                if (line[posArray[j]] == '#'){
                    crashArray[j]++
                }
            }
        }
    }
    rightArray.forEach {print(it);print(" - ")}
    println()
    crashArray.forEach {print(it);print(" - ")}
}


