fn solve(seed: Vec<usize>, end: usize) -> usize {
    let mut last_spoken = 1;
    let mut newest = vec![0i32; end];
    let mut sec_new = vec![0i32; end];
    let mut cntr = 1;
    for e in seed{
        newest[e] = cntr;
        cntr+=1
    }
    for i in cntr..(end+1) as i32{
        let val1 = newest[last_spoken];
        let val2 = sec_new[last_spoken];
        if val2 == 0{
            last_spoken = 0;
        }
        else{
            last_spoken = (val1 - val2) as usize;
        }
        sec_new[last_spoken] = newest[last_spoken];
        newest[last_spoken] = i;
    }
    last_spoken
}

#[aoc(day15, part1)]
pub fn solve_part1(_input: &str) -> usize {
    solve(vec![9usize, 6, 0, 10, 18, 2, 1], 2020)
}

#[aoc(day15, part2)]
pub fn solve_part2(_input: &str) -> usize {
    solve(vec![9usize, 6, 0, 10, 18, 2, 1], 30000000)
}
