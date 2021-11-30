import java.io.File
fun main(){
    val groups = File("input.txt").readText().split("\n\n")
    println(groups.map{ g -> g.toCharArray().filter{ c -> c >= 'a'&& c <='z'}.toSet().size}.sum())
    var task2_cntr = 0
    for (e in groups){
        var totSet =('a'..'z').take(26).toSet()
        for (p in e.split("\n")){
            if (p.isEmpty()){
                continue
            }
            totSet =(p.toCharArray().toSet() intersect totSet)
        }
        task2_cntr += totSet.size
    }
    println(task2_cntr)
}
