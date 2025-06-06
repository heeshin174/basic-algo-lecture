// 1. 필요한 표준 라이브러리 모듈을 가져옵니다.
use std::io; // 표준 입출력 (콘솔 읽기/쓰기) 기능을 사용하기 위해 필요합니다.

fn main() {
    // 2. 테스트 케이스의 개수 t를 읽습니다.
    // `let mut`은 변수를 선언하고 변경 가능하게 만듭니다.
    // `String::new()`는 새로운 빈 문자열을 생성합니다.
    let mut input = String::new();
    // 표준 입력에서 한 줄을 읽어 `input` 문자열에 저장합니다.
    // `.expect()`는 만약 읽기 작업에서 오류가 발생하면 프로그램을 중단하고 메시지를 출력합니다.
    io::stdin().read_line(&mut input).expect("Failed to read line");

    // 읽은 문자열의 앞뒤 공백(개행문자 포함)을 제거하고 정수(usize 타입)로 변환합니다.
    // usize는 부호 없는 정수 타입으로, 주로 크기나 인덱스에 사용됩니다.
    // `.trim()`은 문자열 슬라이드(&str)를 반환합니다.
    // `.parse()`는 문자열을 다른 타입으로 파싱(변환)하려고 시도합니다. 결과는 Result 타입입니다.
    // `.expect()`는 파싱이 실패하면 프로그램을 중단합니다.
    let t: usize = input.trim().parse().expect("Invalid input for t");

    // 3. DP 테이블을 저장할 벡터를 선언하고 초기화합니다.
    // dp[i]는 숫자 i를 만드는 방법의 수를 저장할 것입니다.
    // 문제의 제약 조건이 1 <= n < 11 이므로, 최대 n은 10입니다.
    // 우리는 dp[10]까지의 결과가 필요하며, 인덱스 10을 사용하려면 최소 크기가 11인 벡터가 필요합니다 (인덱스 0부터 시작하므로).
    // 크기가 11이고 모든 값이 0으로 초기화된 usize 타입의 벡터를 만듭니다.
    let mut dp: Vec<usize> = vec![0; 11]; // 인덱스 0부터 10까지 총 11개의 공간

    // 4. 기저 조건(Base Case)을 설정합니다.
    // Python 코드와 동일하게 직접 계산된 초기 값들을 설정합니다.
    // 인덱스 1은 숫자 1을 의미, 인덱스 2는 숫자 2, 인덱스 3은 숫자 3을 의미합니다.
    dp[1] = 1; // 1을 만드는 방법: {1} - 1가지
    dp[2] = 2; // 2를 만드는 방법: {1,1}, {2} - 2가지
    dp[3] = 4; // 3을 만드는 방법: {1,1,1}, {1,2}, {2,1}, {3} - 4가지

    // 5. 점화식을 사용하여 4부터 10까지 결과를 미리 계산합니다.
    // `for i in 4..=10`는 4부터 10까지 *포함하는* 범위를 반복합니다.
    for i in 4..=10 {
        // 동적 계획법 점화식: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        // 이전(i-1), 두 칸 앞(i-2), 세 칸 앞(i-3)에 저장된 값을 가져와 더합니다.
        // 벡터의 크기를 11로 했고, i는 최소 4부터 시작하므로 i-1, i-2, i-3은 항상 유효한 인덱스(1 이상)입니다.
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }

    // 6. 테스트 케이스 수(t)만큼 반복하여 입력을 받고 결과를 출력합니다.
    // `for _ in 0..t`는 0부터 t-1까지 t번 반복하되, 루프 변수(_)는 사용하지 않겠다는 의미입니다.
    for _ in 0..t {
        // 다음 n 값을 읽기 전에 이전에 사용했던 input 문자열을 비웁니다.
        input.clear();
        // n 값을 다시 읽습니다. 위에서 t를 읽을 때와 동일한 과정입니다.
        io::stdin().read_line(&mut input).expect("Failed to read line");
        let n: usize = input.trim().parse().expect("Invalid input for n");

        // 7. 미리 계산해 둔 dp 테이블에서 n에 해당하는 결과를 찾아 출력합니다.
        // `println!` 매크로는 콘솔에 출력하며, `{}`는 변수 값이 들어갈 자리입니다.
        // `dp[n]`은 숫자 n을 만드는 방법의 수이며, 1 <= n < 11 이므로 n은 1부터 10 사이의 값입니다.
        // 이는 우리가 계산해 둔 dp 벡터의 유효한 인덱스 범위(1~10) 안에 있습니다.
        println!("{}", dp[n]);
    }
}