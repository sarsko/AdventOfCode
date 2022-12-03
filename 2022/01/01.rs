use std::fs::File;
use std::io::{BufRead, BufReader, Error, ErrorKind, Read};

fn read<R: Read>(io: R) -> Result<Vec<Vec<usize>>, Error> {
    let br = BufReader::new(io);
    let mut out = vec![];
    let mut curr = vec![];
    for line in br.lines() {
        let line = line?;
        if line.is_empty() {
            out.push(curr);
            curr = vec![]
        } else {
            curr.push(line.trim().parse().map_err(|e| Error::new(ErrorKind::InvalidData, e))?);
        }
    }
    Ok(out)
}

fn main() -> Result<(), Error> {
    let mut data = read(File::open("input.txt")?)?.into_iter().map(|e| e.iter().sum()).collect::<Vec<usize>>();
    data.sort();
    data.reverse();
    println!("{}", data[0]);
    println!("{}", data[..3].into_iter().sum::<usize>());
    Ok(())
}
