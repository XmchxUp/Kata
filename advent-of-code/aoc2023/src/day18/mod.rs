use std::collections::HashMap;

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_18 {
    inputs: Vec<String>,
}

impl Aoc2023_18 {
    pub fn new() -> Self {
        Self::default()
    }

    fn solve(&mut self, part1: bool) -> i64 {
        let mut dirs = HashMap::new();
        dirs.insert("U", (-1, 0));
        dirs.insert("D", (1, 0));
        dirs.insert("L", (0, -1));
        dirs.insert("R", (0, 1));

        let mut points: Vec<(i64, i64)> = vec![(0, 0)];
        let mut b = 0;
        for line in &self.inputs {
            let mut parts = line.split_whitespace();
            let dir = parts.next().unwrap();
            let n = parts.next().unwrap();
            let mut n = n.parse::<i64>().unwrap();
            let mut hex = parts.next().unwrap();
            hex = &hex[2..hex.len() - 1];

            let (dr, dc) = if part1 {
                dirs[dir]
            } else {
                let a = hex.chars().last().unwrap();
                let dir = match a {
                    '0' => "R",
                    '1' => "D",
                    '2' => "L",
                    '3' => "U",
                    _ => panic!("error direction"),
                };
                let tmp = &hex[..hex.len() - 1];
                n = u64::from_str_radix(tmp, 16).unwrap() as i64;
                dirs[dir]
            };
            b += n;
            let (r, c) = points.last().unwrap();
            points.push((r + dr * n, c + dc * n));
        }

        let len = points.len();
        let mut area = 0;
        for i in 0..len - 1 {
            let (x1, y1) = points[i];
            let (x2, y2) = points[i + 1];
            area += x1 * y2 - y1 * x2;
        }
        area = area.abs() / 2;

        let i = area - b / 2 + 1;
        i + b
    }
}

impl Runner for Aoc2023_18 {
    fn info(&self) -> (usize, usize) {
        (2023, 18)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input_18.txt");
        self.inputs = inputs;
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!("{}", self.solve(true))]
    }

    fn part2(&mut self) -> Vec<String> {
        vec![format!("{}", self.solve(false))]
    }
}
