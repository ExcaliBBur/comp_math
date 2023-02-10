public class Methods {
    private final double epsilon = 0.00000001d;

    public double[][] triangleMatrix(double[][] userMatrix) {
        printMatrix(userMatrix, -100);
        for (int i = 0; i < userMatrix[0].length - 1; i++) { //строка
            int pointer = 0;
            double max = Double.MIN_VALUE;
            for (int j = i; j < userMatrix.length; j++) { //столбец
                if (Math.abs(max) < Math.abs(userMatrix[j][i])) {
                    max = userMatrix[j][i];
                    pointer = j;
                }
            }
            if (Math.abs(max) <= epsilon) {
                System.out.println("Максимальный элемент слишком мал, метод Гаусса не подходит.");
                return null;
            }
            System.out.printf("Максимальный по модулю элемент " + (i + 1) + " столбца равен %.2f \n", max);

            double[] tmp = userMatrix[i];
            if (pointer != i) {
                userMatrix[i] = userMatrix[pointer];
                userMatrix[pointer] = tmp;
                System.out.println("Матрица после перестановки " + (i + 1) + " и " + (pointer + 1) + " строк");
                printMatrix(userMatrix, -100);
            } else System.out.println("Матрица не требует перестановки");

            for (int j = i + 1; j < userMatrix.length; j++) {
                double koeff = userMatrix[j][i] / userMatrix[i][i];
                for (int k = i; k < userMatrix[0].length; k++) {
                    //преобразование
                    userMatrix[j][k] = userMatrix[i][k] * koeff - userMatrix[j][k];
                }
            }
            if (i != userMatrix.length - 2) {
                System.out.println("Матрица после преобразования");
                printMatrix(userMatrix, i);
            }
            System.out.println();
        }
        return userMatrix;
    }

    public double[] rootMatrix(double[][] matrix) {
        double[] roots = new double[matrix.length];
        for (int i = matrix.length - 1; i >= 0; i--) {
            double answ = matrix[i][matrix[0].length - 1];
            for (int j = matrix.length - 1; j >= i; j--) {
                answ = answ - matrix[i][j] * roots[j];
            }
            roots[i] = answ / matrix[i][i];
        }
        return roots;
    }

    public double detMatrix(double[][] triangleMatrix) {
        //работает только с треугольной матрицей
        double det = 1;
        for (int i = 0; i < triangleMatrix.length; i++) det *= triangleMatrix[i][i];
        return det;
    }

    public double[] discrepancyMatrix(double[][] matrix, double[] roots) {
        double[] discrepancies = new double[matrix.length];
        for (int i = 0; i < matrix.length; i++) {
            double discrepancy = matrix[i][matrix[0].length - 1];
            for (int j = 0; j < matrix.length; j++) {
                discrepancy -= matrix[i][j] * roots[j];
            }
            discrepancies[i] = discrepancy;
        }
        return discrepancies;
    }

    private void printMatrix(double[][] matrix, int delimeter) {
        for (int i = 0; i < matrix.length; i++) {
            //красивый вывод
            //параметр смещения из-за знака "|"
            boolean isBeautiful = false;
            if (i == delimeter + 1) {
                for (int k = 0; k < matrix[0].length; k++) {
                    if (k == matrix[0].length - 1) System.out.printf("%6s", "------");
                    else if (k >= delimeter + 1) System.out.printf("%10s", "----------");
                    else {
                        if (!isBeautiful) {
                            System.out.printf("%14s", " ");
                            isBeautiful = true;
                        } else System.out.printf("%10s", " ");
                    }
                }
                System.out.println();
            }

            for (int j = 0; j < matrix[0].length; j++) {
                if (j == delimeter + 1 || j == matrix[0].length - 1) {
                    System.out.printf("%5s", "|");
                }
                System.out.printf("%10.2f", matrix[i][j]);
            }
            System.out.println();
        }
    }
}