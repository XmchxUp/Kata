use std::collections::HashMap;

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_1 {
    left: Vec<u32>,
    right: Vec<u32>,
    right_counter: HashMap<u32, u32>,
}

impl Aoc2023_1 {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Runner for Aoc2023_1 {
    fn info(&self) -> (usize, usize) {
        (2024, 1)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input01.txt");

        for line in inputs {
            let (v1, v2) = line.split_once("   ").unwrap();
            let v1 = v1.parse::<u32>().unwrap();
            let v2 = v2.parse::<u32>().unwrap();
            self.left.push(v1);
            self.right.push(v2);

            if let Some(v) = self.right_counter.get(&v2) {
                self.right_counter.insert(v2, v + 1);
            } else {
                self.right_counter.insert(v2, 1);
            }
        }
    }

    fn part1(&mut self) -> Vec<String> {
        self.left.sort();
        self.right.sort();
        vec![format!(
            "{}",
            self.left
                .iter()
                .zip(&self.right)
                .map(|(&v1, &v2)| v1.abs_diff(v2))
                .sum::<u32>()
        )]
    }

    fn part2(&mut self) -> Vec<String> {
        vec![format!(
            "{}",
            self.left
                .iter()
                .map(|&v| v * self.right_counter.get(&v).unwrap_or(&0))
                .sum::<u32>()
        )]
    }
}
