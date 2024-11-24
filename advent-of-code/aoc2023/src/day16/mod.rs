use std::collections::{HashSet, VecDeque};

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_16 {
    map: Vec<Vec<char>>,
}

impl Aoc2023_16 {
    pub fn new() -> Self {
        Self::default()
    }

    fn solve(&mut self, start: (i32, i32, i32, i32)) -> usize {
        // [(r, c, dr, dc)]
        let mut q: VecDeque<(i32, i32, i32, i32)> = VecDeque::new();
        // start top left
        // q.push_back((0, -1, 0, 1));
        q.push_back(start);

        let mut seen = HashSet::new();
        while !q.is_empty() {
            let (mut r, mut c, dr, dc) = q.pop_front().unwrap();
            r += dr;
            c += dc;

            if r < 0 || r >= self.map.len() as i32 || c < 0 || c >= self.map[0].len() as i32 {
                continue;
            }

            let ch = self.map[r as usize][c as usize];

            if ch == '.' || (ch == '-' && dc != 0) || (ch == '|' && dr != 0) {
                let ele = (r, c, dr, dc);
                if !seen.contains(&ele) {
                    seen.insert(ele);
                    q.push_back(ele);
                }
            } else if ch == '/' {
                let tmp = dr;
                let dr = -dc;
                let dc = -tmp;

                let ele = (r, c, dr, dc);
                if !seen.contains(&ele) {
                    seen.insert(ele);
                    q.push_back(ele);
                }
            } else if ch == '\\' {
                let tmp = dr;
                let dr = dc;
                let dc = tmp;

                let ele = (r, c, dr, dc);
                if !seen.contains(&ele) {
                    seen.insert(ele);
                    q.push_back(ele);
                }
            } else {
                let dirs = if ch == '|' {
                    vec![(1, 0), (-1, 0)]
                } else {
                    vec![(0, 1), (0, -1)]
                };
                for (dr, dc) in dirs {
                    let ele = (r, c, dr, dc);
                    if !seen.contains(&ele) {
                        seen.insert(ele);
                        q.push_back(ele);
                    }
                }
            }
        }

        let coords: HashSet<(i32, i32)> = seen.iter().map(|(r, c, _, _)| (*r, *c)).collect();
        // for r in 0..=self.map.len() {
        //     for c in 0..=self.map[0].len() {
        //         if coords.contains(&(r as i32, c as i32)) {
        //             print!("#");
        //         } else {
        //             print!(".");
        //         }
        //     }
        //     println!();
        // }
        coords.len()
    }
}

impl Runner for Aoc2023_16 {
    fn info(&self) -> (usize, usize) {
        (2023, 16)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input_16.txt");
        self.map = inputs.iter().map(|s| s.chars().collect()).collect();
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!("{}", self.solve((0, -1, 0, 1)))]
    }

    fn part2(&mut self) -> Vec<String> {
        let mut res = 0;

        for r in 0..=self.map.len() {
            res = res.max(self.solve((r as i32, -1, 0, 1)));
            res = res.max(self.solve((r as i32, (self.map[0].len() - 1) as i32, 0, -1)));
        }

        for c in 0..=self.map.len() {
            res = res.max(self.solve((-1, c as i32, 1, 0)));
            res = res.max(self.solve(((self.map.len() - 1) as i32, c as i32, -1, 0)));
        }
        vec![format!("{}", res)]
    }
}
