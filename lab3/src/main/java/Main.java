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

        System.out.println("\n1: Метод прямоугольников (3 модификации: левые, правые, средние)");
        System.out.println("2: Метод трапеций");
        System.out.println("3: Метод Симпсона");
        int numberOfMethod = input.getNumber(true);
        double epsilon = input.getEpsilon();

        Expression expression = new Expression(numberOfExpression);

        try {
            Limits.limit(expression, left, "Предела в точке A не существует");
            Limits.limit(expression, right, "Предела в точке B не существует");
            Limits.limitOnInterval(expression, left, right);
        } catch (NoLimitException e) {
            System.out.println(e.toString());
            System.out.println("Интеграл не существует. Программа завершает свою работу");
            System.exit(1);
        }

        if (numberOfMethod == 1) {
            int modificationOfMethod = input.getModification();
            switch (modificationOfMethod) {
                case (1) -> {
                    LeftRectangleMethod leftRectangleMethod = new LeftRectangleMethod();
                    Result res1 = leftRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res1 != null)
                        System.out.println("Метод левых треугольников отработал за " + res1.getN()
                                + " разбиений с результатом " + res1.getRes());
                }
                case (2) -> {
                    RightRectangleMethod rightRectangleMethod = new RightRectangleMethod();
                    Result res2 = rightRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res2 != null)
                        System.out.println("Метод правых треугольников отработал за " + res2.getN()
                                + " разбиений с результатом " + res2.getRes());
                }
                case (3) -> {
                    MidRectangleMethod midRectangleMethod = new MidRectangleMethod();
                    Result res3 = midRectangleMethod.compute(left, right, n, epsilon, expression);
                    if (res3 != null)
                        System.out.println("Метод средних треугольников отработал за " + res3.getN()
                                + " разбиений с результатом " + res3.getRes());
                }
            }
        } else if (numberOfMethod == 2) {
            TrapezoidalMethod trapezoidalMethod = new TrapezoidalMethod();

            Result res = trapezoidalMethod.compute(left, right, n, epsilon, expression);

            if (res != null)
                System.out.println("Метод трапеций отработал за " + res.getN()
                        + " разбиений с результатом " + res.getRes());
        } else {
            SimpsonMethod simpsonMethod = new SimpsonMethod();

            Result res = simpsonMethod.compute(left, right, n, epsilon, expression);

            if (res != null)
                System.out.println("Метод Симпсона отработал за " + res.getN()
                        + " разбиений с результатом " + res.getRes());
        }
    }
}
