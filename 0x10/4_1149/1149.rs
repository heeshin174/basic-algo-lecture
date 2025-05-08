use std::io::{self, Read};
use std::cmp::min;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();

    let mut lines = input.lines();
    let n: usize = lines.next().unwrap().parse().unwrap();

    let mut score: Vec<Vec<i32>> = vec![vec![0; 3]; n + 1];
    let mut dp: Vec<Vec<i32>> = vec![vec![0; 3]; n + 1];

    for i in 1..=n {
        let line: Vec<i32> = lines
            .next()
            .unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        score[i][0] = line[0];
        score[i][1] = line[1];
        score[i][2] = line[2];
    }

    dp[1][0] = score[1][0];
    dp[1][1] = score[1][1];
    dp[1][2] = score[1][2];

    for i in 2..=n {
        dp[i][0] = score[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
        dp[i][1] = score[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
        dp[i][2] = score[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
    }

    println!("{}", min(min(dp[n][0], dp[n][1]), dp[n][2]));
}