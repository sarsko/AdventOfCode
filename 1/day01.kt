fun main(){
    var diffset = mutableSetOf<Int>()
    var lookset = mutableSetOf<Int>()
    for (i in 1..200){
        val num = readLine()!!.toInt()
        lookset.add(num)
        diffset.add(2020 - num)
    }
    print(lookset intersect diffset)
}
