import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_1021_회전하는큐 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int N = Integer.parseInt(str.split(" ")[0]);
        int M = Integer.parseInt(str.split(" ")[1]);

        Queue<Integer> queue = new LinkedList<>();
        Queue<Integer> findQueue = new LinkedList<>();
        int answer = 0;


        for (int i = 1; i <= N; i++) {
            queue.offer(i);
        }

        str = br.readLine();
        for (int i = 0; i < M; i++) {
            findQueue.offer(Integer.parseInt(str.split(" ")[i]));
        }

        while (!findQueue.isEmpty()) {
            int find = findQueue.poll();
            int count = 0;
            while (find != queue.peek()) {
                queue.offer(queue.poll());
                count++;
            }
            answer += Math.min(count, queue.size() - count);
            queue.poll();
        }
        System.out.println(answer);
    }
}
