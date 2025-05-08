import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.lang.Math;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[][] score = new int[n + 1][3];
        int[][] dp = new int[n + 1][3];

        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            score[i][0] = Integer.parseInt(st.nextToken()); // Red cost
            score[i][1] = Integer.parseInt(st.nextToken()); // Green cost
            score[i][2] = Integer.parseInt(st.nextToken()); // Blue cost
        }

        // Base case: for the first house (index 1)
        dp[1][0] = score[1][0];
        dp[1][1] = score[1][1];
        dp[1][2] = score[1][2];

        // Fill the dp table for subsequent houses
        for (int i = 2; i <= n; i++) {
            // If house i is painted Red (0), house i-1 must be Green (1) or Blue (2)
            dp[i][0] = score[i][0] + Math.min(dp[i - 1][1], dp[i - 1][2]);

            // If house i is painted Green (1), house i-1 must be Red (0) or Blue (2)
            dp[i][1] = score[i][1] + Math.min(dp[i - 1][0], dp[i - 1][2]);

            // If house i is painted Blue (2), house i-1 must be Red (0) or Green (1)
            dp[i][2] = score[i][2] + Math.min(dp[i - 1][0], dp[i - 1][1]);
        }

        System.out.println(Math.min(Math.min(dp[n][0], dp[n][1]), dp[n][2]));
        br.close(); // Close the BufferedReader
    }
}