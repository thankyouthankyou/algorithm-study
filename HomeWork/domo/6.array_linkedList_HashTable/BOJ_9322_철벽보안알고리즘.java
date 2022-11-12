import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ_9322_철벽보안알고리즘 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            HashMap<String, Integer> map = new HashMap<>();

            int[] nomal = new int[N];
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                map.put(st.nextToken(), j);
            }

            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                nomal[j] = map.get(st.nextToken());
            }

            st = new StringTokenizer(br.readLine(), " ");
            String[] res = new String[N];
            for (int j = 0; j < N; j++) {
                res[nomal[j]] = st.nextToken();
            }
            for (int j = 0; j < N; j++) {
                sb.append(res[j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
