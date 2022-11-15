import java.util.*;
public class PRO_LV1_같은숫자는싫어 {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.add(arr[0]);

        for(int i=1; i<arr.length; i++){
            if(!stack.peek().equals(arr[i])){
                stack.add(arr[i]);
            }
        }

        int[] answer = new int[stack.size()];

        for(int i=stack.size()-1; i>=0; i--){
            answer[i] = stack.pop();
        }

        return answer;
    }

}
