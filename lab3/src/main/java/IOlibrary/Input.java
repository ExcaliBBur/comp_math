package IOlibrary;

import java.util.Scanner;

public class Input {
    private final Scanner scanner = new Scanner(System.in);

    public int getNumber(boolean isMethod) {
        while (true) {
            if (!isMethod) System.out.print("¬ыберите номер определенного интеграла, который хотите вычислить: ");
            else {
                System.out.print("\n¬ведите номер метода, который хотите использовать: ");
            }
            try {
                int number = Integer.parseInt(scanner.next());
                if (!isMethod) {
                    if (number < 1 || number > 5) throw new NumberFormatException();
                } else {
                    if (number > 3 || number < 1) throw new NumberFormatException();
                }
                return number;
            } catch (NumberFormatException e) {
                if (!isMethod) System.out.println("¬ведите число от 1 до 5");
                else System.out.println("¬ведите число от 1 до 3");
            }
        }
    }

    public int getModification() {
        while (true) {
            System.out.print("\n¬ведите номер модификации, который хотите использовать: ");
            try {
                int number = Integer.parseInt(scanner.next());
                if (number > 3 || number < 1) throw new NumberFormatException();
                return number;
            } catch (NumberFormatException e) {
                System.out.println("¬ведите число от 1 до 3");
            }
        }
    }

    public double getBound(boolean isLower) {
        while (true) {
            if (isLower) System.out.print("\n¬ведите нижний предел интегрировани€: ");
            else System.out.print("\n¬ведите верхний предел интегрировани€: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("¬ведите численную границу");
            }
        }
    }

    public double getEpsilon() {
        while (true) {
            System.out.print("¬ведите погрешность вычислени€: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("¬ведите численную погрешность");
            }
        }
    }
}
