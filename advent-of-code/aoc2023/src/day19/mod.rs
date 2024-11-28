use std::collections::HashMap;

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_19 {
    workflows: HashMap<String, (Vec<(char, char, i32, String)>, String)>,
    values: Vec<HashMap<char, i32>>,
}

impl Aoc2023_19 {
    pub fn new() -> Self {
        Self::default()
    }

    fn accept(&self, values: &HashMap<char, i32>, name: &str) -> bool {
        match name {
            "R" => false,
            "A" => true,

            _ => {
                let (rules, fallback) = &self.workflows[name];
                for (var, cmp, n, target) in rules {
                    match cmp {
                        '<' => {
                            if values[var] < *n {
                                return self.accept(values, target);
                            }
                        }
                        '>' => {
                            if values[var] > *n {
                                return self.accept(values, target);
                            }
                        }
                        _ => {
                            continue;
                        }
                    }
                }
                self.accept(values, fallback)
            }
        }
    }

    fn count(&self, ranges: HashMap<char, (i32, i32)>, name: &str) -> u64 {
        match name {
            "R" => 0,
            "A" => {
                let mut product = 1;
                for (lo, hi) in ranges.values() {
                    product *= (hi - lo + 1) as u64;
                }
                product
            }
            _ => {
                let (rules, fallback) = &self.workflows[name];
                let mut total = 0;
                let mut need_fallback = true;
                let mut curret_ranges = ranges;

                for (key, cmp, n, target) in rules {
                    let (lo, hi) = curret_ranges.get(key).unwrap();
                    let mut true_range = (0, 0);
                    let mut false_range = (0, 0);
                    if *cmp == '<' {
                        true_range = (*lo, *n - 1);
                        false_range = (*n, *hi);
                    } else if *cmp == '>' {
                        true_range = (*n + 1, *hi);
                        false_range = (*lo, *n);
                    } else {
                        panic!("error operator");
                    }

                    if true_range.0 <= true_range.1 {
                        let mut copy = curret_ranges.clone();
                        copy.insert(*key, true_range);
                        total += self.count(copy, target);
                    }

                    if false_range.0 <= false_range.1 {
                        // 更新当前ranges为false_range
                        let mut copy = curret_ranges.clone();
                        copy.insert(*key, false_range);
                        curret_ranges = copy;
                    } else {
                        //如果都没有match则走fallback
                        need_fallback = false;
                        break;
                    }
                }
                if need_fallback {
                    total += self.count(curret_ranges, fallback)
                }
                total
            }
        }
    }
}

impl Runner for Aoc2023_19 {
    fn info(&self) -> (usize, usize) {
        (2023, 19)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input_19.txt");
        let mut parse_value = false;
        for input in inputs {
            if input.is_empty() {
                parse_value = true;
                continue;
            }

            if parse_value {
                let mut m = HashMap::new();
                let tmp: Vec<&str> = input[1..input.len() - 1].split(',').collect();
                for e in tmp {
                    let p = e.split_once('=').unwrap();
                    m.insert(p.0.chars().next().unwrap(), p.1.parse::<i32>().unwrap());
                }
                self.values.push(m);
            } else {
                let parts = input.split_once('{').unwrap();
                let name = parts.0.to_string();
                let parts: Vec<&str> = parts.1[..parts.1.len() - 1].split(',').collect();
                let fallback = parts.last().unwrap();

                let mut rules = Vec::new();
                for part in parts.iter().take(parts.len() - 1) {
                    let (tmp, target) = part.split_once(':').unwrap();
                    let val: i32 = tmp[2..].parse().unwrap();
                    let mut tmp = tmp.chars();
                    rules.push((
                        tmp.next().unwrap(),
                        tmp.next().unwrap(),
                        val,
                        target.to_string(),
                    ));
                }

                self.workflows.insert(name, (rules, fallback.to_string()));
            }
        }
        // println!("{:?}", self.values);
        // println!("{:?}", self.workflows);
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!(
            "{}",
            self.values
                .iter()
                .map(|value| if self.accept(value, "in") {
                    value.values().sum()
                } else {
                    0
                })
                .sum::<i32>()
        )]
    }

    fn part2(&mut self) -> Vec<String> {
        let mut ranges = HashMap::new();
        for ch in "xmas".chars() {
            ranges.insert(ch, (1, 4000));
        }
        vec![format!("{}", self.count(ranges, "in"))]
    }
}
