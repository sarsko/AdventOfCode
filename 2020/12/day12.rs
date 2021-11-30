#[aoc(day12, part1)]
pub fn solve_part1(input: &str) -> isize {
    let mut east = 0;
    let mut north = 0;
    let mut e_mult = 1;
    let mut n_mult = 0;
    for l in input.lines(){
        let (act, val) = l.split_at(1);
        let val = val.parse::<isize>().unwrap();
        match act {
            "E" => east+=val,
            "W" => east-=val,
            "N" => north+=val,
            "S" => north-=val,
            "F" => {north+=val * n_mult;east+= val * e_mult},
            "L" => {for _ in 0..(val/90){
                let tmp = e_mult; e_mult = -n_mult; n_mult = tmp}},
            "R" => {for _ in 0..(val/90){
                let tmp = n_mult; n_mult = -e_mult; e_mult = tmp}},
            _ => panic!("Invalid char"),
        }
    }
    north.abs()+east.abs()
}

#[aoc(day12, part2)]
pub fn solve_part2(input: &str) -> isize {
    let mut east = 10;
    let mut north = 1;
    let mut ship_north = 0;
    let mut ship_east = 0;
    for l in input.lines(){
        let (act, val) = l.split_at(1);
        let val = val.parse::<isize>().unwrap();
        match act {
            "E" => east+=val,
            "W" => east-=val,
            "N" => north+=val,
            "S" => north-=val,
            "F" => {ship_north+=val*north;ship_east+=val*east},
            "L" => {for _ in 0..(val/90){
                let tmp = east; east = -north; north=tmp}},
            "R" => {for _ in 0..(val/90){
                let tmp = north; north = -east; east=tmp}},
            _ => panic!("Invalid char"),
        }
    }
    ship_east.abs()+ship_north.abs()
}
