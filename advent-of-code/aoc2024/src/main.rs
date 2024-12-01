use std::collections::HashMap;

use aoclib::{Runner, Selector};

mod day1;
use day1::*;

fn main() {
    let day1 = Aoc2023_1::new();

    let mut days: HashMap<usize, Box<dyn Runner>> = HashMap::new();
    days.insert(1, Box::new(day1));

    let which = Selector::One(1);

    match which {
        Selector::All => todo!(),
        Selector::One(d) => {
            let day = days.get_mut(&d).unwrap();
            aoclib::run(day.as_mut());
        }
        Selector::Last => todo!(),
    }
}
