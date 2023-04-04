package IOlibrary;

import java.util.Scanner;

public class Input {
    private final Scanner scanner = new Scanner(System.in);

    public int getNumber(boolean isMethod) {
        while (true) {
            if (!isMethod) System.out.print("�������� ����� ������������� ���������, ������� ������ ���������: ");
            else {
                System.out.print("\n������� ����� ������, ������� ������ ������������: ");
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
                if (!isMethod) System.out.println("������� ����� �� 1 �� 5");
                else System.out.println("������� ����� �� 1 �� 3");
            }
        }
    }

    public int getModification() {
        while (true) {
            System.out.print("\n������� ����� �����������, ������� ������ ������������: ");
            try {
                int number = Integer.parseInt(scanner.next());
                if (number > 3 || number < 1) throw new NumberFormatException();
                return number;
            } catch (NumberFormatException e) {
                System.out.println("������� ����� �� 1 �� 3");
            }
        }
    }

    public double getBound(boolean isLower) {
        while (true) {
            if (isLower) System.out.print("\n������� ������ ������ ��������������: ");
            else System.out.print("\n������� ������� ������ ��������������: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("������� ��������� �������");
            }
        }
    }

    public double getEpsilon() {
        while (true) {
            System.out.print("������� ����������� ����������: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("������� ��������� �����������");
            }
        }
    }
}
