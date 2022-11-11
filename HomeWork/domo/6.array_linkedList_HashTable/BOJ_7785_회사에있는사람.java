import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class BOJ_7785_회사에있는사람 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        HashSet<String> set = new HashSet<>();

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            String name = str.split(" ")[0];
            String cmd = str.split(" ")[1];

            if(cmd.equals("enter")) {
                set.add(name);
            } else {
                if(set.contains(name)){
                    set.remove(name);
                }
            }
        }
        ArrayList<String> list = new ArrayList<>(set);
        Collections.sort(list, Collections.reverseOrder());
        for (int i = 0; i < list.size(); i++) {
           sb.append(list.get(i)).append("\n");
        }
        System.out.println(sb);
    }
}
