fun main(){
    var ribbon = 0
    var paper = 0
    for (i in 1..1000){
        val line = readLine()!!.split("x").map{it.toInt()}
        val l = line[0]
        val w = line[1]
        val h = line[2]
        val lw = l*w
        val wh = w*h
        val hl = h*l
        val least = minOf(l,w,h)
        val largest = maxOf(l,w,h)
        val middle = l+w+h - least - largest
        paper+=minOf(l,w,h)
        paper+=lw*2 + wh*2 + hl*2
        ribbon+= l*w*h
        ribbon+= least*2 + middle*2
    }
    println(paper)
    println(ribbon)
}
