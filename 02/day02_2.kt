fun main(){
    var cnt = 0
    for (i in 1..1000){
        val line = readLine()!!
        val pol_pass = line.split(": ")
        val pol_lett = pol_pass[0].split(" ")
        val from_to = pol_lett[0].split("-")

        val from = from_to[0].toInt() - 1
        val to = from_to[1].toInt() - 1
        val letter = pol_lett[1][0]
        val pass = pol_pass[1]

        if ((pass[from] == letter) xor (pass[to] == letter)){
            cnt++;
        }
    }
    println(cnt)
}

