import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class BOJ_10799_쇠막대기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str =  br.readLine();
        str = str.replace("()", "R");

        char[] cArray = str.toCharArray();

        Stack<Character> stack = new Stack<>();
        int count = 0;
        for (int i = 0; i < cArray.length; i++) {
            if(cArray[i] == '('){
                stack.push('(');
            }
            if(cArray[i] == ')') {
                stack.pop();
                count += 1;
            }
            if(cArray[i] == 'R') {
                count += stack.size();
            }
        }
        System.out.println(count);

    }
}
