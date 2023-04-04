package interfaces;

import expression.Expression;
import expression.Result;

public interface Method {
    public Result compute(double left, double right, double n, double epsilon, Expression expression);
    public final int MAX_ITERATIONS = 30;
}
