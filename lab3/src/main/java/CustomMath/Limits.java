package CustomMath;

import exceptions.NoLimitException;
import expression.Expression;

import java.text.DecimalFormat;

public class Limits {
    private static final int PRECISION = 10000;
    private static final double EPSILON = 0.00001;

    public static Double leftLimit(Expression expression, double x) {
        double round = x - EPSILON;
        double eval = 0d;
        double prev;
        int k = 0;

        do {
            prev = eval;
//            eval = expression.Integral().calculate(round);
            eval = expression.F().calculate(round);
            round = x - (0.1 / Math.pow(10, k++));
        } while (Math.abs(eval - prev) >= EPSILON && !Double.isNaN(eval) && k != PRECISION);

        return Double.isFinite(eval) ? eval : null;
    }

    public static Double rightLimit(Expression expression, double x) {
        double round = x + EPSILON;
        double eval = 0d;
        double prev;
        int k = 0;

        do {
            prev = eval;
//            eval = expression.Integral().calculate(round);
            eval = expression.F().calculate(round);
            round = x + (0.1 / Math.pow(10, k++));
        } while (Math.abs(eval - prev) >= EPSILON && !Double.isNaN(eval) && k != PRECISION);

        return Double.isFinite(eval) ? eval : null;
    }

    public static void limit(Expression expression, double x, String msg)
            throws NoLimitException {
        Double left = leftLimit(expression, x);
        Double right = rightLimit(expression, x);
        if (left == null || right == null) {
            throw new NoLimitException(msg);
        }
    }

    public static void limitOnInterval(Expression expression, double left, double right)
            throws NoLimitException {
        DecimalFormat df = new DecimalFormat("#.##");
        for (double i = left + 0.01; i < right; i += 0.01) {
            limit(expression, Double.parseDouble(df.format(i).replace(",", ".")),
                    "Функция терпит разрыв на интервале в точке " + df.format(i));
        }
    }
}
