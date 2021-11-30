use std::collections::HashSet;
use std::collections::HashMap;
#[aoc(day21, part1)]
pub fn solve_part1(input: &str) -> usize {
    let mut allerg_to_ing: HashMap<&str, HashSet<&str>> = HashMap::new();
    let mut all_ingredients: HashSet<&str> = HashSet::new();
    for line in input.lines(){
        let index = line.chars().position(|r| r == '(').unwrap();
        let allergenes = &line[index+10..line.len()-1].split(", ").collect::<Vec<&str>>();
        let ingredients = &line[..index-1].split(" ").collect::<Vec<&str>>();
        for allerg in allergenes{
            let mut hs = HashSet::new();
            for &ingredi in ingredients{
                all_ingredients.insert(ingredi);
                hs.insert(ingredi);
            }
            if allerg_to_ing.contains_key(allerg){
                hs = hs.intersection(&allerg_to_ing.get(allerg).unwrap()).copied().collect();
            }
            allerg_to_ing.insert(allerg, hs);
        }
    }
    for (k,v) in allerg_to_ing{
        println!("Allerg: {:?} may be: {:?}", k, v);
        all_ingredients = all_ingredients.difference(&v).copied().collect();
    }
    input.split_whitespace().filter(|w| all_ingredients.contains(w)).count()
}

#[aoc(day21, part2)]
pub fn solve_part2(input: &str) -> i64 {
    0
}
