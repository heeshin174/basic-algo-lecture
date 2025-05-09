use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let n: usize = input.trim().parse().expect("Please enter a valid number");

    let mod_val = 10007;
    let mut d = vec![0; n + 1];

    if n >= 1 {
        d[1] = 1;
    }
    if n >= 2 {
        d[2] = 2;
    }

    for i in 3..=n {
        d[i] = (d[i - 1] + d[i - 2]) % mod_val;
    }

    println!("{}", d[n]);
}