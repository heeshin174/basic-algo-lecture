#include <bits/stdc++.h>
using namespace std;

int score[305];
int n;
int dp[305];

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  for(int i = 1; i <= n; i++) cin >> score[i];
  if(n == 1){
    cout << score[1];
    return 0;
  } else if (n == 2) {
    cout << score[1]+score[2];
    return 0;
  }
  dp[1] = score[1];
  dp[2] = score[1]+score[2];
  dp[3] = score[3]+max(score[1], score[2]);
  for(int i = 4; i <= n; i++){
    dp[i] = score[i]+max(dp[i-3]+score[i-1], dp[i-2]);
  }
  cout << dp[n];
}
