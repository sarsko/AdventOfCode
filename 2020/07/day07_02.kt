import java.io.File
fun recur(graph:MutableMap<String, MutableSet<Pair<Int, String>>>, bag:String):Int{
    var cntr = 1
    for (e in graph[bag]!!){
        cntr+= e.first * recur(graph, e.second)
    }
    return cntr
}

fun main(){
    var graph = mutableMapOf<String, MutableSet<Pair<Int, String>>>()
    val input = File("kladd2.txt").readText().split("\n").map{it.split(", ")}
    for (line in input){
        if (line[0].length != 0 ){
                graph[line[0]] = mutableSetOf<Pair<Int, String>>()
                for (e in line.drop(1)){
                    if (e[0] != 'n'){
                        graph[line[0]]!!.add(Pair(e.take(1).toInt(), e.drop(2)))
                    }
            }
        }
    }
    var bags = 0
    for(pair in graph["shiny gold bag"]!!){
        bags += pair.first * recur(graph, pair.second)
    }
    var old_sum = 0
    var not_stabilized = true
    while (not_stabilized){
        var new_sum = 0
        for ((key, value) in graph){
            var tempset = mutableSetOf<Pair<Int, String>>()
            for (v in value){
                if (graph[key] != null && graph[v.second] != null){
                    for (e in graph[v.second]!!){
                        tempset.add(e)
                    }
                }
            }
            for (e in tempset){
                graph[key]!!.add(e)
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
        for (pair in value){
            if (pair.second == "shiny gold bag"){
                cnt++
                break
            }
        }
    }
    println(cnt)
    println(bags)
}

