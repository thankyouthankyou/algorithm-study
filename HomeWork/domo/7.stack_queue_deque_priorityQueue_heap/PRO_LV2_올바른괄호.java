import java.util.Stack;

public class PRO_LV2_올바른괄호 {
    static boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack = new Stack();

        for (char c : s.toCharArray()) {
            if ('(' == c ) {
                stack.add(c);
            } else if (')' == c) {
                if(stack.isEmpty()) return false;
                stack.pop();
            }
        }

        if(!stack.isEmpty()) return false;
        return answer;
    }

    public static void main(String[] args) {
        String s = "()()";
        System.out.println(solution(s));
    }
}