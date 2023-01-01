import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_11724_연결요소의개수 {
	public static int N;
	public static int[][] arr;
	public static boolean[] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		arr = new int[N+1][N+1];
		visited = new boolean[N+1];
		int cnt = 0;

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			arr[u][v] = 1;
			arr[v][u] = 1;
		}

		for (int i = 1; i <= N; i++) {
			if (!visited[i]) {
				dfs(i);
				cnt++;
			}
		}
		System.out.println(cnt);
	}

	private static void dfs(int j) {
		visited[j] = true;

		for (int k = 1; k <= N; k++) {
			if (arr[j][k] == 1 && !visited[k]) {
				dfs(k);
			}
		}
	}
}
