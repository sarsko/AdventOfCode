#[aoc(day13, part1)]
pub fn solve_part1(input: &str) -> i32 {
    let numbers: Vec<i32> = input.split(|c| c == '\n' || c == ',').filter(|&c| c != "x").into_iter().map(|c| c.parse::<i32>().unwrap()).collect();
    let first = numbers[0];
    for num in numbers{
        println!("num: {} wait: {}",num, num-(first%num));
    }
    0
}

#[aoc(day13, part2)]
pub fn solve_part2(input: &str) -> isize {
    let mut cnt = 0;
    for e in input.split(","){
        if e != "x"{
            println!("{} cnt: {}", e, cnt);
        }
        cnt += 1;
    }
    // (x mod 37=0) Λ ((x+27) mod 41= 0) Λ ((x+37) mod 587 = 0) Λ ((x+55) mod 13 = 0)Λ ((x+56) mod 19 = 0)Λ ((x+60) mod 23 = 0) Λ ((x+66) mod 29 = 0) Λ ((x+68) mod 733 = 0)Λ ((x+85) mod 17 = 0)
    0
}
