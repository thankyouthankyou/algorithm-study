import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2954_나는요리사다 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[5];
        int max = Integer.MIN_VALUE;
        int maxIdx = 0;
        for (int i = 0; i < 5; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 4; j++) {
                arr[i] += Integer.parseInt(st.nextToken());
                if(j==3 && max < arr[i]) {
                    max = arr[i];
                    maxIdx = i+1;
                }
            }
        }

        System.out.println(maxIdx + " " + max);
    }
}