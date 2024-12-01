use std::collections::HashMap;

use aoclib::{Runner, Selector};

mod day12;
use day12::*;
mod day13;
use day13::*;
mod day14;
use day14::*;
mod day15;
use day15::*;
mod day16;
use day16::*;
mod day17;
use day17::*;
mod day18;
use day18::*;
mod day19;
use day19::*;
mod day20;
use day20::*;
mod day21;
use day21::*;
mod day22;
use day22::*;
mod day23;
use day23::*;
mod day24;
use day24::*;
mod day25;
use day25::*;

fn main() {
    let day12 = Aoc2023_12::new();
    let day13 = Aoc2023_13::new();
    let day14 = Aoc2023_14::new();
    let day15 = Aoc2023_15::new();
    let day16 = Aoc2023_16::new();
    let day17 = Aoc2023_17::new();
    let day18 = Aoc2023_18::new();
    let day19 = Aoc2023_19::new();
    let day20 = Aoc2023_20::new();
    let day21 = Aoc2023_21::new();
    let day22 = Aoc2023_22::new();
    let day22 = Aoc2023_22::new();
    let mut days: HashMap<usize, Box<dyn Runner>> = HashMap::new();
    days.insert(12, Box::new(day12));
    days.insert(13, Box::new(day13));
    days.insert(14, Box::new(day14));
    days.insert(15, Box::new(day15));
    days.insert(16, Box::new(day16));
    days.insert(17, Box::new(day17));
    days.insert(18, Box::new(day18));
    days.insert(19, Box::new(day19));
    days.insert(20, Box::new(day20));

    let which = Selector::One(20);

    match which {
        Selector::All => todo!(),
        Selector::One(d) => {
            let day = days.get_mut(&d).unwrap();
            aoclib::run(day.as_mut());
        }
        Selector::Last => todo!(),
    }
}
