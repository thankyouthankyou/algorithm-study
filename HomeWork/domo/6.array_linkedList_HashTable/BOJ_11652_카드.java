import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_11652_카드 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<Long, Integer> map = new HashMap<>();
        for (int i = 0; i < N; i++) {
            Long num = Long.parseLong(br.readLine());
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        ArrayList<Integer> list = new ArrayList(map.values());

        int max = 0;
        for (Integer num : list)
            if (num > max)
                max = num;

        PriorityQueue queue = new PriorityQueue();
        for (Long key : map.keySet())
            if (max == map.get(key)) {
                queue.add(key);
            }


        System.out.println(queue.poll());
    }
}
