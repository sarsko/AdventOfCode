import java.io.File
fun main(){
    var graph = mutableMapOf<String, Set<String>>()
    val input = File("input_01.txt").readText().split("\n").map{it.split(", ")}
    for (line in input){
        if (line[0].length != 0 ){
            if (graph[line[0]] == null){
                graph[line[0]] = line.drop(1).toSet()
            }
            else{
                graph[line[0]] = graph[line[0]]!! union line.drop(1).toSet()
            }
        }
    }
    var old_sum = 0
    var not_stabilized = true
    while (not_stabilized){
        var new_sum = 0
        for ((key, value) in graph){
            for (v in value){
                if (graph[key] != null && graph[v] != null){
                    graph[key] = graph[key]!! union graph[v]!!
                }
            }
            new_sum += value.size
        }
        if (new_sum == old_sum){
            not_stabilized = false
        }
        old_sum = new_sum
    }
    var cnt = 0
    for ((_, value) in graph){
        if (value.contains("shiny gold bag")){
            cnt++
        }
    }
    println(cnt)
}

