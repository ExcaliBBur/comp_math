package expression;

public class Result {
    private final double res;
    private final double n;

    public Result(double res, double n) {
        this.res = res;
        this.n = n;
    }

    public double getN() {
        return n;
    }

    public double getRes() {
        return res;
    }
}
