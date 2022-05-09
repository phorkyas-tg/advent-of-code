#[path = "filereader.rs"] mod filereader;

pub fn day_two() {
    let lines = filereader::read_lines_from_file("./data/day2.txt".to_string());

    let mut complete_area = 0;
    let mut ribbon_length = 0;

    for line in lines {
        let mut dimensions: Vec<i32> = 
            line.split('x')
            .map(str::trim)
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect(); 

        dimensions.sort();

        let a = 2 * dimensions[0] * dimensions[1];
        let b = 2 * dimensions[1] * dimensions[2];
        let c = 2 * dimensions[2] * dimensions[0];

        let min_area = [a, b, c].iter().min().unwrap() / 2;

        complete_area += a + b + c + min_area;

        ribbon_length += (2 * dimensions[0]) + (2 * dimensions[1]) + 
                         (dimensions[0] * dimensions[1] * dimensions[2]);
    }

    assert!(complete_area == 1606483);
    assert!(ribbon_length == 3842356);

    println!("day two - part one: {}\nday two - part two: {}", complete_area, ribbon_length);
}