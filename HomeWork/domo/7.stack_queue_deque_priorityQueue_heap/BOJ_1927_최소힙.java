import java.io.*;
import java.util.PriorityQueue;

public class BOJ_1927_최소힙 {
    public static void main(String[] args) throws IOException {
        PriorityQueue pq = new PriorityQueue();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            if (num == 0) {
                if(pq.isEmpty()){
                    System.out.println(0);
                } else {
                    System.out.println(pq.poll());
                }
            } else {
                pq.offer(num);
            }
        }
    }
}