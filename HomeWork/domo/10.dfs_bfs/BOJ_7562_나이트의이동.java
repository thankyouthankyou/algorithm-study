import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7562_나이트의이동 {
	public static int[][] arr;
	public static boolean[][] visited;
	public static int N;
	public static int targetX;
	public static int targetY;
	public static int[] xArray = {1, 2, 2, 1, -1, -2, -2, -1};
	public static int[] yArray = {2, 1, -1, -2, -2, -1, 1, 2};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			N = Integer.parseInt(br.readLine());
			visited = new boolean[N][N];

			st = new StringTokenizer(br.readLine());
			int startX = Integer.parseInt(st.nextToken());
			int startY = Integer.parseInt(st.nextToken());

			st = new StringTokenizer(br.readLine());
			targetX = Integer.parseInt(st.nextToken());
			targetY = Integer.parseInt(st.nextToken());

			bfs(startX, startY);
		}
	}

	public static void bfs(int startX, int startY) {
		Queue<int[]> queue = new LinkedList<>();
		visited[startY][startX] = true;
		queue.offer(new int[]{startX, startY, 0});

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int x = cur[0];
			int y = cur[1];
			int cnt = cur[2];

			if (x == targetX && y == targetY) {
				System.out.println(cnt);
				return;
			}

			for (int i = 0; i < 8; i++) {
				int nx = x + xArray[i];
				int ny = y + yArray[i];

				if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[ny][nx]) {
					visited[ny][nx] = true;
					queue.offer(new int[]{nx, ny, cnt + 1});
				}

			}
		}
	}
}
