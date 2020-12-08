import java.io.File
fun main(){
    val input = File("input.txt").readText().split("\n").map{it.split(" ")}
    var visitedset = mutableSetOf<Int>()
    var acc = 0
    var i = 0
    var changeJmps = true
    var changeNumber = 0
    var increaseNumber = 0
    while(true){
        if (input[i].size < 2){
            println(acc)
            break
        }
        if (visitedset.contains(i)){
            if (increaseNumber==0){
                println(acc)
            }
            visitedset = mutableSetOf<Int>()
            i = 0
            acc = 0
            increaseNumber++
            changeNumber = increaseNumber
        }
        visitedset.add(i)
        val firstChar = input[i][0][0]
        if (firstChar == 'a'){
            if (input[i][1][0] == '+'){
                acc += input[i][1].drop(1).toInt()
            }
            else{
                acc -= input[i][1].drop(1).toInt()
            }
            i++
        }
        changeNumber--
        if (firstChar == 'n' || (changeNumber == 0 && changeJmps)){
            i++
        }
        else if (firstChar == 'j' || (changeNumber == 0 && !changeJmps)){
            if (input[i][1][0] == '+'){
                i += input[i][1].drop(1).toInt()
            }
            else{
                i -= input[i][1].drop(1).toInt()
            }
        }
    }

}
