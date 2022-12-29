import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_2667_단지번호붙이기 {
	public static int[][] arr;
	public static int[][] visited;
	public static int[] xDics = {1, -1, 0, 0};
	public static int[] yDics = {0, 0, 1, -1};
	public static int[] count = new int[1000];

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		arr = new int[N][N];
		visited = new int[N][N];

		for (int i = 0; i < N; i++) {
			String temp = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(temp.split("")[j]);
			}
		}

		int id = 0;
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr[i].length; j++) {
				if (arr[i][j] == 1 && visited[i][j] == 0) {
					id++;
					visited[i][j] = id;
					count[id] = bfs(j, i, id);
				}
			}
		}

		System.out.println(id);
		Arrays.sort(count,1,id+1);
		for (int i = 1; i <= id; i++) {
			System.out.println(count[i]+1);
		}
	}

	public static int bfs(int x, int y, int id) {
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[]{x, y});
		int count = 0;

		while (!queue.isEmpty()) {
			int[] cur = queue.poll();
			int curX = cur[0];
			int curY = cur[1];


			for (int i = 0; i < 4; i++) {
				int newX = curX + xDics[i];
				int newY = curY + yDics[i];

				if (newX < 0 || newX >= arr.length || newY < 0 || newY >= arr.length) {
					continue;
				}
				if (visited[newY][newX] != 0) {
					continue;
				}
				if (arr[newY][newX] == 1) {
					visited[newY][newX] = id;
					count++;
					queue.offer(new int[]{newX, newY});
				}
			}
		}
		return count;
	}
}