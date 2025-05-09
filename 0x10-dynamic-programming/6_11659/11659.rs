use std::io;
use std::str::SplitWhitespace;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let mut iter = input.split_whitespace();
    let n: usize = iter.next().unwrap().parse().unwrap();
    let m: usize = iter.next().unwrap().parse().unwrap();

    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let nums: Vec<i32> = input
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    println!("{:?}", nums);

    let mut prefix_sum: Vec<i32> = vec![0; n + 1];
    prefix_sum[1] = nums[0];

    for i in 1..n {
        prefix_sum[i + 1] = prefix_sum[i] + nums[i];
    }

    println!("{:?}", prefix_sum);

    for _ in 0..m {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let mut iter = input.split_whitespace();
        let start: usize = iter.next().unwrap().parse().unwrap();
        let end: usize = iter.next().unwrap().parse().unwrap();
        println!("{}", prefix_sum[end] - prefix_sum[start - 1]);
    }
}