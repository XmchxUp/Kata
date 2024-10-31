use std::collections::{HashMap, HashSet};

use aoclib::{utils::read_file, Runner};

#[derive(Default)]
pub struct Aoc2023_14 {
    grid: Vec<Vec<char>>,
    rows: usize,
    cols: usize,
    states: HashMap<String, usize>,
}

impl Aoc2023_14 {
    pub fn new() -> Self {
        Self::default()
    }

    fn move_cycle(&mut self, cycle: usize) -> bool {
        let state_string = self.grid_to_string();
        let idx = self.states.get(&state_string).or(Some(&0)).unwrap();
        if *idx != 0 {
            if cycle == 1 {
                return true;
            }
            if cycle.is_power_of_two() && idx.is_power_of_two() {
                return true;
            }
        }
        self.states.insert(state_string, cycle);

        self.move_north();
        self.move_west();
        self.move_south();
        self.move_east();
        false
    }

    fn grid_to_string(&self) -> String {
        self.grid
            .iter()
            .map(|row| row.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join(";")
    }

    fn move_east(&mut self) {
        let mut cur_col = (self.cols - 2) as i32;
        while cur_col >= 0 {
            for row in 0..self.rows {
                if self.grid[row][cur_col as usize] == 'O' {
                    let mut pre_col = (cur_col + 1) as usize;
                    while pre_col < self.cols {
                        if self.grid[row][pre_col as usize] == '.' {
                            pre_col += 1;
                        } else {
                            break;
                        }
                    }
                    let new_col = (pre_col - 1) as usize;
                    if new_col != cur_col as usize {
                        self.grid[row][new_col] = 'O';
                        self.grid[row][cur_col as usize] = '.';
                    }
                }
            }
            cur_col -= 1;
        }
    }

    fn move_west(&mut self) {
        let mut cur_col = 1;
        while cur_col < self.cols {
            for row in 0..self.rows {
                if self.grid[row][cur_col] == 'O' {
                    let mut pre_col = (cur_col - 1) as i32;
                    while pre_col >= 0 {
                        if self.grid[row][pre_col as usize] == '.' {
                            pre_col -= 1;
                        } else {
                            break;
                        }
                    }
                    let new_col = (pre_col + 1) as usize;
                    if new_col != cur_col {
                        self.grid[row][new_col] = 'O';
                        self.grid[row][cur_col] = '.';
                    }
                }
            }
            cur_col += 1;
        }
    }

    fn move_south(&mut self) {
        let mut cur_row = (self.rows - 2) as i32;
        while cur_row >= 0 {
            for col in 0..self.cols {
                if self.grid[cur_row as usize][col] == 'O' {
                    let mut pre_row = (cur_row + 1) as usize;
                    while pre_row < self.rows {
                        if self.grid[pre_row][col] == '.' {
                            pre_row += 1;
                        } else {
                            break;
                        }
                    }
                    let new_row = (pre_row - 1) as usize;
                    if new_row != cur_row as usize {
                        self.grid[new_row][col] = 'O';
                        self.grid[cur_row as usize][col] = '.';
                    }
                }
            }
            cur_row -= 1;
        }
    }

    fn move_north(&mut self) {
        let mut cur_row = 1;
        while cur_row < self.rows {
            for col in 0..self.cols {
                if self.grid[cur_row][col] == 'O' {
                    let mut pre_row = (cur_row - 1) as i32;
                    while pre_row >= 0 {
                        if self.grid[pre_row as usize][col] == '.' {
                            pre_row -= 1;
                        } else {
                            break;
                        }
                    }
                    let new_row = (pre_row + 1) as usize;
                    if new_row != cur_row {
                        self.grid[new_row][col] = 'O';
                        self.grid[cur_row][col] = '.';
                    }
                }
            }
            cur_row += 1;
        }
    }

    fn get_score(&mut self) -> usize {
        let mut count = 0;

        self.move_north();
        for (i, row) in self.grid.iter().enumerate() {
            count += row
                .iter()
                .map(|c| if *c == 'O' { self.rows - i } else { 0 })
                .sum::<usize>();
        }

        count
    }
}

impl Runner for Aoc2023_14 {
    fn info(&self) -> (usize, usize) {
        (2023, 14)
    }

    fn parse(&mut self) {
        let lines = read_file("./inputs/test_14.txt");
        self.grid = lines.into_iter().map(|s| s.chars().collect()).collect();
        self.rows = self.grid.len();
        assert!(self.rows > 0);
        self.cols = self.grid[0].len();
    }

    fn part1(&mut self) -> Vec<String> {
        self.move_north();
        vec![format!("{}", self.get_score())]
    }

    fn part2(&mut self) -> Vec<String> {
        for i in 0..1000000000 {
            if self.move_cycle(i) {
                println!("found {}", i + 1);
                break;
            }
        }
        vec![format!("{}", self.get_score())]
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {}
}
