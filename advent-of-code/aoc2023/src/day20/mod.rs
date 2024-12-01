use std::collections::{HashMap, VecDeque};

use aoclib::Runner;

#[derive(Default)]
pub struct Aoc2023_20 {
    modules: HashMap<String, Module>,
    broadcast_targets: Vec<String>,
}

impl Aoc2023_20 {
    pub fn new() -> Self {
        Self::default()
    }

    fn init_conj_module(&mut self) {
        // init conjunction module memory
        let mut updates = Vec::new();
        for (name, module) in &self.modules {
            for output in &module.outputs {
                if let Some(output_module) = self.modules.get(output) {
                    match output_module.typ {
                        ModuleType::Conjunction => updates.push((output.clone(), name.clone())),
                        ModuleType::FlipFlop => continue,
                    }
                }
            }
        }
        for (output, name) in updates {
            if let Some(output_module) = self.modules.get_mut(&output) {
                output_module.memory.insert(name, Pluse::Low);
            }
        }
    }
}

impl Runner for Aoc2023_20 {
    fn info(&self) -> (usize, usize) {
        (2023, 20)
    }

    fn parse(&mut self) {
        let inputs = aoclib::utils::read_file("./inputs/input_20.txt");
        for input in inputs {
            let (left, right) = input.split_once(" -> ").unwrap();

            if left == "broadcaster" {
                let mut targets: Vec<String> = right.split(", ").map(|e| e.to_string()).collect();
                self.broadcast_targets.append(&mut targets);
            } else {
                let typ = &left[0..1];
                let name = &left[1..];

                self.modules.insert(
                    name.to_string(),
                    Module::new(
                        typ.into(),
                        right.split(", ").map(|e| e.to_string()).collect(),
                        name.to_string(),
                    ),
                );
            }
        }

        self.init_conj_module();
    }

    fn part1(&mut self) -> Vec<String> {
        let mut low = 0;
        let mut hi = 0;
        let mut modules = self.modules.clone();

        for _ in 0..1000 {
            low += 1;
            let mut q = VecDeque::new();
            for name in &self.broadcast_targets {
                q.push_back(("broadcaster".to_string(), name.to_string(), Pluse::Low));
            }

            while !q.is_empty() {
                let (origin, target, pluse) = q.pop_front().unwrap();
                match pluse {
                    Pluse::Low => low += 1,
                    Pluse::High => hi += 1,
                }

                if let Some(module) = modules.get_mut(&target) {
                    match module.typ {
                        ModuleType::FlipFlop => match pluse {
                            Pluse::Low => {
                                module.status = match module.status {
                                    Status::On => Status::Off,
                                    Status::Off => Status::On,
                                    Status::None => panic!("error status in FlipFlop"),
                                };

                                let p = match module.status {
                                    Status::On => Pluse::High,
                                    Status::Off => Pluse::Low,
                                    Status::None => panic!("error status in FlipFlop"),
                                };

                                for output in &module.outputs {
                                    q.push_back((module.name.to_string(), output.to_string(), p));
                                }
                            }
                            Pluse::High => continue,
                        },
                        ModuleType::Conjunction => {
                            module.memory.insert(origin, pluse);
                            let p = if module.memory.values().all(|x| *x == Pluse::High) {
                                Pluse::Low
                            } else {
                                Pluse::High
                            };

                            for output in &module.outputs {
                                q.push_back((module.name.to_string(), output.to_string(), p));
                            }
                        }
                    }
                }
            }
        }

        vec![format!("{}", low * hi)]
    }

    fn part2(&mut self) -> Vec<String> {
        let feed = "hb".to_string();

        let mut seen = HashMap::new();
        for (name, module) in &self.modules {
            if module.outputs.contains(&feed) {
                seen.insert(name.clone(), 0);
            }
        }

        let mut cycle_lengths = HashMap::new();
        let mut res = 1;
        let mut end = false;
        let mut presses = 0;

        loop {
            presses += 1;
            let mut q = VecDeque::new();
            for name in &self.broadcast_targets {
                q.push_back(("broadcaster".to_string(), name.to_string(), Pluse::Low));
            }

            while !q.is_empty() {
                let (origin, target, pluse) = q.pop_front().unwrap();

                if let Some(module) = self.modules.get_mut(&target) {
                    if module.name == feed && pluse == Pluse::High {
                        let v = seen.get(&origin).unwrap() + 1;
                        seen.insert(origin.clone(), v);

                        if !cycle_lengths.contains_key(&origin) {
                            cycle_lengths.insert(origin.clone(), presses);
                        } else if presses != v * cycle_lengths.get(&origin).unwrap() {
                            panic!("error");
                        }

                        if seen.values().all(|&x| x != 0) {
                            end = true;
                            for &v in cycle_lengths.values() {
                                res = aoclib::utils::lcm(res, v);
                            }
                            break;
                        }
                    }

                    match module.typ {
                        ModuleType::FlipFlop => match pluse {
                            Pluse::Low => {
                                module.status = match module.status {
                                    Status::On => Status::Off,
                                    Status::Off => Status::On,
                                    Status::None => panic!("error status in FlipFlop"),
                                };

                                let p = match module.status {
                                    Status::On => Pluse::High,
                                    Status::Off => Pluse::Low,
                                    Status::None => panic!("error status in FlipFlop"),
                                };

                                for output in &module.outputs {
                                    q.push_back((module.name.to_string(), output.to_string(), p));
                                }
                            }
                            Pluse::High => continue,
                        },
                        ModuleType::Conjunction => {
                            module.memory.insert(origin, pluse);
                            let p = if module.memory.values().all(|x| *x == Pluse::High) {
                                Pluse::Low
                            } else {
                                Pluse::High
                            };

                            for output in &module.outputs {
                                q.push_back((module.name.to_string(), output.to_string(), p));
                            }
                        }
                    }
                }
            }

            if end {
                break;
            }
        }
        vec![format!("{}", res)]
    }
}

#[derive(Debug, PartialEq, Clone, Copy)]
enum ModuleType {
    FlipFlop,
    Conjunction,
}

impl From<&str> for ModuleType {
    fn from(value: &str) -> Self {
        match value {
            "%" => ModuleType::FlipFlop,
            "&" => ModuleType::Conjunction,
            _ => panic!("unknow module type: {}", value),
        }
    }
}

#[derive(Debug, Clone, Copy)]
enum Status {
    On,
    Off,
    None,
}

#[derive(Debug, PartialEq, Clone, Copy)]
enum Pluse {
    Low,
    High,
}

#[derive(Debug, Clone)]
struct Module {
    typ: ModuleType,
    outputs: Vec<String>,
    status: Status,
    name: String,
    memory: HashMap<String, Pluse>,
}

impl Module {
    pub fn new(typ: ModuleType, outputs: Vec<String>, name: String) -> Self {
        let status = match typ {
            ModuleType::FlipFlop => Status::Off,
            ModuleType::Conjunction => Status::None,
        };
        Self {
            typ,
            outputs,
            name,
            status,
            memory: HashMap::new(),
        }
    }
}
