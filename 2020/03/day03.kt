fun main(){
    val lon = 3 // longitude = east west
    var right = 0 // right from 0,0
    val fline = readLine()!!
    var width = fline.length
    var crashes = 0
    for (i in 2..323){
        val line = readLine()!!
        right = (right + lon) % width
        if (line[right] == '#'){
            crashes++
        }
    }
    println(crashes)
}
