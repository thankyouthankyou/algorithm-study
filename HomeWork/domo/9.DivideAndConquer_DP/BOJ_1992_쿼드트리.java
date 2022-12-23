import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1992_쿼드트리 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N][N];

		for (int i = 0; i < N; i++) {
			String tmp = br.readLine();
			for (int j = 0; j < N; j++) {
				arr[i][j] = Integer.parseInt(tmp.split("")[j]);
			}
		}

		divide(arr);
	}

	private static void divide(int[][] arr) {
		int allCnt = 0;
		for (int i = 0; i < arr.length; i++) {
			for (int j = 0; j < arr.length; j++) {
				if (arr[i][j] == 1) {
					allCnt++;
				}
			}
		}

		if (allCnt == arr.length * arr.length) {
			System.out.print(1);
			return;
		} else if (allCnt == 0) {
			System.out.print(0);
			return;
		}

		int len = arr.length / 2;
		int[][] tmp = new int[len][len];

		System.out.print("(");
		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				tmp[i][j] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = 0; i < len; i++) {
			for (int j = len; j < len * 2; j++) {
				tmp[i][j - len] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len; i < len * 2; i++) {
			for (int j = 0; j < len; j++) {
				tmp[i - len][j] = arr[i][j];
			}
		}
		divide(tmp);

		for (int i = len; i < len * 2; i++) {
			for (int j = len; j < len * 2; j++) {
				tmp[i - len][j - len] = arr[i][j];
			}
		}
		divide(tmp);
		System.out.print(")");
	}
}
