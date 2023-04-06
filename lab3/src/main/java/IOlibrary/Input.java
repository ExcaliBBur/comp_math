package IOlibrary;

import java.util.Scanner;

public class Input {
    private final Scanner scanner = new Scanner(System.in);

    public int getNumber(boolean isMethod) {
        while (true) {
            if (!isMethod) System.out.print("Âûáåðèòå íîìåð îïðåäåëåííîãî èíòåãðàëà, êîòîðûé õîòèòå âû÷èñëèòü: ");
            else {
                System.out.print("\nÂâåäèòå íîìåð ìåòîäà, êîòîðûé õîòèòå èñïîëüçîâàòü: ");
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
                if (!isMethod) System.out.println("Ââåäèòå ÷èñëî îò 1 äî 5");
                else System.out.println("Ââåäèòå ÷èñëî îò 1 äî 3");
            }
        }
    }

    public int getModification() {
        while (true) {
            System.out.print("\nÂâåäèòå íîìåð ìîäèôèêàöèè, êîòîðûé õîòèòå èñïîëüçîâàòü: ");
            try {
                int number = Integer.parseInt(scanner.next());
                if (number > 3 || number < 1) throw new NumberFormatException();
                return number;
            } catch (NumberFormatException e) {
                System.out.println("Ââåäèòå ÷èñëî îò 1 äî 3");
            }
        }
    }

    public double getBound(boolean isLower) {
        while (true) {
            if (isLower) System.out.print("\nÂâåäèòå íèæíèé ïðåäåë èíòåãðèðîâàíèÿ: ");
            else System.out.print("\nÂâåäèòå âåðõíèé ïðåäåë èíòåãðèðîâàíèÿ: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("Ââåäèòå ÷èñëåííóþ ãðàíèöó");
            }
        }
    }

    public double getEpsilon() {
        while (true) {
            System.out.print("Ââåäèòå ïîãðåøíîñòü âû÷èñëåíèÿ: ");
            try {
                return Double.parseDouble(scanner.next().replaceAll(",", "."));
            } catch (NumberFormatException e) {
                System.out.println("Ââåäèòå ÷èñëåííóþ ïîãðåøíîñòü");
            }
        }
    }
}
