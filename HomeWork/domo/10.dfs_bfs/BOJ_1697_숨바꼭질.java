import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1697_숨바꼭질 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		boolean[] visited = new boolean[100001];
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[]{N, 0});
		visited[N] = true;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int x = cur[0];
			int cnt = cur[1];

			if (x == K) {
				System.out.println(cnt);
				return;
			}

			int nx;
			nx = x * 2;
			if (nx >= 0 && nx <= 100000 && !visited[nx]){
				visited[nx] = true;
				queue.offer(new int[]{nx, cnt + 1});
			}

			nx = x + 1;
			if (nx >= 0 && nx <= 100000 && !visited[nx]){
				visited[nx] = true;
				queue.offer(new int[]{nx, cnt + 1});
			}

			nx = x - 1;
			if (nx >= 0 && nx <= 100000 && !visited[nx]){
				visited[nx] = true;
				queue.offer(new int[]{nx, cnt + 1});
			}
		}
	}
}
