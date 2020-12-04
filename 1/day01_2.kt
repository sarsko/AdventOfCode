fun main(){
    var diffset = mutableSetOf<Int>()
    var lookset = mutableSetOf<Int>()
    for (i in 1..200){
        val num = readLine()!!.toInt()
        lookset.add(num)
        diffset.add(2020 - num)
    }
    print(lookset intersect diffset)
    var thirdset = mutableSetOf<Int>()
    for (diff in diffset){
        for (look in lookset){
            val rest = diff - look
            thirdset.add(rest)
        }
    }
    print(thirdset intersect lookset)
}

