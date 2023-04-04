package methods;

public class RungeRule {
    public boolean isPerformed(double I_h, double I_h2, int k, double epsilon) {
        return (Math.abs(I_h2 - I_h)) / (Math.pow(2, k) - 1) <= epsilon;
    }
}
