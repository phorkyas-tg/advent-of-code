#[path = "filereader.rs"] mod filereader;
use std::collections::HashSet;

#[derive(Hash, Eq, PartialEq, Debug)]
struct Coordinates {
    x: i32,
    y: i32,
}

pub fn day_three() {
    let lines = filereader::read_lines_from_file("./data/day3.txt".to_string());

    let mut coordinates = HashSet::new();
    let mut robo_coordinates = HashSet::new();

    let mut current_x = 0;
    let mut current_y = 0; 

    let mut santa_x = 0;
    let mut santa_y = 0;
    let mut robo_x = 0;
    let mut robo_y = 0;

    coordinates.insert(Coordinates { x: current_x, y: current_y });
    robo_coordinates.insert(Coordinates { x: current_x, y: current_y });

    for (i, c) in lines[0].chars().enumerate() {
        let mut dx = 0;
        let mut dy = 0;
        
        if c == '>' { dy += 1; }
        if c == '<' { dy -= 1; }
        if c == 'v' { dx += 1; }
        if c == '^' { dx -= 1; }

        current_x += dx;
        current_y += dy;

        if i % 2 == 0 {
            santa_x += dx;
            santa_y += dy;
        }
        else {
            robo_x += dx;
            robo_y += dy;
        }

        coordinates.insert(Coordinates { x: current_x, y: current_y });
        robo_coordinates.insert(Coordinates { x: santa_x, y: santa_y });
        robo_coordinates.insert(Coordinates { x: robo_x, y: robo_y });
    }

    assert!(coordinates.len() == 2572);
    assert!(robo_coordinates.len() == 2631);

    println!("day three - part one: {}\nday three - part two: {}", 
        coordinates.len(), 
        robo_coordinates.len());
}