import java.io.File
fun main(){
    val passports = File("input4.txt").readText().split("\n\n")
    val passportRegex = "(byr:(19[2-9][0-9]|200[0-2])(\n| |$))|(iyr:(201[0-9]|2020)(\n| |$))|(eyr:(202[0-9]|2030)(\n| |$))|(hgt:(1[5-8][0-9]|19[0-3])cm(\n| |$))|(hgt:(5[8-9]|6[0-9]|7[0-6])in(\n| |$))|(hcl:#[0-9a-f]{6}(\n| |$))|(ecl:(amb|blu|brn|gry|grn|hzl|oth)(\n| |$))|(pid:[0-9]{9}(\n| |$))".toRegex()
    var cnt = 0
    passports.forEach{if(passportRegex.findAll(it).count()>6){cnt++}}
    println(cnt)
}
