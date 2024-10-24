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
            self.patterns.iter().map(|p| p.score).sum::<usize>()
        )]
    }

    fn part2(&mut self) -> Vec<String> {
        todo!()
    }
}

#[derive(Debug)]
struct Pattern {
    pub score: usize,
}

impl From<&Vec<String>> for Pattern {
    fn from(value: &Vec<String>) -> Self {
        let mut score = 0;
        let rows = value.len();
        let cols = value.get(0).unwrap().len();

        //  check horizontal
        for r in 1..rows {
            if value[r] != value[r - 1] {
                continue;
            }

            let mut i = (r - 1) as i32;
            let mut j = r;
            let mut found = true;
            while i >= 0 && j < rows {
                if value[i as usize] != value[j] {
                    found = false;
                    break;
                }
                i -= 1;
                j += 1;
            }

            if found {
                score += 100 * r;
                break;
            }
        }

        // check verctial
        let columns: Vec<Vec<char>> = (0..cols)
            .into_iter()
            .map(|c| {
                value
                    .iter()
                    .map(|row| row.chars().nth(c).unwrap())
                    .collect()
            })
            .collect();

        for c in 1..cols {
            if columns[c] != columns[c - 1] {
                continue;
            }

            let mut i = (c - 1) as i32;
            let mut j = c;
            let mut found = true;
            while i >= 0 && j < cols {
                if columns[i as usize] != columns[j] {
                    found = false;
                    break;
                }
                i -= 1;
                j += 1;
            }

            if found {
                score += c;
                break;
            }
        }

        Pattern { score }
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
        let pattern: Pattern = (&input).try_into().unwrap();
        assert_eq!(pattern.score, 5);
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
        let pattern: Pattern = (&input).try_into().unwrap();
        assert_eq!(pattern.score, 400);
    }
}
