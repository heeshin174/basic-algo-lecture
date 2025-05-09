import java.util.*;  
import java.io.*;  
  
public class Main {  
    static int N, M;  
    static int[][] graph;  
    static boolean[][] visited; // 방문 기록
    static int[] dx = {0, 0, -1, 1};  
    static int[] dy = {-1, 1, 0, 0};  
    public static void main(String[] args) throws IOException {  
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
        StringTokenizer st = new StringTokenizer(br.readLine());  
        N = Integer.parseInt(st.nextToken());  
        M = Integer.parseInt(st.nextToken());  
        graph = new int[N][M];  
        for (int i = 0; i < N; i++) {  
            st = new StringTokenizer(br.readLine());  
            for (int j = 0; j < M; j++) {  
                graph[i][j] = Integer.parseInt(st.nextToken());  
            }  
        }

		// BFS 구현
        Queue<int[]> queue = new LinkedList<>();  
        queue.add(new int[] {0, 0}); // 시작점
        visited = new boolean[N][M];  
        visited[0][0] = true; 
        while (!queue.isEmpty()) {  
            int[] node = queue.poll();
            int x = node[0];
            int y = node[1];
            // 상하좌우 탐색
            for (int i = 0; i < 4; i++) {  
                int nx = x + dx[i];  
                int ny = y + dy[i];  
                if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;  
                if (graph[nx][ny] != 1 || visited[nx][ny]) continue;  
                visited[nx][ny] = true;  
                queue.add(new int[] {nx, ny});  
            }  
        }  
    }  
}