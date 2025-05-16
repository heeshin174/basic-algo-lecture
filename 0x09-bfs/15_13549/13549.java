import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        dist = new int[100001];

        Arrays.fill(dist, -1);

        Deque<Integer> deque = new ArrayDeque<>();
        deque.add(n);
        dist[n] = 0;

        while (!deque.isEmpty()) {
            int current = deque.poll();

            if (current == m) break;

            // 순간이동: 비용 0 → 앞에 넣기
            int teleport = current * 2;
            if (teleport <= 100000 && dist[teleport] == -1) {
                dist[teleport] = dist[current];
                deque.addFirst(teleport);
            }

            // 걷기: 비용 1 → 뒤에 넣기
            for (int next : new int[]{current - 1, current + 1}) {
                if (next >= 0 && next <= 100000 && dist[next] == -1) {
                    dist[next] = dist[current] + 1;
                    deque.addLast(next);
                }
            }
        }

        System.out.println(dist[m]);
    }
}
