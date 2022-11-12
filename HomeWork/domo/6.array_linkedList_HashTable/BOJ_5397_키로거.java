import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_5397_키로거 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        Stack<String> leftStack = new Stack<>();
        Stack<String> rightStack = new Stack<>();

        for (int i = 0; i < N; i++) {
            String[] cmds = br.readLine().split("");
            for (int j = 0; j < cmds.length; j++) {
                switch (cmds[j]) {
                    case "<":
                        if (!leftStack.isEmpty()) {
                            rightStack.push(leftStack.pop());
                        }
                        break;
                    case ">":
                        if (!rightStack.isEmpty()) {
                            leftStack.push(rightStack.pop());
                        }
                        break;
                    case "-":
                        if (!leftStack.isEmpty()) {
                            leftStack.pop();
                        }
                        break;
                    default :
                        leftStack.push(cmds[j]);
                        break;
                }
            }

            while (!leftStack.isEmpty()) {
                rightStack.push(leftStack.pop());
            }
            while (!rightStack.isEmpty()){
                sb.append(rightStack.pop());
            }
            sb.append("\n");
            leftStack.clear();
            rightStack.clear();
        }
        System.out.println(sb);
    }
}
