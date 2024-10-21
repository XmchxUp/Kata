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
        let lines = aoclib::utils::read_file("./inputs/test_13.txt");

        let mut tmp = vec![];
        for line in lines.iter() {
            if line.trim().is_empty() {
                self.patterns.push((&tmp).into());
                tmp.clear();
                continue;
            }
            tmp.push(line);
        }

        if !tmp.is_empty() {
            self.patterns.push((&tmp).into());
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

impl From<&Vec<&String>> for Pattern {
    fn from(value: &Vec<&String>) -> Self {
        let rows = value.len();
        let cols = value.get(0).unwrap().len();
        let mut is_hor_reflect = false;

        //  check horizontal
        let mut mirror_idx = rows;
        for r in 0..rows - 1 {
            let cur_line = value.get(r).unwrap();
            assert_eq!(cols, cur_line.len());
            for nr in r + 1..rows {
                if cur_line == value.get(nr).unwrap() {
                    mirror_idx = r;
                    break;
                }
            }
            if mirror_idx != rows {
                is_hor_reflect = true;
                break;
            }
        }

        if !is_hor_reflect {
            // check verctial
            for c in 0..cols - 1 {
                let mut cur_line = String::new();
                for r in 0..rows {
                    let tmp = value.get(r).unwrap();
                    cur_line.push(tmp.chars().nth(c).unwrap());
                }

                for nc in c..cols {
                    let mut tmp_line = String::new();
                    for r in 0..rows {
                        let tmp = value.get(r).unwrap();
                        tmp_line.push(tmp.chars().nth(nc).unwrap());
                    }

                    if tmp_line == cur_line {
                        mirror_idx = c;
                        break;
                    }
                }
                if mirror_idx != rows {
                    break;
                }
            }
        }

        assert_ne!(mirror_idx, rows);

        Pattern {
            rows,
            cols,
            is_hor_reflect,
            mirror_idx,
        }
    }
}
