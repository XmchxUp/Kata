use std::collections::HashMap;

use aoclib::{Runner, Selector};

mod day12;
use day12::*;
mod day13;
use day13::*;
mod day14;
use day14::*;

fn main() {
    let day12 = Aoc2023_12::new();
    let day13 = Aoc2023_13::new();
    let day14 = Aoc2023_14::new();
    let mut days: HashMap<usize, Box<dyn Runner>> = HashMap::new();
    days.insert(12, Box::new(day12));
    days.insert(13, Box::new(day13));
    days.insert(14, Box::new(day14));

    let which = Selector::One(14);

    match which {
        Selector::All => todo!(),
        Selector::One(d) => {
            let day = days.get_mut(&d).unwrap();
            aoclib::run(day.as_mut());
        }
        Selector::Last => todo!(),
    }
}
