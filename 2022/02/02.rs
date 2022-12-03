use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind, Read};

#[derive(Debug, Clone, Copy, Eq, PartialEq)]
enum RPS {
    R,
    P,
    S,
}


impl RPS {
    fn get_shape_score(self) -> usize {
        match self {
            RPS::R => 1,
            RPS::P => 2,
            RPS::S => 3,
        }
    }

    fn part1(self, o: RPS) -> usize {
        o.get_shape_score() + match (self, o) {
            (a, b) if a == b => 3,
            (RPS::R, RPS::P) | (RPS::P, RPS::S) | (RPS::S, RPS::R) => 6,
            _ => 0,

        }
    }

    fn part2(self, o: RPS) -> usize {
        match o {
            RPS::R => match self {
                RPS::R => 3,
                RPS::P => 1,
                RPS::S => 2,
            }, // lose
            RPS::P => self.get_shape_score() + 3, // draw
            RPS::S => 6 + match self {
                RPS::R => 2,
                RPS::P => 3,
                RPS::S => 1,
            }, // Win
        }
    }

}

fn read<R: Read>(io: R) -> Result<Vec<(RPS, RPS)>, Error> {
    let br = BufReader::new(io);
    let mut out = vec![];
    for line in br.lines() {
        let line = line?;
        let mut spl = line.split(" ");
        out.push((
            match spl.next().unwrap() {
                "A" => RPS::R,
                "B" => RPS::P,
                "C" => RPS::S,
                _ => panic!(),
            },
            match spl.next().unwrap() {
                "X" => RPS::R,
                "Y" => RPS::P,
                "Z" => RPS::S,
                _ => panic!(),
        }));
    }
    Ok(out)
}

fn main() -> Result<(), Error> {
    let data = read(File::open("input.txt")?)?;
    let res: usize = data.iter().map(|(o, y)| o.part1(*y)).sum();
    println!("{:?}", res);
    let res: usize = data.iter().map(|(o, y)| o.part2(*y)).sum();
    println!("{:?}", res);
    Ok(())
}
