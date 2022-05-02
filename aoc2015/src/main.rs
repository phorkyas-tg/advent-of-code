use std::fs;
use std::path::Path;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() -> std::io::Result<()> {
    day_one();
    day_two()?;

    Ok(())
}

fn day_two() -> std::io::Result<()>  {
    // read file from path
    let file = File::open("./data/day2.txt")?;
    let reader = BufReader::new(file);

    let lines: Vec<_> = reader
        .lines()
        .flatten()
        .collect();
    
    let mut complete_area = 0;
    for line in lines {
        let dimensions: Vec<i32> = 
            line.split('x')
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect(); 


        let a = 2 * dimensions[0] * dimensions[1];
        let b = 2 * dimensions[1] * dimensions[2];
        let c = 2 * dimensions[2] * dimensions[0];

        let min_area = [a, b, c].iter().min().unwrap() / 2;

        complete_area += a + b + c + min_area;
    }

    println!("day two - part one: {}\nday two - part two: {}", complete_area, "TODO");
    Ok(())
}

fn day_one() {
    // read file from path
    let filename = Path::new("./data/day1.txt");
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut floor = 0;
    let mut basement_floor = 0;

    for (i, c) in contents.chars().enumerate() {
        if c == '(' { floor += 1; }
        if c == ')' { floor -= 1; }

        if basement_floor == 0 && floor == -1 {basement_floor = i + 1}
    }

    println!("day one - part one: {}\nday one - part two: {}", floor, basement_floor);
}
