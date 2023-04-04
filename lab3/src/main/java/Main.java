import CustomMath.Limits;
import IOlibrary.Input;
import exceptions.NoLimitException;
import expression.Expression;
import expression.Result;
import methods.*;


public class Main {
    public static void main(String[] args) {

        final int n = 4;
        Input input = new Input();

        System.out.println("1: (x^2) dx ");
        System.out.println("2: (sin(x)) dx");
        System.out.println("3: (1 / sqrt(x)) dx");
        System.out.println("4: (1 / x^2) dx");
        System.out.println("5: (1 / (1 - x)) dx");

        int numberOfExpression = input.getNumber(false);
        double left = input.getBound(true);
        double right = input.getBound(false);

        System.out.println("\n1: ����� ��������������� (3 �����������: �����, ������, �������)");
        System.out.println("2: ����� ��������");
        System.out.println("3: ����� ��������");
        int numberOfMethod = input.getNumber(true);
        double epsilon = input.getEpsilon();

        Expression expression = new Expression(numberOfExpression);

        try {
            Limits.limit(expression, left, "������� � ����� A �� ����������");
            Limits.limit(expression, right, "������� � ����� B �� ����������");
            Limits.limitOnInterval(expression, left, right);
        } catch (NoLimitException e) {
            System.out.println(e.toString());
            System.out.println("�������� �� ����������. ��������� ��������� ���� ������");
            System.exit(1);
        }

        if (numberOfMethod == 1) {
            int modificationOfMethod = input.getModification();
            switch (modificationOfMethod) {
                case (1) -> {
                    LeftRectangleMethod leftRectangleMethod = new LeftRectangleMethod();
                    Result res1 = leftRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res1 != null)
                        System.out.println("����� ����� ������������� ��������� �� " + res1.getN()
                                + " ��������� � ����������� " + res1.getRes());
                }
                case (2) -> {
                    RightRectangleMethod rightRectangleMethod = new RightRectangleMethod();
                    Result res2 = rightRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res2 != null)
                        System.out.println("����� ������ ������������� ��������� �� " + res2.getN()
                                + " ��������� � ����������� " + res2.getRes());
                }
                case (3) -> {
                    MidRectangleMethod midRectangleMethod = new MidRectangleMethod();
                    Result res3 = midRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res3 != null)
                        System.out.println("����� ������� ������������� ��������� �� " + res3.getN()
                                + " ��������� � ����������� " + res3.getRes());
                }
            }
        } else if (numberOfMethod == 2) {
            TrapezoidalMethod trapezoidalMethod = new TrapezoidalMethod();

            Result res = trapezoidalMethod.compute(left, right, n, epsilon, expression);

            if (res != null)
                System.out.println("����� �������� ��������� �� " + res.getN()
                        + " ��������� � ����������� " + res.getRes());
        } else {
            SimpsonMethod simpsonMethod = new SimpsonMethod();

            Result res = simpsonMethod.compute(left, right, n, epsilon, expression);

            if (res != null)
                System.out.println("����� �������� ��������� �� " + res.getN()
                        + " ��������� � ����������� " + res.getRes());
        }
    }
}
