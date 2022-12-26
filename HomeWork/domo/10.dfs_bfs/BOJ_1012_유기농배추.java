import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1012_유기농배추 {
	public static int N, M, cnt;
	public static int[][] arr;
	public static int[] dx = {1, -1, 0, 0};
	public static int[] dy = {0, 0, 1, -1};
	public static boolean[][] visitied;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			M = Integer.parseInt(st.nextToken());
			N = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			cnt = 0;
			arr = new int[N][M];
			visitied = new boolean[N][M];

			for (int j = 0; j < K; j++) {
				st = new StringTokenizer(br.readLine());
				int X = Integer.parseInt(st.nextToken());
				int Y = Integer.parseInt(st.nextToken());
				arr[Y][X] = 1;
			}

			for (int j = 0; j < N; j++) {
				for (int k = 0; k < M; k++) {
					if (arr[j][k] == 1 && !visitied[j][k]) {
						bfs(j, k);
						cnt++;
					}
				}
			}
			System.out.println(cnt);
		}
	}

	public static void bfs(int y, int x) {
		Queue<int[]> queue = new LinkedList<>();
		visitied[y][x] = true;
		queue.offer(new int[]{x, y});

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int curX = cur[0];
			int curY = cur[1];
			for (int i = 0; i < 4; i++) {
				int nx = curX + dx[i];
				int ny = curY + dy[i];

				if (nx >= 0 && nx < M && ny >= 0 && ny < N && !visitied[ny][nx] && arr[ny][nx] == 1) {
					visitied[ny][nx] = true;
					queue.offer(new int[]{nx, ny});
				}
			}
		}
	}
}
