import java.util.*;

public class test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> list = new ArrayList<>();
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        for (int i = 0; i < n; i++) list.add(scanner.nextInt());
        Collections.sort(list);
        int maxSum = sum(list) / 2;
        for (int i = 0; i < n; i++) {
            if (sum(list1) <= sum(list2)) {
                list1.add(list.get(i));
                if (sum(list1) >= maxSum) {
                    for (int k = i + 1; k < n; k++)
                        list2.add(list.get(k));
                    break;
                }
            } else {
                list2.add(list.get(i));
                if (sum(list2) >= maxSum) {
                    for (int k = i + 1; k < n; k++)
                        list1.add(list.get(k));
                    break;
                }
            }
        }
        System.out.println(list1);
        System.out.println(list2);

        System.out.println(Math.abs(sum(list1) - sum(list2)));
    }

    public static int sum(List<Integer> list) {
        return list.stream().reduce(0, Integer::sum);
    }
}
