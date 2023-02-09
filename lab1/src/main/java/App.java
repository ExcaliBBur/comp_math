import java.io.IOException;

public class App {
    public static void main(String[] args) throws IOException {
        Methods methods = new Methods();
        Input input = new Input();
        boolean isConsole = input.checkInputType();
        double[][] matrix;
        if (isConsole) {
            int n = input.sizeOfConsoleMatrix();
            matrix = input.inputConsoleMatrix(n);
        } else {
            System.out.println("Перед тем как начать, советуем посмотреть примеры ввода матриц в файлах \"test*\"");
            input.setInputFileName(input.getInputFileName());
            matrix = input.inputFileMatrix();
        }
        if (matrix == null) return;

        if (methods.triangleMatrix(matrix) == null) return;

        for (int i = 0; i < matrix[0].length * 10 + 5; i++) System.out.print("-");
        System.out.println();

        double det = methods.detMatrix(matrix);
        System.out.printf("Определитель матрицы равен %.5f \n", det);

        if (det == 0) System.out.println("Система имеет бесконечное множество решений");
        else {
            System.out.println("Вектор неизвестных: ");
            double[] roots = methods.rootMatrix(matrix);
            int counter = 1;
            for (double root : roots) {
                String ending = ", ";
                if (counter == roots.length) ending = ". ";
                System.out.printf("x%d = %.3f%s", counter++, root, ending);
            }
            counter = 1;
            System.out.println("\nВектор невязок: ");
            double[] discrepancies = methods.discrepancyMatrix(matrix, roots);
            for (double discrepancy : discrepancies) {
                String ending = ", ";
                if (counter == discrepancies.length) ending = ". ";
                System.out.printf("r%d = %.30f%s", counter++, discrepancy, ending);
            }
        }
    }
}