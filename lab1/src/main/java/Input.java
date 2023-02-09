import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;

public class Input {
    private final Scanner scanner = new Scanner(System.in);
    private String fileName;

    //Проверяем через что производится ввод
    public boolean checkInputType() {
        System.out.println("Вы хотите ввести матрицу через консоль или через файл? " +
                "1 - консоль, 2 - файл.");
        boolean isConsole = false;
        try {
            int num = Integer.parseInt(scanner.next());
            if (num == 1) isConsole = true;
        } catch (Exception e) {
            System.out.println("Ошибка: неправильный формат ввода");
            checkInputType();
        }
        return isConsole;
    }

    //Ввод матрицы из консоли
    public double[][] inputConsoleMatrix(int length) {
        System.out.println("Введите расширенную матрицу: ");
        double[][] matrix = new double[length][length + 1];
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < length + 1; j++) {
                try {
                    matrix[i][j] = Double.parseDouble(scanner.next().replaceAll(",", "."));
                } catch (Exception e) {
                    System.out.println("Произошла ошибка при считывании коэффициента, начинаем заново...");
                    inputConsoleMatrix(length);
                }
            }
        }
        return matrix;
    }

    //Размер матрицы из консоли
    public int sizeOfConsoleMatrix() {
        System.out.println("Введите размерность матрицы: ");
        int n = 0;
        try {
            int length = Integer.parseInt(scanner.next());
            if (length > 20) {
                System.out.println("Ошибка: размерность матрицы должна быть не больше 20!");
                sizeOfConsoleMatrix();
            }
            if (length < 2) {
                System.out.println("Ошибка: размерность матрицы должна быть не менее 2!");
                sizeOfConsoleMatrix();
            }
            n = length;
        } catch (Exception e) {
            System.out.println("Произошла ошибка при чтении размерности, повторяем ввод...");
            sizeOfConsoleMatrix();
        }
        return n;
    }

    //Получаем имя файла
    public String getInputFileName() {
        System.out.println("Введите название файла: ");
        return scanner.next();
    }

    //Устанавливаем имя файла
    public void setInputFileName(String fileName) {
        this.fileName = fileName;
    }

    //Получаем матрицу из файла
    public double[][] inputFileMatrix() throws IOException {
        File file = new File(fileName);
        double[][] matrix;
        while (!file.exists()) {
            System.out.println("Такого файла не существует :( Пробуем считать название заново");
            setInputFileName(getInputFileName());
            file = new File(fileName);
        }
        if (!file.canRead()) {
            System.out.println("Невозможно чтение из этого файла, возможно, нет необходимых прав доступа");
            return null;
        }

        BufferedReader reader = new BufferedReader(new FileReader(file));
        try {
            String[] line = reader.readLine().split(" ");
            if (line.length > 1) {
                System.out.println("Неправильный формат ввода из файла! " +
                        "На первой строчке должна быть только размерность матрицы");
                reader.close();
                return null;
            }
            int n = Integer.parseInt(line[0]);
            if (n > 20) {
                System.out.println("Ошибка: размерность матрицы должна быть не больше 20!");
                return null;
            }
            if (n < 2) {
                System.out.println("Ошибка: размерность матрицы должна быть не менее 2!");
                return null;
            }

            matrix = new double[n][n + 1];
            for (int i = 0; i < n; i++) {
                String[] currentLine = reader.readLine().replace(",", ".").split(" ");
                for (int j = 0; j < n + 1; j++)
                    try {
                        matrix[i][j] = Double.parseDouble(currentLine[j]);
                    } catch (Exception e) {
                        System.out.println("Неправильный формат ввода из файла! " +
                                "Проверьте файл на наличие лишних пробелов или пустых строк");
                        reader.close();
                        return null;
                    }
            }
            System.out.println("Чтение из файла произошло успешно.");
            reader.close();
            return matrix;
        } catch (NullPointerException e) {
            System.out.println("Файл пустой");
            return null;
        }
    }
}