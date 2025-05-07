// http://boj.kr/e93e56bb850a46378cf8f53486233cdc
#include <bits/stdc++.h>
using namespace std;

int score[305];
int n;
int dp[305];

int main(void){
  ios::sync_with_stdio(0);
  cin.tie(0);
  cin >> n;
  int tot = 0;
  for(int i = 1; i <= n; i++){
    cin >> score[i];
    tot += score[i];
  }
  if(n <= 2){
    cout << tot;
    return 0;
  }
  dp[1] = score[1];
  dp[2] = score[2];
  dp[3] = score[3];
  for(int i = 4; i <= n-1; i++) dp[i] = min(dp[i-2],dp[i-3])+score[i];
  cout << tot - min(dp[n-1],dp[n-2]);
}
