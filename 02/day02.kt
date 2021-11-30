fun main(){
    var cnt = 0
    for (i in 1..1000){
        val line = readLine()!!
        val pol_pass = line.split(": ")
        val pol_lett = pol_pass[0].split(" ")
        val from_to = pol_lett[0].split("-")

        val from = from_to[0].toInt()
        val to = from_to[1].toInt()
        val letter = pol_lett[1][0]
        val pass = pol_pass[1]
        var freq = 0
        for (j in 0..pass.length - 1) {
            if (letter == pass[j]) {
                freq++
            }
        }
        if ((from <= freq) && (freq <= to)){
            cnt++;
        }
    }
    println(cnt)
}
