fun main(){
    var floor = 0
    var index = 0
    val line = readLine()!!
    for (c in line){
        index++
        if (c == '('){
            floor++
        }
        else{
            floor--
            if (floor < 0) {
                println(index)
                break
            }
        }
    }
}


