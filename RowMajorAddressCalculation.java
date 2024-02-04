import java.util.Scanner;

public class RowMajorAddressCalculation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the number of dimensions: ");
        int dimensions = scanner.nextInt();

        int[] upperBounds = new int[dimensions];

        // Get the upper bounds for each dimension
        for (int i = 0; i < dimensions; i++) {
            System.out.print("Enter the upper bound for dimension " + i + ": ");
            upperBounds[i] = scanner.nextInt();
        }

        // Prompt the user to enter the indices for the element
        int[] indices = new int[dimensions];
        for (int i = 0; i < dimensions; i++) {
            System.out.print("Enter the index for dimension " + i + ": ");
            indices[i] = scanner.nextInt();
        }

        // Calculate the memory address of the element
        long address = calculateAddress(indices, upperBounds);

        System.out.println("Memory address of the element: " + address);
    }

    public static long calculateAddress(int[] indices, int[] upperBounds) {
        int dimensions = indices.length;
        int[] multipliers = new int[dimensions];

        // Calculate the multipliers for each dimension
        multipliers[dimensions - 1] = 1;
        for (int i = dimensions - 2; i >= 0; i--) {
            multipliers[i] = multipliers[i + 1] * upperBounds[i + 1];
        }

        // Calculate the memory address using the row-major formula
        long address = 0;
        for (int i = 0; i < dimensions; i++) {
            address += indices[i] * multipliers[i];
        }

        return address;
    }
}
