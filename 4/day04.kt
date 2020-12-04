import java.io.File
fun main(){
    val passports = File("input4.txt").readText().split("\n\n")
    val passportRegex = "byr:|iyr:|eyr:|hgt:|hcl:|ecl:|pid:".toRegex()
    var cnt = 0
    passports.forEach{if(passportRegex.findAll(it).count()>6){cnt++}}
    println(cnt)
}
