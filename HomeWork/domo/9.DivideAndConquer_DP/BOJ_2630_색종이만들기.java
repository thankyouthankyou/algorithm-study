import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2630_색종이만들기 {
    public static int white;
    public static int blue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][N];
        StringTokenizer st;

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        divide(arr);
        System.out.println(white);
        System.out.println(blue);
    }

    private static void divide(int[][] arr) {
        int allCount = 0;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i][j] == 1) {
                    allCount += 1;
                }
            }
        }
        if (allCount == (arr.length * arr.length)) {
            blue++;
            return;
        } else if (allCount == 0) {
            white++;
            return;
        }

        int len = arr.length / 2;
        int[][] tmp = new int[len][len];

        for (int i = 0; i < len; i++) { // 1번
            for (int j = 0; j < len; j++) {
                tmp[i][j] = arr[i][j];
            }
        }
        divide(tmp);

        for (int i = 0; i < len; i++) { // 2번
            for (int j = len; j < arr.length; j++) {
                tmp[i][j - len] = arr[i][j];
            }
        }
        divide(tmp);

        for (int i = len; i < arr.length; i++) { // 3번
            for (int j = 0; j < len; j++) {
                tmp[i - len][j] = arr[i][j];
            }
        }
        divide(tmp);

        for (int i = len; i < arr.length; i++) { // 4번
            for (int j = len; j < arr.length; j++) {
                tmp[i - len][j - len] = arr[i][j];
            }
        }
        divide(tmp);
    }
}
