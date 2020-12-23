use std::collections::HashMap;

fn pretty_print(cups: &Vec<usize>){
    let mut cur = 1;
    for _ in 1..cups.len(){
        print!("{}", cups[cur]);
        cur = cups[cur];
    }
    println!();
}

#[aoc(day23, part1)]
pub fn solve_part1(_input: &str) -> u32 {
    let mut cur = 1;
    let mut cups = vec![0usize, 9, 5, 4, 6, 8, 7, 2, 1, 3];
    for i in 0..100{
        let first = cups[cur];
        let second = cups[first];
        let third = cups[second];
        let mut dest = cur - 1;
        if dest == 0{
            dest = 9;
        }
        while dest == first || dest == second || dest == third{
            dest = dest - 1;
            if dest == 0{
                dest = 9;
            }
        }
        cups[cur] = cups[third];
        cups[third] = cups[dest];
        cups[dest] = first;
        cur = cups[cur];
    }
    pretty_print(&cups);
    0
}

#[aoc(day23, part2)]
pub fn solve_part2_vector(_input: &str) -> u64 {
    let mut cur = 1;
    let mut cups = vec![0usize, 9, 5, 4, 6, 8, 7, 2, 10, 3];
    for i in 11..1_000_001{
        cups.push(i);
    }
    cups.push(cur);
    for i in 0..10_000_000{
        let first = cups[cur];
        let second = cups[first];
        let third = cups[second];
        let mut dest = cur - 1;
        if dest == 0 {
            dest = 1_000_000;
        }
        while dest == first || dest == second || dest == third{
            dest = dest - 1;
            if dest == 0{
                dest = 1_000_000;
            }
        }
        cups[cur] = cups[third];
        cups[third] = cups[dest];
        cups[dest] = first;
        cur = cups[cur];
    }
    cups[1] as u64 * cups[cups[1]] as u64
}

pub fn solve_part2_hashmap(_input: &str) -> u64 {
    let mut cur = 1;
    let mut cups: HashMap<usize, usize> = HashMap::new();
    cups.insert(1, 9);
    cups.insert(2, 5);
    cups.insert(3, 4);
    cups.insert(4, 6);
    cups.insert(5, 8);
    cups.insert(6, 7);
    cups.insert(7, 2);
    cups.insert(8, 10);
    cups.insert(9, 3);
    for i in 11..1_000_001{
        cups.insert(i-1, i);
    }
    cups.insert(1_000_000, cur);
    for i in 0..10_000_000{
        let first = *cups.get(&cur).unwrap();
        let second = *cups.get(&first).unwrap();
        let third = *cups.get(&second).unwrap();
        let mut dest = cur - 1;
        if dest == 0 {
            dest = 1_000_000;
        }
        while dest == first || dest == second || dest == third{
            dest = dest - 1;
            if dest == 0{
                dest = 1_000_000;
            }
        }
        cups.insert(cur, *cups.get(&third).unwrap());
        cups.insert(third, *cups.get(&dest).unwrap());
        cups.insert(dest, first);
        cur = *cups.get(&cur).unwrap();
    }
    *cups.get(&1).unwrap() as u64 * *cups.get(&cups.get(&1).unwrap()).unwrap() as u64
}
