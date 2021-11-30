fun main(){
    // R1 D1 = 60
    // R3 D1 = 225
    // R5 D1 = 57
    // R7 D1 = 58
    // R1 D2 = 25
    val lon = 1 // longitude = east west
    var right = 0 // right from 0,0
    val fline = readLine()!!
    var width = fline.length
    var crashes = 0
    var div2 = 0
    for (i in 2..323){
        val line = readLine()!!
        div2++
        if (div2%2 == 0){
            right = (right + lon) % width
            if (line[right] == '#'){
                crashes++
            }
        }
    }
    println(crashes)
}


