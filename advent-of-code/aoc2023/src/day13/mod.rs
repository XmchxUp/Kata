use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_13 {
    patterns: Vec<Pattern>,
}

impl Aoc2023_13 {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Runner for Aoc2023_13 {
    fn info(&self) -> (usize, usize) {
        (2023, 13)
    }

    fn parse(&mut self) {
        let lines = aoclib::utils::read_file("./inputs/input_13.txt");

        let mut tmp = vec![];
        for line in lines.iter() {
            if line.trim().is_empty() {
                self.patterns.push((&tmp).into());
                tmp.clear();
                continue;
            }
            tmp.push(line.clone());
        }

        if !tmp.is_empty() {
            self.patterns.push((&tmp).into());
        }
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!(
            "{}",
            self.patterns.iter().map(|p| p.score1).sum::<usize>()
        )]
    }

    fn part2(&mut self) -> Vec<String> {
        vec![format!(
            "{}",
            self.patterns.iter().map(|p| p.score2).sum::<usize>()
        )]
    }
}

#[derive(Debug)]
struct Pattern {
    pub score1: usize,
    pub score2: usize,
}
impl Pattern {
    fn find_mirror(grid: &[String], allow_one_difference: bool) -> usize {
        for x in 1..grid.len() {
            let above: Vec<&String> = grid[..x].iter().rev().collect();
            let below: Vec<&String> = grid[x..].iter().collect();

            let min_len = std::cmp::min(above.len(), below.len());
            let above = &above[..min_len];
            let below = &below[..min_len];

            if !allow_one_difference {
                if above == below {
                    return x;
                }
            } else {
                let diff_count: usize = above
                    .iter()
                    .zip(below.iter())
                    .map(|(a_row, b_row)| {
                        a_row
                            .chars()
                            .zip(b_row.chars())
                            .filter(|(a, b)| a != b)
                            .count()
                    })
                    .sum();
                if diff_count == 1 {
                    return x;
                }
            }
        }
        0
    }

    fn transpose(grid: &[String]) -> Vec<String> {
        let cols = grid[0].len();
        let rows = grid.len();
        let mut res: Vec<String> = vec![String::with_capacity(rows); cols];

        for row in grid {
            for (i, ch) in row.chars().enumerate() {
                res[i].push(ch);
            }
        }

        res
    }
}

impl From<&Vec<String>> for Pattern {
    fn from(grid: &Vec<String>) -> Self {
        let mut score1 = 0;
        let row = Self::find_mirror(grid, false);
        score1 += row * 100;
        let cols = Self::transpose(grid);
        let col = Self::find_mirror(&cols, false);
        score1 += col;

        let mut score2 = 0;
        let row = Self::find_mirror(grid, true);
        score2 += row * 100;
        let col = Self::find_mirror(&cols, true);
        score2 += col;

        // part1
        // //  check horizontal
        // for r in 1..rows {
        //     if grid[r] != grid[r - 1] {
        //         continue;
        //     }

        //     let mut i = (r - 1) as i32;
        //     let mut j = r;
        //     let mut found = true;
        //     while i >= 0 && j < rows {
        //         if grid[i as usize] != grid[j] {
        //             found = false;
        //             break;
        //         }
        //         i -= 1;
        //         j += 1;
        //     }

        //     if found {
        //         score += 100 * r;
        //         break;
        //     }
        // }

        // // check verctial
        // let columns: Vec<Vec<char>> = (0..cols)
        //     .map(|c| {
        //         grid
        //             .iter()
        //             .map(|row| row.chars().nth(c).unwrap())
        //             .collect()
        //     })
        //     .collect();

        // for c in 1..cols {
        //     if columns[c] != columns[c - 1] {
        //         continue;
        //     }

        //     let mut i = (c - 1) as i32;
        //     let mut j = c;
        //     let mut found = true;
        //     while i >= 0 && j < cols {
        //         if columns[i as usize] != columns[j] {
        //             found = false;
        //             break;
        //         }
        //         i -= 1;
        //         j += 1;
        //     }

        //     if found {
        //         score += c;
        //         break;
        //     }
        // }

        Pattern { score1, score2 }
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_1() {
        let input: Vec<String> = vec![
            "#.##..##.".to_string(),
            "..#.##.#.".to_string(),
            "##......#".to_string(),
            "##......#".to_string(),
            "..#.##.#.".to_string(),
            "..##..##.".to_string(),
            "#.#.##.#.".to_string(),
        ];
        let pattern: Pattern = (&input).into();
        assert_eq!(pattern.score1, 5);
    }

    #[test]
    fn test_2() {
        let input: Vec<String> = vec![
            "#...##..#".to_string(),
            "#....#..#".to_string(),
            "..##..###".to_string(),
            "#####.##.".to_string(),
            "#####.##.".to_string(),
            "..##..###".to_string(),
            "#....#..#".to_string(),
        ];
        let pattern: Pattern = (&input).into();
        assert_eq!(pattern.score1, 400);
    }
}
