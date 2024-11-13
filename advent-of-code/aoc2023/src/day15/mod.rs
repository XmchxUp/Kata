use std::collections::HashMap;

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_15 {
    seq: Sequence,
}

impl Aoc2023_15 {
    pub fn new() -> Self {
        Self::default()
    }
}

impl Runner for Aoc2023_15 {
    fn info(&self) -> (usize, usize) {
        (2023, 15)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input_15.txt");
        assert_eq!(inputs.len(), 1);
        self.seq = inputs.get(0).unwrap().clone().into();
    }

    fn part1(&mut self) -> Vec<String> {
        vec![format!("{}", self.seq.get_score_part1())]
    }

    fn part2(&mut self) -> Vec<String> {
        vec![format!("{}", self.seq.get_score_part2())]
    }
}

#[derive(Default)]
struct Sequence {
    steps: Vec<String>,
}

impl Sequence {
    fn hash(&self, step: &String) -> usize {
        // + *17 %256
        let mut res = 0;
        for c in step.chars() {
            res += c as usize;
            res *= 17;
            res %= 256;
        }
        res
    }

    pub fn get_score_part2(&self) -> usize {
        let mut boxes: [HashMap<String, (usize, usize)>; 256] =
            std::array::from_fn(|_| HashMap::new());

        for step in &self.steps {
            if let Some((label_part, _)) = step.split_once('-') {
                let label = label_part.to_string();
                let idx = self.hash(&label);
                if let Some((_, removed_slot)) = boxes[idx].remove(&label) {
                    for value in boxes[idx].values_mut() {
                        if value.1 > removed_slot {
                            value.1 -= 1;
                        }
                    }
                }
            } else if let Some((label_part, lens_part)) = step.split_once('=') {
                let label = label_part.to_string();
                let idx = self.hash(&label);
                let lens: usize = lens_part.parse().expect("Invalid number in step");
                let next_slot = boxes[idx].len() + 1;

                boxes[idx]
                    .entry(label.clone())
                    .and_modify(|value| value.0 = lens)
                    .or_insert_with(|| (lens, next_slot));
            }
        }
        boxes
            .iter()
            .enumerate()
            .map(|(idx, map)| {
                map.iter()
                    .map(|(_, (lens, slot))| (idx + 1) * lens * slot)
                    .sum::<usize>()
            })
            .sum()
    }

    pub fn get_score_part1(&self) -> usize {
        let mut score = 0;
        for step in &self.steps {
            score += self.hash(step);
        }
        score
    }
}

impl From<String> for Sequence {
    fn from(value: String) -> Self {
        let steps = value.split(',').map(|s| s.to_string()).collect();
        Self { steps: steps }
    }
}

#[cfg(test)]

mod tests {
    use super::*;

    #[test]
    fn test_case1() {
        let input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".to_string();
        let seq: Sequence = input.into();
        assert_eq!(seq.get_score_part1(), 1320);
    }

    #[test]
    fn test_case2() {
        let input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".to_string();
        let seq: Sequence = input.into();
        assert_eq!(seq.get_score_part2(), 145);
    }
}
