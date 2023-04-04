package expression;

public class Result {
    private Double res;
    private Double n;

    public Result(Double res, Double n) {
        this.res = res;
        this.n = n;
    }

    public Result() {
        this.res = 0d;
        this.n = 0d;
    }
    public void setN(Double n) {
        this.n = n;
    }

    public void setRes(Double res) {
        this.res = res;
    }

    public Double getN() {
        return n;
    }

    public Double getRes() {
        return res;
    }
}
