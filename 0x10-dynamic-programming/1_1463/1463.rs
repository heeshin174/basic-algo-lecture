use std::io; // For reading input
use std::cmp::min; // For the min function

fn main() {
    // 1. Handle Input
    // Declare a mutable string to hold the input line
    let mut input = String::new();

    // Read a line from standard input into the 'input' string
    // .expect() is a simple way to handle potential errors - if reading fails,
    // the program will panic with the given message.
    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    // Trim whitespace from the input string and parse it as an unsigned integer (usize)
    // usize is a good type for sizes and indices.
    // .expect() is used again to handle potential parsing errors (e.g., if the input isn't a number)
    let n: usize = input.trim().parse()
        .expect("Invalid input");

    // 2. Choose and Initialize Data Structure
    // Create a mutable vector 'dp' of unsigned integers (usize)
    // It has size n + 1. We use n+1 size so that dp[i] corresponds to the number i.
    // All elements are initially set to 0. We'll overwrite these shortly.
    let mut dp: Vec<usize> = vec![0; n + 1];

    // 3. Implement the Base Case
    // The base case is n=1, which requires 0 operations.
    // We only set this if n is at least 1 (which it must be for the logic to work).
    if n >= 1 {
        dp[1] = 0;
    }
    // Note: dp[0] remains 0 but is unused by the problem logic (we start from 1).

    // 4. Implement the Loop
    // Iterate from i = 2 up to n *inclusive*. The `..=` creates an inclusive range.
    for i in 2..=n {
        // The first possibility is always subtracting 1 from the previous number.
        // The cost is 1 operation (subtracting 1) + the minimum operations needed for i-1.
        dp[i] = dp[i - 1] + 1;

        // Check the other possibilities and update dp[i] if they are better.

        // If i is divisible by 2:
        if i % 2 == 0 {
            // The cost is 1 operation (dividing by 2) + the minimum operations for i / 2.
            // Use std::cmp::min to find the minimum between the current dp[i] and this new possibility.
            dp[i] = min(dp[i], dp[i / 2] + 1);
        }

        // If i is divisible by 3:
        if i % 3 == 0 {
            // The cost is 1 operation (dividing by 3) + the minimum operations for i / 3.
            // Again, take the minimum.
            dp[i] = min(dp[i], dp[i / 3] + 1);
        }
    }

    // 5. Output the Result
    // Print the calculated minimum operations for the input number n, which is stored at dp[n].
    println!("{}", dp[n]);
}