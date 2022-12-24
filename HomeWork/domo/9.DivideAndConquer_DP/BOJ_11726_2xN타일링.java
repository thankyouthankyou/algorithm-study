import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11726_2xN타일링 {
	public static long[] dp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		dp = new long[1001];
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 3;
		dp[4] = 5;

		System.out.println(solution(N));
	}

	private static long solution(int N) {
		if (N <= 4) {
			return dp[N];
		}

		for (int i = 5; i <= N; i++) {
			dp[i] = (dp[i-1] % 10007) + (dp[i-2] % 10007);
		}
		return dp[N];
	}
}