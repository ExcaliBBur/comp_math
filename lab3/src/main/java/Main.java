import CustomMath.Limits;
import IOlibrary.Input;
import exceptions.NoLimitException;
import expression.Answer;
import expression.Expression;
import expression.Result;
import methods.*;


public class Main {
    public static void main(String[] args) {

        final int n = 4;
        Input input = new Input();

        System.out.println("1: (x^2) dx ");
        System.out.println("2: (sin(x)) dx");
        System.out.println("3: (1 / sqrt(x)) dx");
        System.out.println("4: (1 / x^2) dx");
        System.out.println("5: (1 / (1 - x)) dx");

        int numberOfExpression = input.getNumber(false);
        double left = input.getBound(true);
        double right = input.getBound(false);

        System.out.println("\n1: ����� ��������������� (3 �����������: �����, ������, �������)");
        System.out.println("2: ����� ��������");
        System.out.println("3: ����� ��������");
        int numberOfMethod = input.getNumber(true);
        double epsilon = input.getEpsilon();

        Expression expression = new Expression(numberOfExpression);
        int modificationOfMethod = 0;
        if (numberOfMethod == 1) modificationOfMethod = input.getModification();

        Answer answer = new Answer(numberOfMethod, modificationOfMethod, left, right, n, epsilon, expression);
        Result result = null;

        if (Limits.limit(expression, left, "������� � ����� A �� ����������") == null) {
            result = answer.getAnswerForBreaks(false);
        }
        else if (Limits.limit(expression, right, "������� � ����� B �� ����������") == null) {
            result = answer.getAnswerForBreaks(true);
        }
        else {
            Double dot = Limits.limitOnInterval(expression, left, right);
            if (dot == null) {
                result = answer.getAnswer(left, right);
            }
            else {
                Result result1 = answer.getAnswer(left, dot - 0.00001);
                Result result2 = answer.getAnswer(dot + 0.00001, right);
                if (result1 != null && result2 != null) {
                    result.setRes(result1.getRes() + result2.getRes());
                    result.setN(result1.getN() + result2.getN());
                }
            }
        }

        if (result != null) answer.printAnswer(result);
    }
}
