import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class BOJ_18870_좌표압축 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        int[] nums = new int[N];

        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        int[] sortNums = nums.clone();
        Arrays.sort(sortNums);

        HashMap<Integer, Integer> map = new HashMap<>();
        int cnt = 0;
        for (int x : sortNums) {
            if (!map.containsKey(x)) {
                map.put(x, cnt++);
            }
        }

        for (int x : nums) {
            sb.append(map.get(x)).append(" ");
        }
        System.out.println(sb);
    }

}
