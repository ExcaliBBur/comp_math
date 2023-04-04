package expression;

import methods.*;

public class Answer {
    private final static int PRECISION = 100;
    private final int numberOfMethod;
    private final int modificationOfMethod;
    private final double left;
    private final double right;
    private final int n;
    private final double epsilon;
    private final Expression expression;

    public Answer(int numberOfMethod, int modificationOfMethod, double left, double right, int n, double epsilon, Expression expression) {
        this.numberOfMethod = numberOfMethod;
        this.modificationOfMethod = modificationOfMethod;
        this.left = left;
        this.right = right;
        this.n = n;
        this.epsilon = epsilon;
        this.expression = expression;
    }

    public Result getAnswer(double left, double right) {
        if (numberOfMethod == 1) {
            switch (modificationOfMethod) {
                case (1) -> {
                    LeftRectangleMethod leftRectangleMethod = new LeftRectangleMethod();

                    return leftRectangleMethod.compute(left, right, n, epsilon, expression);
                }
                case (2) -> {
                    RightRectangleMethod rightRectangleMethod = new RightRectangleMethod();

                    return rightRectangleMethod.compute(left, right, n, epsilon, expression);
                }
                case (3) -> {
                    MidRectangleMethod midRectangleMethod = new MidRectangleMethod();

                    return midRectangleMethod.compute(left, right, n, epsilon, expression);
                }
            }
        } else if (numberOfMethod == 2) {
            TrapezoidalMethod trapezoidalMethod = new TrapezoidalMethod();

            return trapezoidalMethod.compute(left, right, n, epsilon, expression);
        } else {
            SimpsonMethod simpsonMethod = new SimpsonMethod();

            return simpsonMethod.compute(left, right, n, epsilon, expression);
        }
        return null;
    }

    public Result getAnswerForBreaks(boolean type) {
        double prev;
        Result current = new Result();
        int k = 0;
        do {
            prev = current.getRes();
            if (type) {
                current = getAnswer(left, right - (0.1 / Math.pow(10, k++)));
            }
            else {
                current = getAnswer(left + (0.1 / Math.pow(10, k++)), right);
            }

        } while (current != null && (Math.abs(current.getRes() - prev) >= epsilon
                && !Double.isNaN(current.getRes()) && k != PRECISION));

        return current != null && Double.isFinite(current.getRes()) ? current : null;
    }


    public void printAnswer(Result result) {
        if (numberOfMethod == 1) {
            switch (modificationOfMethod) {
                case (1) -> {
                    if (result != null)
                        System.out.println("Метод левых треугольников отработал за " + result.getN()
                                + " разбиений с результатом " + result.getRes());
                }
                case (2) -> {
                    if (result != null)
                        System.out.println("Метод правых треугольников отработал за " + result.getN()
                                + " разбиений с результатом " + result.getRes());
                }
                case (3) -> {
                    if (result != null)
                        System.out.println("Метод средних треугольников отработал за " + result.getN()
                                + " разбиений с результатом " + result.getRes());
                }
            }
        } else if (numberOfMethod == 2) {
            if (result != null)
                System.out.println("Метод трапеций отработал за " + result.getN()
                        + " разбиений с результатом " + result.getRes());
        } else {
            if (result != null)
                System.out.println("Метод Симпсона отработал за " + result.getN()
                        + " разбиений с результатом " + result.getRes());
        }
    }
}
