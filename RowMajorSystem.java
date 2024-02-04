import java.util.Scanner;

public class RowMajorSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of rows: ");
        int rows = scanner.nextInt();

        System.out.print("Enter the number of columns: ");
        int columns = scanner.nextInt();

        int[][] matrix = new int[rows][columns];

        // Populate the matrix with user input
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print("Enter element at position (" + i + ", " + j + "): ");
                matrix[i][j] = scanner.nextInt();
            }
        }

        // Calculate the base address of the matrix
        long baseAddress = getAddress(matrix);

        // Calculate the memory address of each element in the matrix
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                long elementAddress = baseAddress + (i * columns + j) * Integer.BYTES;

                System.out.println("Element at position (" + i + ", " + j + ") address: " + elementAddress);
            }
        }
    }

    public static long getAddress(int[][] matrix) {
        // Get the memory address of the matrix using the unsafe class (requires additional setup)
        // This is just a simplified example; in practice, obtaining the memory address in Java is not straightforward
        sun.misc.Unsafe unsafe = getUnsafeInstance();
        return unsafe.arrayBaseOffset(int[][].class);
    }

    public static sun.misc.Unsafe getUnsafeInstance() {
        try {
            java.lang.reflect.Field theUnsafe = sun.misc.Unsafe.class.getDeclaredField("theUnsafe");
            theUnsafe.setAccessible(true);
            return (sun.misc.Unsafe) theUnsafe.get(null);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}

