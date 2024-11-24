use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashSet},
};

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_17 {
    map: Vec<Vec<i32>>,
}

impl Aoc2023_17 {
    pub fn new() -> Self {
        Self::default()
    }

    fn solve(&mut self, part1: bool) -> i32 {
        // (heat loss, r, c, dr, dc, n)
        let mut pq = BinaryHeap::new();
        pq.push(Reverse((0, 0, 0, 0, 0, 0)));

        let mut min_heat_loss = 0;
        let mut seen = HashSet::new();

        while let Some(Reverse((heat_loss, r, c, dr, dc, n))) = pq.pop() {
            let e = (r, c, dr, dc, n);

            let is_end = r == self.map.len() as i32 - 1 && c == self.map[0].len() as i32 - 1;
            if is_end && (part1 || n >= 4) {
                min_heat_loss = heat_loss;
                break;
            }

            if seen.contains(&e) {
                continue;
            }
            seen.insert(e);

            if ((part1 && n < 3) || (!part1 && n < 10)) && (dr, dc) != (0, 0) {
                let nr = r + dr;
                let nc = c + dc;
                if 0 <= nr && nr < self.map.len() as i32 && 0 <= nc && nc < self.map[0].len() as i32
                {
                    pq.push(Reverse((
                        heat_loss + self.map[nr as usize][nc as usize],
                        nr,
                        nc,
                        dr,
                        dc,
                        n + 1,
                    )));
                }
            }
            if part1 || (n >= 4 || (r, c) == (0, 0)) {
                for (ndr, ndc) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
                    if (ndr, ndc) != (dr, dc) && (ndr, ndc) != (-dr, -dc) {
                        let nr = r + ndr;
                        let nc = c + ndc;
                        if 0 <= nr
                            && nr < self.map.len() as i32
                            && 0 <= nc
                            && nc < self.map[0].len() as i32
                        {
                            pq.push(Reverse((
                                heat_loss + self.map[nr as usize][nc as usize],
                                nr,
                                nc,
                                ndr,
                                ndc,
                                1,
                            )));
                        }
                    }
                }
            }
        }

        min_heat_loss
    }
}

impl Runner for Aoc2023_17 {
    fn info(&self) -> (usize, usize) {
        (2023, 17)
    }

    fn parse(&mut self) {
        let input = aoclib::utils::read_file("./inputs/input_17.txt");
        self.map = input
            .iter()
            .map(|s| s.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
            .collect();
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!("{}", self.solve(true))]
    }

    fn part2(&mut self) -> Vec<String> {
        vec![format!("{}", self.solve(false))]
    }
}
