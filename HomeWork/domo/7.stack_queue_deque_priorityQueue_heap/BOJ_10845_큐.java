import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        int[] queue = new int[N];
        int front = 0;
        int back = -1;
        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            String cmd = str.split(" ")[0];
            switch (cmd) {
                case "push":
                    int value = Integer.parseInt(str.split(" ")[1]);
                    queue[++back] = value;
                    break;
                case "pop":
                    if (front > back) {
                        sb.append("-1\n");
                    } else {
                        sb.append(queue[front++] + "\n");
                    }
                    break;
                case "size":
                    sb.append((back - front + 1) + "\n");
                    break;
                case "empty" :
                    if(front > back){
                        sb.append("1\n");
                    }else{
                        sb.append("0\n");
                    }
                    break;
                case "front":
                    if(front > back){
                        sb.append("-1\n");
                    }else{
                        sb.append(queue[front] + "\n");
                    }
                    break;
                case "back":
                    if(front > back){
                        sb.append("-1\n");
                    }else{
                        sb.append(queue[back]+"\n");
                    }
                    break;
            }
        }
        System.out.println(sb);
    }
}