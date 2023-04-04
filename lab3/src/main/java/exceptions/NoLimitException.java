package exceptions;

public class NoLimitException extends Exception{
    private final String s;
    public NoLimitException(String s) {
        this.s = s;
    }
    public String toString() {
        return s;
    }
}
