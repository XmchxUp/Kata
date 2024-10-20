use chrono::Datelike;
use std::{collections::HashMap, env, process::exit, time::Instant};

mod day12;

fn main() {
    let mut days: HashMap<usize, fn()> = HashMap::new();
    days.insert(12, day12::day12);

    let args: Vec<String> = env::args().collect();
    let today = chrono::Local::now();

    let mut which_day = today.day() as usize - 1;
    if args.len() != 2 {
        println!("./aoc2023 which_day");
        exit(-1);
    } else if let Ok(day) = args[1].parse::<usize>() {
        which_day = day;
    }

    let now = Instant::now();
    (days.get(&which_day).unwrap())();
    let elasped = now.elapsed();
    println!(
        "-- Completion time: {:6.2}ms",
        elasped.as_micros() as f64 / 1000.
    )
}
