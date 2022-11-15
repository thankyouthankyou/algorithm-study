import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_11723_집합 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int M = Integer.parseInt(br.readLine());
        int bitMask = 0;
        int num = 0;
        for (int i = 0; i < M; i++) {
            String[] str = br.readLine().split(" ");
            switch (str[0]) {
                case "add" :
                    num = Integer.parseInt(str[1]);
                    bitMask |= (1 << num - 1);
                    break;
                case "remove" :
                    num = Integer.parseInt(str[1]);
                    bitMask &= ~(1 << num - 1);
                    break;
                case "check" :
                    num = Integer.parseInt(str[1]);
                    sb.append(
                    (bitMask & (1 << num - 1)) != 0 ? "1\n" : "0\n"
                    );
                    break;
                case "toggle" :
                    num = Integer.parseInt(str[1]);
                    bitMask ^= (1 << num - 1);
                    break;
                case "all" :
                    bitMask |= (~0);
                    break;
                case "empty" :
                    bitMask &= 0;
                    break;
            }
        }
        System.out.println(sb);
    }
}
