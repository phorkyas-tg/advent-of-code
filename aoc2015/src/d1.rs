#[path = "filereader.rs"] mod filereader;

pub fn day_one() {
    // read file from path
    let lines = filereader::read_lines_from_file("./data/day1.txt".to_string());


    let mut floor = 0;
    let mut basement_floor = 0;

    for (i, c) in lines[0].chars().enumerate() {
        if c == '(' { floor += 1; }
        if c == ')' { floor -= 1; }

        if basement_floor == 0 && floor == -1 {basement_floor = i + 1}
    }

    assert!(floor == 74);
    assert!(basement_floor == 1795);

    println!("day one - part one: {}\nday one - part two: {}", floor, basement_floor);
}