package methods;

import expression.Expression;
import expression.Result;
import interfaces.Method;

public class SimpsonMethod implements Method {
    private final RungeRule rule = new RungeRule();
    private final int k = 4;


    @Override
    public Result compute(double left, double right, double n, double epsilon, Expression expression) {
        double h;
        double h_1;
        double res1;
        double res2;
        int counter = 0;
        while (true) {
            counter++;
            h = (right - left) / n;
            h_1 = h / 2;
            res1 = (expression.F().calculate(left) + expression.F().calculate(right));
            res2 = res1;
            double ptr = h;
            for (int i = 1; i <= n - 1; i++) {
                if (i % 2 != 0) res1 += 4 * expression.F().calculate(left + ptr);
                else res1 += 2 * expression.F().calculate(left + ptr);
                ptr += h;
            }
            res1 *= h / 3;
            if (Double.isInfinite(res1) || Double.isNaN(res1) || Math.abs(res1) >= 10000) {
                System.out.println("Интеграл не существует.");
                return null;
            }
            ptr = 0;
            for (int i = 1; i <= 2 * n - 1; i++) {
                if (i % 2 != 0) res2 += 4 * expression.F().calculate(left + ptr);
                else res2 += 2 * expression.F().calculate(left + ptr);
                ptr += h_1;
            }
            res2 *= h_1 / 3;
            if (rule.isPerformed(res1, res2, k, epsilon)) break;
            else if (counter >= MAX_ITERATIONS) {
                System.out.println("Метод Симпсона не смог отработать за " + MAX_ITERATIONS + " итераций");
                return null;
            }
            n *= 2;
        }
        return new Result(res1, n);
    }

}
