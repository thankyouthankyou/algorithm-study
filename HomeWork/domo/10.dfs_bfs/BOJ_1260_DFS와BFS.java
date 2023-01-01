import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1260_DFS와BFS {
	public static int N;
	public static int M;
	public static int V;
	public static int[][] arr;
	public static boolean[] dfsVisited;
	public static boolean[] bfsVisited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		V = Integer.parseInt(st.nextToken());

		arr = new int[N + 1][N + 1];
		dfsVisited = new boolean[N + 1];
		bfsVisited = new boolean[N + 1];


		for (int i = 0; i < M; i++) {
			String temp = br.readLine();
			int a = Integer.parseInt(temp.split(" ")[0]);
			int b = Integer.parseInt(temp.split(" ")[1]);
			arr[a][b] = 1;
			arr[b][a] = 1;
		}
		dfs(V);
		System.out.println();
		bfs(V);
		System.out.println();
	}

	public static void dfs(int n) {
		if (n < 1 || n >= arr.length) {
			return;
		}

		dfsVisited[n] = true;
		System.out.print(n + " ");

		for (int i = 1; i < arr.length; i++) {
			if (arr[n][i] == 1 && !dfsVisited[i]) {
				dfs(i);
			}
		}

	}

	public static void bfs(int n) {
		Queue<Integer> queue = new LinkedList<>();
		queue.offer(n);

		while (!queue.isEmpty()) {
			int cur = queue.poll();
			if(bfsVisited[cur]){
				continue;
			}
			bfsVisited[cur] = true;
			System.out.print(cur + " ");
			for (int i = 1; i < arr.length; i++) {
				if (arr[cur][i] == 1 && !bfsVisited[i]) {
					queue.offer(i);
				}
			}
		}
	}
}