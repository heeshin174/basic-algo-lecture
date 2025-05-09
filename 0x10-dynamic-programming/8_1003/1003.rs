use std::io;

fn main() {
    let mut input = String::new();
    // 테스트 케이스의 개수를 읽습니다.
    io::stdin().read_line(&mut input).expect("입력을 읽지 못했습니다.");
    let t: usize = input.trim().parse().expect("유효하지 않은 입력입니다.");

    // dp 테이블을 선언합니다. n이 40까지 가능하므로 크기를 41로 설정합니다.
    // 각 요소는 [fib(0) 호출 횟수, fib(1) 호출 횟수]를 저장합니다.
    let mut dp: [[i32; 2]; 41] = [[0, 0]; 41];

    dp[0] = [1, 0];
    dp[1] = [0, 1];

    // 2부터 40까지 dp 테이블을 채웁니다.
    // fib(i)의 호출 횟수는 fib(i-1)과 fib(i-2) 호출 횟수의 합입니다.
    for i in 2..41 {
        dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
        dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
    }

    // 각 테스트 케이스에 대해 n을 읽고 결과를 출력합니다.
    for _ in 0..t {
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("입력을 읽지 못했습니다.");
        let n: usize = input.trim().parse().expect("유효하지 않은 입력입니다.");

        println!("{} {}", dp[n][0], dp[n][1]);
    }
}
