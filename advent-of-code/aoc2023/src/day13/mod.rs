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
                if let Ok(v) = (&tmp).try_into() {
                    self.patterns.push(v);
                }
                tmp.clear();
                continue;
            }
            tmp.push(line);
        }

        if !tmp.is_empty() {
            if let Ok(v) = (&tmp).try_into() {
                self.patterns.push(v);
            }
        }
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!("{:?}", self.patterns)]
    }

    fn part2(&mut self) -> Vec<String> {
        todo!()
    }
}

#[derive(Debug)]
struct Pattern {
    rows: usize,
    cols: usize,
    is_hor_reflect: bool,
    mirror_idx: usize,
}

impl TryFrom<&Vec<&String>> for Pattern {
    type Error = String;

    fn try_from(value: &Vec<&String>) -> Result<Self, Self::Error> {
        let rows = value.len();
        let cols = value.get(0).unwrap().len();
        let mut is_hor_reflect = false;

        //  check horizontal
        let mut mirror_idx = rows;
        for r in 1..rows / 2 + 1 {
            let nr = r + 1;
            if value[r] != value[nr] {
                continue;
            }
            let mut i = r - 1;
            let mut j = nr + 1;
            while i != 0 && j < rows {
                if value[i] != value[j] {
                    break;
                }
                i -= 1;
                j += 1;
            }
            if i == 0 && j == rows {
                is_hor_reflect = true;
                mirror_idx = r;
                break;
            }
        }

        if !is_hor_reflect {
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

            for c in 1..cols / 2 + 1 {
                let nc = c + 1;
                if columns[c] != columns[nc] {
                    continue;
                }

                let mut i = c - 1;
                let mut j = nc + 1;
                while i != 0 && j < cols {
                    if columns[i] != columns[j] {
                        break;
                    }
                    i -= 1;
                    j += 1;
                }
                if i == 0 && j == cols {
                    is_hor_reflect = false;
                    mirror_idx = c;
                    break;
                }
            }
        }

        if mirror_idx == rows {
            return Err("not found mirror".to_string());
            // println!("{:?}", value);
        }
        // assert_ne!(mirror_idx, rows, "not found mirror");

        Ok(Pattern {
            rows,
            cols,
            is_hor_reflect,
            mirror_idx,
        })
    }
}
