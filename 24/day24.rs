use std::collections::HashMap;
#[aoc_generator(day24)]
pub fn input_generator(input: &str) -> HashMap<(i32, i32), i32> {
    let mut hmap: HashMap<(i32, i32), i32> = HashMap::new();
    for line in input.lines(){
        let mut it = line.chars().peekable();
        let mut east = 0;
        let mut north = 0;
        while let Some(&c) = it.peek() {
            match c {
                's' => {
                    it.next();
                    let c2 = it.peek();
                    match c2 {
                        Some('e') => {north-=1;east+=1},
                        Some('w') => {north-=1;east-=1},
                        _ => panic!("Invalid char"),
                    }
                    it.next();
                }
                'n' => {
                    it.next();
                    let c2 = it.peek();
                    match c2 {
                        Some('e') => {north+=1;east+=1},
                        Some('w') => {north+=1;east-=1},
                        _ => panic!("Invalid char"),
                    }
                    it.next();
                }
                'e' => {east+=2; it.next();}
                'w' => {east-=2; it.next();}
                _ => panic!("Invalid char"),
            }
        }
        match hmap.get(&(east,north)){
            Some(1) => hmap.insert((east,north), 0),
            Some(0) => hmap.insert((east,north), 1),
            _ => hmap.insert((east,north), 1),
        };
    }
    hmap
}

#[aoc(day24, part1)]
pub fn solve_part1(input: &HashMap<(i32, i32), i32>) -> i32{
    input.values().sum()
}

#[aoc(day24, part2)]
pub fn solve_part2(input: &HashMap<(i32, i32), i32>) -> i32{
    let mut oldmap = input.clone();
    for i in 0..100{
        let mut nextmap: HashMap<(i32, i32), i32> = HashMap::new();
        let mut tmpmap: HashMap<(i32, i32), i32> = HashMap::new();
        for (east, north) in oldmap.keys(){
            if oldmap.get(&(*east, *north)).unwrap() == &1{
                if oldmap.get(&(east-1, north-1)).is_none(){
                    tmpmap.insert((east-1, north-1), 0);
                }
                if oldmap.get(&(east+1, north+1)).is_none(){
                    tmpmap.insert((east+1, north+1), 0);
                }
                if oldmap.get(&(east-2, *north)).is_none(){
                    tmpmap.insert((east-2, *north), 0);
                }
                if oldmap.get(&(east+2, *north)).is_none(){
                    tmpmap.insert((east+2, *north), 0);
                }
                if oldmap.get(&(east-1, north+1)).is_none(){
                    tmpmap.insert((east-1, north+1), 0);
                }
                if oldmap.get(&(east+1, north-1)).is_none(){
                    tmpmap.insert((east+1, north-1), 0);
                }
            }
        }
        for (key, val) in tmpmap{
            oldmap.insert(key, val);
        }
        for (&key, &val) in &oldmap{
            if val == 1 {
                let (east, north) = key;
                let cnt = count(&oldmap, east, north);
                if cnt == 0 || cnt > 2{
                    nextmap.insert((east,north), 0);
                }
                else{
                    nextmap.insert((east,north), 1);
                }
            }
            if val == 0 {
                let (east, north) = key;
                let cnt = count(&oldmap, east, north);
                if cnt == 2{
                    nextmap.insert((east,north), 1);
                }
                else{
                    nextmap.insert((east,north), 0);
                }
            }
        }
        oldmap = nextmap;
    }
    oldmap.values().sum()
}

fn count(hmap: &HashMap<(i32, i32), i32>, east: i32, north: i32) -> i32{
    hmap.get(&(east-1, north-1)).unwrap_or_else(||&0) + hmap.get(&(east+1, north+1)).unwrap_or_else(||&0) +
        hmap.get(&(east-2, north)).unwrap_or_else(||&0) + hmap.get(&(east+2, north)).unwrap_or_else(||&0) +
        hmap.get(&(east-1, north +1)).unwrap_or_else(||&0) + hmap.get(&(east+1, north-1)).unwrap_or_else(||&0)
}



