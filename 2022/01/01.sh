# awk command is stolen from the aoc reddit, as I could not find a way to do it in any other way
awk -v RS= '{$1=$1}1' input.txt | sed 's/ /+/g' | bc | sort -n | tail -n 1
awk -v RS= '{$1=$1}1' input.txt | sed 's/ /+/g' | bc | sort -n | tail -n 3 | paste -sd+ - | bc
