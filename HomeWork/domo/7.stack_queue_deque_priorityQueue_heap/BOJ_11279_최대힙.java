import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;

public class BOJ_11279_최대힙 {
    public static void main(String[] args) throws IOException {
        PriorityQueue pq = new PriorityQueue(Collections.reverseOrder());
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