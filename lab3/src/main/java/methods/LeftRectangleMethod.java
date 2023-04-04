package methods;

import expression.Expression;
import expression.Result;
import interfaces.Method;

public class LeftRectangleMethod implements Method {
    private final RungeRule rule = new RungeRule();
    private final int k = 1;

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
            res1 = 0;
            res2 = 0;
            double ptr = 0;
            for (int i = 1; i <= n; i++) {
                res1 += expression.F().calculate(left + ptr);
                ptr += h;
            }
            res1 *= h;
            ptr = 0;
            for (int i = 1; i <= 2 * n; i++) {
                res2 += expression.F().calculate(left + ptr);
                ptr += h_1;
            }
            res2 *= h_1;
            if (rule.isPerformed(res1, res2, k, epsilon)) break;
            else if (counter >= MAX_ITERATIONS) {
                System.out.println("����� ����� ��������������� �� ���� ���������� �� " + MAX_ITERATIONS + " ��������");
                return null;
            }
            n *= 2;
        }
        return new Result(res1, n);
    }

}
