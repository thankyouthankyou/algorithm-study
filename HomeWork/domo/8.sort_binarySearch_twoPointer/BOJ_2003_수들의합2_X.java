import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2003_수들의합2_X {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] arr = new int[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        int lt = 0;
        int sum = 0;
        for (int rt = 0; rt < N; rt++) {
            sum += arr[rt];
            if (sum == M) {
                answer++;
                sum = 0;
            } else if (sum > M) {
                rt = lt;
                lt ++;
                sum = 0;
            }

        }

        System.out.println(answer);
    }

}
