package methods;

import expression.Expression;
import expression.Result;
import interfaces.Method;

public class TrapezoidalMethod implements Method {
    private final RungeRule rule = new RungeRule();
    private final int k = 2;


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
            res1 = (expression.F().calculate(left) + expression.F().calculate(right)) / 2;
            res2 = res1;
            double ptr = h;
            for (int i = 1; i <= n - 1; i++) {
                res1 += expression.F().calculate(left + ptr);
                ptr += h;
            }
            res1 *= h;
            ptr = 0;
            for (int i = 1; i <= 2 * n - 1; i++) {
                res2 += expression.F().calculate(left + ptr);
                ptr += h_1;
            }
            res2 *= h_1;
            if (rule.isPerformed(res1, res2, k, epsilon)) break;
            else if (counter >= MAX_ITERATIONS) {
                System.out.println("Метод трапеций не смог отработать за " + MAX_ITERATIONS + " итераций");
                return null;
            }
            n *= 2;
        }
        return new Result(res1, n);
    }

}
