
use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind, Read};
use std::time::Instant;

/*
fn read(io: File) -> Vec<Vec<usize>> {
    let now = Instant::now();
    let br = BufReader::new(io);
    let mut out = vec![];
    let mut curr = vec![];
    for line in br.lines() {
        let line = line.unwrap();
        if line.is_empty() {
            out.push(curr);
            curr = vec![]
        } else {
            curr.push(line.trim().parse().unwrap());
        }
    }
    println!("{:?}", now.elapsed());
    out
}

fn main() -> Result<(), Error> {
    let data_t = read(File::open("francesco_1657.txt")?);
    let mut data = data_t.iter().map(|e| e.iter().sum()).collect::<Vec<usize>>();
    data.sort();
    data.reverse();
    println!("{}", data[0]);
    println!("{}", data[..3].iter().sum::<usize>());
    Ok(())
}
*/

fn read(io: File) -> Vec<usize> {
    let br = BufReader::with_capacity(1024 * 64, io);
    let mut out = vec![];
    let mut curr: usize = 0;
    for line in br.lines() {
        let line = line.unwrap();
        if !line.is_empty() {
            curr += line.trim().parse::<usize>().unwrap();
        } else {
            out.push(curr);
            curr = 0;
        }
    }
    out
}

fn main() -> Result<(), Error> {
    let now = Instant::now();
    let mut data = read(File::open("francesco_1657.txt")?);
    data.sort();
    data.reverse();
    println!("{}", data[0]);
    println!("{}", data[..3].iter().sum::<usize>());
    println!("{:?}", now.elapsed());
    Ok(())
}
