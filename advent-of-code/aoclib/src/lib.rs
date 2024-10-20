use std::time::{Duration, Instant};

pub mod utils;

pub trait Runner {
    fn info(&self) -> (usize, usize);
    fn parse(&mut self);
    fn part1(&mut self) -> Vec<String>;
    fn part2(&mut self) -> Vec<String>;
}

pub enum Selector {
    All,
    One(usize),
    Last,
}

pub fn run(runner: &mut dyn Runner) {
    let name = runner.info();
    println!("---- {}, Day {} ----", name.0, name.1);

    let start = Instant::now();
    runner.parse();
    let parse_time = start.elapsed().as_millis();
    println!("{:3}.{:03} Parsing", parse_time / 1000, parse_time % 1000);

    let start = Instant::now();
    let p1 = runner.part1();
    let p1_time = start.elapsed();
    print_sol(1, &p1, p1_time);

    let start = Instant::now();
    let p2 = runner.part2();
    let p2_time = start.elapsed();
    print_sol(2, &p2, p2_time);
}

fn print_sol(part: usize, output: &[String], duration: Duration) {
    let ms = duration.as_millis();
    let sec_part = ms / 1000;
    let ms_part = ms % 1000;

    let mut i = output.iter();
    println!(
        "{sec_part:3}.{ms_part:03} Part {part}: {}",
        i.next().unwrap()
    );
    for line in i {
        println!("{:16}{line}", "");
    }
}
