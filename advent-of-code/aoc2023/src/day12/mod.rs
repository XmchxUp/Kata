use std::{collections::HashMap, str::FromStr};

use aoclib::Runner;

type Cache = HashMap<(usize, usize), usize>;

#[derive(Default)]
pub struct Aoc2023_12 {
    springs: Vec<Spring>,
}

impl Aoc2023_12 {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Runner for Aoc2023_12 {
    fn info(&self) -> (usize, usize) {
        (2023, 12)
    }

    fn parse(&mut self) {
        let lines = aoclib::utils::read_file("./inputs/input_12.txt");
        for line in lines.iter() {
            self.springs.push(line.parse().unwrap());
        }
    }

    fn part1(&mut self) -> Vec<String> {
        let a: usize = self.springs.iter().map(Spring::arrangements).sum();
        vec![format!("{}", a)]
    }

    fn part2(&mut self) -> Vec<String> {
        let a: usize = self.springs.iter().map(Spring::part2).sum();
        vec![format!("{}", a)]
    }
}

struct Spring {
    pattern: Vec<char>,
    numbers: Vec<usize>,
}

impl Spring {
    pub fn arrangements(&self) -> usize {
        let mut cache = Cache::new();
        Self::count(&self.pattern, &self.numbers, &mut cache)
    }

    pub fn part2(&self) -> usize {
        let mut pattern = vec![];
        for _ in 0..4 {
            pattern.extend(self.pattern.iter().chain(&['?']));
        }
        pattern.extend(self.pattern.iter());

        let mut numbers = vec![];
        for _ in 0..5 {
            numbers.extend(self.numbers.iter());
        }

        // println!("{:?}", self.pattern);
        let mut cache = Cache::new();
        Self::count(&pattern, &numbers, &mut cache)
    }

    fn count(pattern: &[char], numbers: &[usize], cache: &mut Cache) -> usize {
        if let Some(res) = cache.get(&(pattern.len(), numbers.len())) {
            return *res;
        }

        if numbers.is_empty() {
            return (!pattern.contains(&'#')) as usize;
        }

        let remain_len: usize = numbers.iter().sum();

        if pattern.len() < remain_len {
            return 0;
        }

        let res = match pattern[0] {
            '?' => Self::count(&pattern[1..], numbers, cache) + Self::hash(pattern, numbers, cache),
            '.' => Self::count(&pattern[1..], numbers, cache),
            '#' => Self::hash(pattern, numbers, cache),
            v => panic!("invalid char {v}"),
        };
        cache.insert((pattern.len(), numbers.len()), res);
        res
    }

    //          ???.### 1,1,3
    //          /         \
    // #??.### 1,1,3        .??.### 1,1,3

    fn hash(pattern: &[char], numbers: &[usize], cache: &mut Cache) -> usize {
        if pattern.len() < numbers[0] || pattern[0..numbers[0]].contains(&'.') {
            return 0;
        }

        if pattern.len() == numbers[0] {
            return (numbers.len() == 1) as usize;
        }

        // tail
        if pattern[numbers[0]] == '#' {
            return 0;
        }

        Self::count(&pattern[numbers[0] + 1..], &numbers[1..], cache)
    }
}

impl FromStr for Spring {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let (pattern, numbers) = s.split_once(' ').unwrap();
        let pattern = pattern.chars().collect();
        let numbers = numbers.split(',').map(|v| v.parse().unwrap()).collect();

        Ok(Spring { pattern, numbers })
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test() {
        let s: Spring = "???.### 1,1,3".parse().unwrap();
        assert_eq!(1, s.arrangements());

        let s: Spring = ".??..??...?##. 1,1,3".parse().unwrap();
        assert_eq!(4, s.arrangements());

        let s: Spring = "?#?#?#?#?#?#?#? 1,3,1,6".parse().unwrap();
        assert_eq!(1, s.arrangements());

        let s: Spring = "????.#...#... 4,1,1".parse().unwrap();
        assert_eq!(1, s.arrangements());

        let s: Spring = "????.######..#####. 1,6,5".parse().unwrap();
        assert_eq!(4, s.arrangements());

        let s: Spring = "?###???????? 3,2,1".parse().unwrap();
        assert_eq!(10, s.arrangements());
    }
}
