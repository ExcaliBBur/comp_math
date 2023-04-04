package expression;

import interfaces.FuncExpression;

public class Expression {
    private int numExpression;

    public Expression(int numExpression) {
        this.numExpression = numExpression;
    }

    public int getNumExpression() {
        return numExpression;
    }

    public FuncExpression F() {
        return switch (numExpression) {
            case (1) -> (x) -> (x * x);
            case (2) -> (x) -> Math.sin(x);
            case (3) -> (x) -> 1 / Math.sqrt(x);
            case (4) -> (x) -> 1 / (x * x);
            case (5) -> (x) -> (1) / (1 - x);
            default -> null;
        };
    }
    public FuncExpression Integral() {
        return switch (numExpression) {
            case (1) -> (x) -> (x * x * x) / (3);
            case (2) -> (x) -> -Math.cos(x);
            case (3) -> (x) -> 2 * Math.sqrt(x);
            case (4) -> (x) -> -1 / x;
            case (5) -> (x) -> -Math.log(1 - x);
            default -> null;
        };
    }
}
