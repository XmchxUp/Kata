use std::{
    fs::File,
    io::{BufRead, BufReader},
};

pub fn read_file(filename: &str) -> Vec<String> {
    let file = File::open(filename).expect("cannot open file");

    BufReader::new(file)
        .lines()
        .map(|line| line.unwrap())
        .collect()
}

pub fn gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

pub fn lcm(a: u64, b: u64) -> u64 {
    (a * b) / gcd(a, b)
}
