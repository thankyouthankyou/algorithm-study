import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_1406_에디터 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String[] str = br.readLine().split("");
        int M = Integer.parseInt(br.readLine());

        Stack<String> lStack = new Stack();
        Stack<String> rStack = new Stack();

        for (int i = 0; i < str.length; i++) {
            lStack.push(str[i]);
        }

        for (int i = 0; i < M; i++) {
            String[] cmd = br.readLine().split(" ");
            switch (cmd[0]){
                case "L" :
                    if(lStack.size() > 0){
                        rStack.push(lStack.pop());
                    }
                    break;
                case "D" :
                    if(rStack.size() > 0) {
                        lStack.push(rStack.pop());
                    }
                    break;
                case "B" :
                    if(lStack.size() > 0) {
                        lStack.pop();
                    }
                    break;
                case "P" :
                    String data = cmd[1];
                    lStack.push(data);
                    break;
            }
        }
        while (!lStack.isEmpty()){
            rStack.push(lStack.pop());
        }

        while (!rStack.isEmpty()) {
            sb.append(rStack.pop());
        }
        System.out.println(sb);
    }
}
