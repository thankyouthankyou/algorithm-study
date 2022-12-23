import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1780_종이의개수 {
	public static int minus;
	public static int zero;
	public static int plus;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		divide(arr);
		System.out.println(minus);
		System.out.println(zero);
		System.out.println(plus);

	}

	private static void divide(int[][] arr) {
		int minusCnt = 0;
		int zeroCnt = 0;
		int plusCnt = 0;
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr.length; j++) {
				if (arr[i][j] == -1) minusCnt++;
				if (arr[i][j] == 0) zeroCnt++;
				if (arr[i][j] == 1) plusCnt++;
			}
		}

		if (minusCnt == arr.length * arr.length) {
			minus++;
			return;
		}
		if (zeroCnt == arr.length * arr.length) {
			zero++;
			return;
		}
		if (plusCnt == arr.length * arr.length) {
			plus++;
			return;
		}

		int len = arr.length / 3;
		int[][] tmp = new int[len][len];

		for (int i = 0; i < len; i++) { // 1
			for (int j = 0; j < len; j++) {
				tmp[i][j] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = 0; i < len; i++) { // 2
			for (int j = len; j < len * 2; j++) {
				tmp[i][j - len] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = 0; i < len; i++) { // 3
			for (int j = len * 2; j < len * 3; j++) {
				tmp[i][j - len * 2] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len; i < len * 2; i++) { // 4
			for (int j = 0; j < len; j++) {
				tmp[i - len][j] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len; i < len * 2; i++) { // 5
			for (int j = len; j < len * 2; j++) {
				tmp[i - len][j - len] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len; i < len * 2; i++) { // 6
			for (int j = len * 2; j < len * 3; j++) {
				tmp[i - len][j - len * 2] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len * 2; i < len * 3; i++) { // 7
			for (int j = 0; j < len ; j++) {
				tmp[i - len * 2][j] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len * 2; i < len * 3; i++) { // 8
			for (int j = len; j < len * 2 ; j++) {
				tmp[i - len * 2][j - len] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len * 2; i < len * 3; i++) { // 7
			for (int j = len * 2; j < len * 3 ; j++) {
				tmp[i - len * 2][j - len * 2] = arr[i][j];
			}
		}
		divide(tmp);

	}
}
