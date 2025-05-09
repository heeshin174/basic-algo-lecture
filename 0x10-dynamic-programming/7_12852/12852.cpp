#include <bits/stdc++.h>
using namespace std;

int dp[1000005];
int prev[1000005];
int n;

int main(void) {
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  dp[1] = 0;
  for(int i = 2; i <= n; i++){
    dp[i] = dp[i-1] + 1;
    prev[i] = i-1;
    if(i%2 == 0 && dp[i] > dp[i/2] + 1){
      dp[i] = dp[i/2] + 1;
      prev[i] = i/2;
    }
    if(i%3 == 0 && dp[i] > dp[i/3] + 1){
      dp[i] = dp[i/3] + 1;
      prev[i] = i/3;
    }
  }
  cout << dp[n] << '\n';
  int cur = n;
  while(true){
    cout << cur << ' ';
    if(cur == 1) break;
    cur = prev[cur];    
  }
}
