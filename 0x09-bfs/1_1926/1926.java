import java.util.*;  
import java.io.*;  
  
public class Main {  
    static int n, m;  
    static int[][] graph;  
    static int[][] visited;  
    static int[] dx = {0, 0, -1, 1};  
    static int[] dy = {-1, 1, 0, 0};  
    public static void main(String[] args) throws IOException {  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        StringTokenizer st = new StringTokenizer(br.readLine());  
        n = Integer.parseInt(st.nextToken());  
        m = Integer.parseInt(st.nextToken());  
        graph = new int[n][m];  
        for (int i = 0; i < n; i++) {  
            st = new StringTokenizer(br.readLine());  
            for (int j = 0; j < m; j++) {  
                graph[i][j] = Integer.parseInt(st.nextToken());  
            }  
        }  
  
        Queue<int[]> queue = new LinkedList<>();  
        visited = new int[n][m];  
        int num = 0; // 그림의 개수  
        int max = 0; // 그림의 넓이의 최댓값  
        for (int i =0; i<n; i++) {  
            for (int j = 0; j<m; j++) {  
               if (graph[i][j] == 0 || visited[i][j] == 1) {  
                   continue;  
               }  
               num++;  
               visited[i][j] = 1;  
               queue.add(new int[] {i, j});  
               int area = 0;  
                while (!queue.isEmpty()) {  
                   area++;  
                   int[] node = queue.poll();
                   int x = node[0];
                   int y = node[1];
                   for(int k = 0; k<4; k++) {  
                       int nx = x + dx[k];  
                       int ny = y + dy[k];
						// 경계 밖 무시
						if (nx<0 || ny<0 || nx>=n || ny>=m) continue;
						// 이미 간 곳 또는 갈 수 없는 벽 무시
						if (visited[nx][ny] == 1 || graph[nx][ny] != 1) continue;
						visited[x][y] = 1;  
						queue.add(new int[]({x, y});  
                   }  
               }  
               max = Math.max(max, area);  
            }  
        }  
        System.out.println(num);  
        System.out.println(max);  
    }  
}