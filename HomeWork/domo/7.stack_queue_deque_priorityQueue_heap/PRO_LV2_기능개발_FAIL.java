import java.util.*;

public class PRO_LV2_기능개발_FAIL {

    public static int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> list = new ArrayList<>();
        int[] sucessDay = new int[progresses.length];
        for (int i = 0; i < progresses.length; i++) {
            sucessDay[i] =  (100 - progresses[i]) % Math.round(speeds[i]) > 0 ? (100 - progresses[i]) / Math.round(speeds[i]) + 1 : (100 - progresses[i]) / Math.round(speeds[i]);
        }


        int startDay = sucessDay[0];
        int count = 1;
        for (int i = 0; i < sucessDay.length; i++){
            System.out.print(sucessDay[i] + " ");
        }
        for (int i = 1; i < sucessDay.length; i++){
            if(sucessDay[i] < startDay) {
                count ++;
            } else {
                startDay = sucessDay[i];
                list.add(count);
                count = 1;
            }
        }
        list.add(count);

        return list.stream().mapToInt(i -> i).toArray();
    }

    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(Arrays.toString(solution(progresses, speeds)));

        progresses = new int[]{95, 90, 99, 99, 80, 99};
        speeds = new int[]{1, 1, 1, 1, 1, 1};
        System.out.println(Arrays.toString(solution(progresses, speeds)));
    }
}
