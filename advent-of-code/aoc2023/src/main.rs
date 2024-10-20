mod day12;

use std::collections::HashMap;

use aoclib::{Runner, Selector};
use day12::*;

fn main() {
    let day12 = Aoc2023_12::new();
    let mut days: HashMap<usize, Box<dyn Runner>> = HashMap::new();
    days.insert(12, Box::new(day12));

    let which = Selector::One(12);

    match which {
        Selector::All => todo!(),
        Selector::One(d) => {
            let day = days.get_mut(&d).unwrap();
            aoclib::run(day.as_mut());
        }
        Selector::Last => todo!(),
    }
}
