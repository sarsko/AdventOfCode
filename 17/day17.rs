#[aoc(day17, part1)]
pub fn solve_part1(input: &str) -> i32 {
    let PADDING = 64;
    let mut cubes = vec![];
    for i in 0..32 {
        let mut plane = vec![];
        for e in 0..PADDING {
            let mut curr = vec![];
            for e2 in 0..PADDING {
                curr.push(0);
            }
            plane.push(curr);
        }
        cubes.push(plane);
    }
    let mut inp = vec![];
    for _ in 0..32 {
        let mut curr = vec![];
        for _ in 0..PADDING {
            curr.push(0);
        }
        inp.push(curr);
    }
    for l in input.lines() {
        let mut curr = vec![];
        for e in 0..28 {
            curr.push(0);
        }
        for e in l.chars() {
            if e == '#' {
                curr.push(1);
            }
            else if e == '.' {
                curr.push(0);
            }
        }
        for e in 0..28 {
            curr.push(0);
        }
        inp.push(curr);
    }
    for _ in 0..32 {
        let mut curr = vec![];
        for _ in 0..PADDING {
            curr.push(0);
        }
        inp.push(curr);
    }
    cubes.push(inp);
    for i in 0..32 {
        let mut plane = vec![];
        for e in 0..PADDING {
            let mut curr = vec![];
            for e2 in 0..PADDING {
                curr.push(0);
            }
            plane.push(curr);
        }
        cubes.push(plane);
    }
    for m in 0..6 {
        let mut ilayer = vec![];
        for i in 1..PADDING-1 {
            let mut jlayer = vec![];
            for j in 1..PADDING-1 {
                let mut klayer = vec![];
                for k in 1..PADDING-1 {
                    let mut neigh_cnt = -cubes[i][j][k];
                    for i2 in -1..2 {
                        for j2 in -1..2 {
                            for k2 in -1..2 {
                                neigh_cnt = neigh_cnt + cubes[(i as i32 +i2) as usize][(j as i32+j2) as usize][(k as i32+k2) as usize];
                            }
                        }
                    }
                    if neigh_cnt == 3 {
                        klayer.push(1);
                    }
                    else if neigh_cnt == 2 {
                        klayer.push(cubes[i][j][k]);
                    }
                    else {
                        klayer.push(0);
                    }
                }
                jlayer.push(klayer);
            }
            ilayer.push(jlayer);
        }
        for i in 0..PADDING-2 {
            for j in 0..PADDING-2 {
                for k in 0..PADDING-2 {
                    cubes[i][j][k] = ilayer[i][j][k];
                }
            }
        }
    }
    let mut rtot = 0;
    for i in 0..PADDING {
        for j in 0..PADDING {
            for k in 0..PADDING {
                rtot += cubes[i][j][k];
            }
        }
    }
    rtot
}

#[aoc(day17, part2)]
pub fn solve_part2(input: &str) -> i32 {
    let PADDING = 64;
    let mut cubes = vec![];
    for i in 0..32 {
        let mut planes = vec![];
        for _ in 0..PADDING {
            let mut plane = vec![];
            for e in 0..PADDING {
                let mut curr = vec![];
                for e2 in 0..PADDING {
                    curr.push(0);
                }
                plane.push(curr);
            }
            planes.push(plane);
        }
        cubes.push(planes);
    }
    let mut inp = vec![];
    for _ in 0..32 {
        let mut plane = vec![];
        for _ in 0..PADDING {
            let mut curr = vec![];
            for _ in 0..PADDING {
                curr.push(0);
            }
            plane.push(curr);
        }
        inp.push(plane);
    }
    let mut plane = vec![];
    for _ in 0..32 {
        let mut curr = vec![];
        for _ in 0..PADDING {
            curr.push(0);
        }
        plane.push(curr);
    }
    for l in input.lines() {
        let mut curr = vec![];
        for e in 0..28 {
            curr.push(0);
        }
        for e in l.chars() {
            if e == '#' {
                curr.push(1);
            }
            else if e == '.' {
                curr.push(0);
            }
        }
        for e in 0..28 {
            curr.push(0);
        }
        plane.push(curr);
    }
    for _ in 0..PADDING {
        let mut curr = vec![];
        for _ in 0..PADDING {
            curr.push(0);
        }
        plane.push(curr);
    }
    inp.push(plane);
    for _ in 0..32 {
        let mut plane = vec![];
        for _ in 0..PADDING {
            let mut curr = vec![];
            for _ in 0..PADDING {
                curr.push(0);
            }
            plane.push(curr);
        }
        inp.push(plane);
    }
    cubes.push(inp);
    for i in 0..32 {
        let mut planes = vec![];
        for _ in 0..PADDING {
            let mut plane = vec![];
            for e in 0..PADDING {
                let mut curr = vec![];
                for e2 in 0..PADDING {
                    curr.push(0);
                }
                plane.push(curr);
            }
            planes.push(plane);
        }
        cubes.push(planes);
    }
    for m in 0..6 {
        let mut ilayer = vec![];
        for i in 1..PADDING-1 {
            let mut jlayer = vec![];
            for j in 1..PADDING-1 {
                let mut klayer = vec![];
                for k in 1..PADDING-1 {
                    let mut hlayer = vec![];
                    for h in 1..PADDING-1 {
                        let mut neigh_cnt = -cubes[i][j][k][h];
                        for i2 in -1..2 {
                            for j2 in -1..2 {
                                for k2 in -1..2 {
                                    for h2 in -1..2 {
                                        neigh_cnt = neigh_cnt + cubes[(i as i32 +i2) as usize][(j as i32+j2) as usize][(k as i32+k2) as usize][(h as i32+h2) as usize];
                                    }
                                }
                            }
                        }
                        if neigh_cnt == 3 {
                            hlayer.push(1);
                        }
                        else if neigh_cnt == 2 {
                            hlayer.push(cubes[i][j][k][h]);
                        }
                        else {
                            hlayer.push(0);
                        }
                    }
                    klayer.push(hlayer);
                }
                jlayer.push(klayer);
            }
            ilayer.push(jlayer);
        }
        for i in 0..PADDING-2 {
            for j in 0..PADDING-2 {
                for k in 0..PADDING-2 {
                    for h in 0..PADDING-2 {
                        cubes[i][j][k][h] = ilayer[i][j][k][h];
                    }
                }
            }
        }
    }
    let mut rtot = 0;
    for i in 0..PADDING {
        for j in 0..PADDING {
            for k in 0..PADDING {
                for h in 0..PADDING {
                    rtot += cubes[i][j][k][h];
                }
            }
        }
    }
    rtot
}

