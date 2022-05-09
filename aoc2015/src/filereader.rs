use std::fs::File;
use std::io::{BufReader, BufRead};

pub fn read_lines_from_file(filename: String) -> Vec<String>  {
    // read file from path
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);

    reader.lines().flatten().collect()
}