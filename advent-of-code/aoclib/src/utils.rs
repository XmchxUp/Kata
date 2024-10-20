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
