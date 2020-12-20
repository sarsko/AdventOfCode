#[aoc(day16, part1)]
pub fn solve_part1(input: &str) -> i32 {
    let mut sum = 0;
    for l in input.lines().skip(25) {
        for num in l.split(",").map(|s| s.parse::<i32>().unwrap()) {
            if num < 31 || num > 970 {
                sum += num;
            }
        }
    }
    sum
}

#[aoc(day16, part2)]
pub fn solve_part2(input: &str) -> i64 {
    let low: [i32; 20] = [
        45, 36, 46, 46, 35, 42, 47, 31, 48, 49, 33, 35, 38, 41, 44, 41, 47, 44, 30, 38,
    ];
    let high: [i32; 20] = [
        950, 956, 967, 950, 974, 962, 953, 970, 964, 964, 959, 951, 950, 962, 962, 956, 954, 964,
        970, 965,
    ];
    let upper: [i32; 20] = [
        422, 741, 788, 57, 99, 883, 83, 227, 840, 487, 263, 509, 590, 266, 402, 615, 156, 313, 110,
        541,
    ];
    let lower: [i32; 20] = [
        444, 752, 806, 70, 108, 903, 95, 240, 853, 499, 381, 522, 601, 285, 419, 634, 178, 338,
        133, 550,
    ];
    let mut valid_ticks: Vec<Vec<i32>> = Vec::new();
    for l in input.lines().skip(25) {
        let curr: Vec<i32> = l.split(",").map(|s| s.parse::<i32>().unwrap()).collect();
        let mut valid = true;
        for num in &curr {
            if num < &31 || num > &970 {
                valid = false;
            }
        }
        if valid {
            valid_ticks.push(curr);
        }
    }
    let mut possibilities = vec![vec![0; 0]; 20];
    for i in 0..20 {
        'second: for j in 0..20 {
            for v in &valid_ticks {
                let curr = v[i];
                if curr < low[j] || curr > high[j] || (curr > upper[j] && curr < lower[j]) {
                    continue 'second;
                }
            }
            possibilities[i].push(j as i32);
        }
    }
    let mut taken: Vec<i32> = Vec::new();
    let mut done = false;
    let myTicket: [i32; 20] = [
        109, 199, 223, 179, 97, 227, 197, 151, 73, 79, 211, 181, 71, 139, 53, 149, 137, 191, 83,
        193,
    ];
    let mut solutions: Vec<usize> = Vec::new();
    while !done {
        let mut cnt = 0;
        for field in &possibilities {
            let mut difference = vec![];
            for i in field {
                if !taken.contains(&i) {
                    difference.push(i);
                }
            }
            if solutions.len() == 6 {
                done = true;
            }
            if difference.len() == 1 {
                let val = *difference[0];
                if val < 6 {
                    solutions.push(cnt);
                }
                taken.push(val);
            }
            cnt += 1;
        }
    }
    let mut sum: i64 = 1;
    for i in solutions.iter() {
        sum *= myTicket[*i] as i64;
    }
    sum
}
