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
        vec![format!("{}", self.seq.get_score())]
    }

    fn part2(&mut self) -> Vec<String> {
        todo!()
    }
}

#[derive(Default)]
struct Sequence {
    steps: Vec<String>,
}

impl Sequence {
    pub fn get_score(&self) -> usize {
        // + *17 %256
        let mut score = 0;
        for step in &self.steps {
            let mut tmp = 0;
            for c in step.chars() {
                tmp += c as usize;
                tmp *= 17;
                tmp %= 256;
            }
            score += tmp;
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
        assert_eq!(seq.get_score(), 1320);
    }
}
