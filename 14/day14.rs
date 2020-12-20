use std::collections::HashMap;

#[aoc(day14, part1)]
pub fn solve_part1(input: &str) -> i64 {
    let mut mask = "";
    let mut memory = HashMap::new();
    for line in input.lines(){
        match line.chars().nth(1).unwrap(){
            'a' => mask = &line[7..],
            _ => {memory.insert(
                line.split(" ").collect::<Vec<&str>>()[1].parse::<i64>().unwrap(),
                value(&mask,
                    line.split(" ").collect::<Vec<&str>>()[2].parse::<i64>().unwrap()));},
            }
    }
    let mut sum = 0;
    for (_, v) in memory{
        sum+=v;
    }
    sum
}
fn value(mask: &str, val: i64) -> i64 {
    let bin_val = format!("{:0>36b}", val);
    let mut out_val: Vec<char> = Vec::new();
    for (m, v) in mask.chars().zip(bin_val.chars()){
        out_val.push(match m {
            'X' => v,
            _ => m,
        });
    }
    i64::from_str_radix(&out_val.iter().collect::<String>(), 2).unwrap()
}

#[aoc(day14, part2)]
pub fn solve_part2(input: &str) -> i64 {
    let mut mask = "";
    let mut memory:HashMap<i64, i64> = HashMap::new();
    for line in input.lines(){
        match line.chars().nth(1).unwrap(){
            'a' => mask = &line[7..],
            _ => {insert_addr_val(&mut memory,
                &calc_addr(&mask, line.split(" ").collect::<Vec<&str>>()[1].parse::<i64>().unwrap()),
                    line.split(" ").collect::<Vec<&str>>()[2].parse::<i64>().unwrap());
                },
            }
    }
    let mut sum = 0;
    for (_, v) in memory{
        sum+=v;
    }
    sum
}
fn insert_addr_val(map: &mut HashMap<i64, i64>, addr: &str, val: i64){
    for i in 0..addr.len(){
        if addr.as_bytes()[i] == 'X' as u8{
            insert_addr_val(map, &format!("{}{}{}",&addr[0..i], "0", &addr[i+1..]), val);
            insert_addr_val(map, &format!("{}{}{}",&addr[0..i], "1", &addr[i+1..]), val);
            return;
        }
    }
    map.insert(i64::from_str_radix(&addr, 2).unwrap(), val);
}

fn calc_addr(mask: &str, addr: i64) -> String {
    let bin_val = format!("{:0>36b}", addr);
    let mut out: Vec<char> = Vec::new();
    for (m, v) in mask.chars().zip(bin_val.chars()){
        out.push(match m {
            'X' => 'X',
            '1' => m,
            _ => v,
        });
    }
    out.iter().collect::<String>()
}
