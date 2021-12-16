use std::collections::HashMap;

fn slice_to_isize(vec_to_slice: &Vec<char>, from: usize, to: usize) -> isize {
    let as_s: String = vec_to_slice[from..to].iter().collect();
    isize::from_str_radix(&as_s, 2).unwrap()
}

fn slice_and_incr(vec_to_slice: &Vec<char>, i: &mut usize, slice_len: usize) -> isize {
    *i += slice_len;
    slice_to_isize(vec_to_slice, *i - slice_len, *i)
}

pub fn parse_packet(as_binary: &Vec<char>, entry_i: usize, part1: &mut isize) -> (usize, isize) {
    if entry_i + 8 >= as_binary.len() {
        return (entry_i + 8, 0);
    }
    let mut i = entry_i;
    let packet_version = slice_and_incr(&as_binary, &mut i, 3);
    *part1 += packet_version;
    let packet_type = slice_and_incr(&as_binary, &mut i, 3);
    let return_value = if packet_type == 4 {
        let mut total_payload = vec![];
        let mut keep_reading_bit = '1';
        while keep_reading_bit != '0' {
            keep_reading_bit = as_binary[i];
            i += 1;
            total_payload.extend_from_slice(&as_binary[i..i+4]);
            i += 4;
        }
        slice_to_isize(&total_payload, 0, total_payload.len())
    } else {
        let mut packets = vec![];
        let length_type_id = as_binary[i];
        i += 1;
        if length_type_id == '0' {
            let goal = slice_and_incr(&as_binary, &mut i, 15) as usize + i;
            while i < goal {
                let (new_i, packet_val) = parse_packet(&as_binary, i, part1);
                i = new_i;
                packets.push(packet_val);
            }
        } else {
            let number_of_packets = slice_and_incr(&as_binary, &mut i, 11);
            for _ in 0..number_of_packets {
                let (new_i, packet_val) = parse_packet(&as_binary, i, part1);
                i = new_i;
                packets.push(packet_val);
            }
        }
        match packet_type {
            0 =>  packets.iter().sum(),
            1 =>  packets.iter().product(),
            2 => *packets.iter().min().unwrap(),
            3 => *packets.iter().max().unwrap(),
            5 => if packets[0] >  packets[1] {1} else {0},
            6 => if packets[0] <  packets[1] {1} else {0},
            7 => if packets[0] == packets[1] {1} else {0},
            _ => panic!(),
        }
    };
    return (i, return_value);
}

#[aoc_generator(day16)]
pub fn parse_input(input: &str) -> Vec<char>{
    let tuples =
       [('0', "0000"),
        ('1', "0001"),
        ('2', "0010"),
        ('3', "0011"),
        ('4', "0100"),
        ('5', "0101"),
        ('6', "0110"),
        ('7', "0111"),
        ('8', "1000"),
        ('9', "1001"),
        ('A', "1010"),
        ('B', "1011"),
        ('C', "1100"),
        ('D', "1101"),
        ('E', "1110"),
        ('F', "1111")];
    let mut hex_to_bin = HashMap::new();
    for (k, v) in tuples.iter() {
        hex_to_bin.insert(*k, *v);
    }
    let mut as_binary = vec![];
    for e in input.chars() {
        match hex_to_bin.get(&e) {
            Some(bin) => {
                for e in bin.chars() {
                    as_binary.push(e)
                }
            },
            None => panic!(),
        }
    }
    as_binary
}

#[aoc(day16, part1)]
pub fn solve_part1(input: &Vec<char>) -> isize {
    let mut part1 = 0;
    parse_packet(&input, 0, &mut part1);
    part1
}

#[aoc(day16, part2)]
pub fn solve_part2(input: &Vec<char>) -> isize {
    let (_, return_value) = parse_packet(&input, 0, &mut 0);
    return_value
}
