type Layout = Vec<Vec<char>>;

#[aoc_generator(day11)]
pub fn input_generator(input: &str) -> Layout {
    input
        .lines()
        .map(|l| l.chars().collect::<Vec<char>>())
        .collect()
}

fn value(input: &Layout, i: usize, j: usize) -> u32 {
    match input.get(i){
        None => 0,
        y => match y.unwrap().get(j){
            None => 0,
            Some('#') => 1,
            _ => 0,
        }
    }
}

fn count(input: &Layout, i: usize, j: usize) -> u32 {
    value(&input, i-1, j-1) + value(&input, i-1, j) + value(&input, i-1, j+1) +
    value(&input, i, j-1) + value(&input, i, j+1) +
    value(&input, i+1, j-1) + value(&input, i+1, j) + value(&input, i+1, j+1)
}

#[aoc(day11, part1)]
pub fn solve_part1(input: &Layout) -> usize {
    let mut updated = true;
    let mut old: Vec<Vec<char>> = input.clone();
    while updated {
        updated = false;
        let mut new: Vec<Vec<char>> = Vec::new();
        for i in 0..old.len() {
            let mut vec = Vec::new();
            for j in 0..old[i].len() {
               vec.push(match old[i][j] {
                    '.' => '.',
                    '#' => if count(&old, i, j) >= 4 { updated = true;'L' } else { '#' },
                    'L' => if count(&old, i, j) == 0 { updated = true;'#' } else { 'L' },
                    _ => panic!("Invalid char"),
                });
            }
            new.push(vec);
        }
        old = new.clone()
    }
    old.iter().flatten().filter(|&n| *n == '#').count()
}

fn value_2(input: &Layout, i: usize, j: usize, i_dir: i32, j_dir: i32) -> u32 {
    match input.get(i){
        None => 0,
        y => match y.unwrap().get(j){
            None | Some('L') => 0,
            Some('#') => 1,
            _ => value_2(&input, (i as i32 + i_dir) as usize, (j as i32 + j_dir) as usize, i_dir, j_dir),
        }
    }
}

fn count_2(input: &Layout, i: usize, j: usize) -> u32 {
    value_2(&input, i-1, j-1, -1, -1) + value_2(&input, i-1, j, -1, 0) + value_2(&input, i-1, j+1, -1, 1) +
    value_2(&input, i, j-1, 0, -1) + value_2(&input, i, j+1, 0, 1) +
    value_2(&input, i+1, j-1, 1, -1) + value_2(&input, i+1, j, 1, 0) + value_2(&input, i+1, j+1, 1, 1)
}

#[aoc(day11, part2)]
pub fn solve_part2(input: &Layout) -> usize {
    let mut updated = true;
    let mut old: Vec<Vec<char>> = input.clone();
    while updated {
        updated = false;
        let mut new: Vec<Vec<char>> = Vec::new();
        for i in 0..old.len() {
            let mut vec = Vec::new();
            for j in 0..old[i].len() {
               vec.push(match old[i][j] {
                    '.' => '.',
                    '#' => if count_2(&old, i, j) >= 5 { updated = true;'L' } else { '#' },
                    'L' => if count_2(&old, i, j) == 0 { updated = true;'#' } else { 'L' },
                    _ => panic!("Invalid char"),
                });
            }
            new.push(vec);
        }
        old = new.clone()
    }
    old.iter().flatten().filter(|&n| *n == '#').count()
}

