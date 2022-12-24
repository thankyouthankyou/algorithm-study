import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2178_미로탐색 {
	public static int N;
	public static int M;
	public static int[] xArray = {1, -1, 0, 0};
	public static int[] yArray = {0, 0, 1, -1};
	public static int[][] arr;
	public static boolean[][] visitied;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		arr = new int[N+1][M+1];
		visitied = new boolean[N+1][M+1];

		for (int i = 1; i <= N; i++) {
			String str = br.readLine();
			for (int j = 1; j <= M; j++) {
				arr[i][j] = Integer.parseInt(str.split("")[j-1]);
			}
		}

		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[]{1, 1, 1});
		visitied[1][1] = true;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int x = cur[0];
			int y = cur[1];
			int cnt = cur[2];

			if (x == N && y == M) {
				System.out.println(cnt);
				break;
			}

			if (x >= 1 && x <= N && y >= 1 && y <= M) {
				for (int i = 0; i < 4; i++) {
					int nx = x + xArray[i];
					int ny = y + yArray[i];

					if (nx >= 1 && nx <= N && ny >= 1 && ny <= M && !visitied[nx][ny] && arr[nx][ny] == 1) {
						visitied[nx][ny] = true;
						queue.offer(new int[]{nx, ny, cnt + 1});
					}
				}
			}
		}
	}
}
