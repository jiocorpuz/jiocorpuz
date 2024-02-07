import java.util.Scanner;
import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class StackQueue {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        while (!exit) {
            System.out.println("Choose an option:");
            System.out.println("1. Stack");
            System.out.println("2. Queue");
            System.out.println("3. Exit");

            int option = scanner.nextInt();

            switch (option) {
                case 1:
                    // Stack implementation
                    Stack<Integer> stack = new Stack<>();

                    System.out.println("Enter the number of elements to push onto the stack:");
                    int numElements = scanner.nextInt();

                    System.out.println("Enter the elements:");

                    for (int i = 0; i < numElements; i++) {
                        int element = scanner.nextInt();
                        stack.push(element);
                    }

                    boolean stackExit = false;

                    while (!stackExit) {
                        System.out.println("Choose an operation:");
                        System.out.println("1. Pop an element");
                        System.out.println("2. Print the stack");
                        System.out.println("3. Return to options");

                        int operation = scanner.nextInt();

                        switch (operation) {
                            case 1:
                                if (!stack.isEmpty()) {
                                    int poppedElement = stack.pop();
                                    System.out.println("Popped element: " + poppedElement);
                                } else {
                                    System.out.println("Stack is empty!");
                                }
                                break;

                            case 2:
                                System.out.println("Stack elements:");

                                for (int i = stack.size() - 1; i >= 0; i--) {
                                    System.out.println(stack.get(i));
                                }
                                break;

                            case 3:
                                stackExit = true;
                                break;

                            default:
                                System.out.println("Invalid operation!");
                                break;
                        }
                    }

                    break;

                case 2:
                    // Queue implementation
                    Queue<Integer> queue = new LinkedList<>();

                    System.out.println("Enter the number of elements to add to the queue:");
                    numElements = scanner.nextInt();

                    System.out.println("Enter the elements:");

                    for (int i = 0; i < numElements; i++) {
                        int element = scanner.nextInt();
                        queue.add(element);
                    }

                    boolean queueExit = false;

                    while (!queueExit) {
                        System.out.println("Choose an operation:");
                        System.out.println("1. Dequeue an element");
                        System.out.println("2. Print the queue");
                        System.out.println("3. Return to options");

                        int operation = scanner.nextInt();

                        switch (operation) {
                            case 1:
                                if (!queue.isEmpty()) {
                                    int dequeuedElement = queue.remove();
                                    System.out.println("Dequeued element: " + dequeuedElement);
                                } else {
                                    System.out.println("Queue is empty!");
                                }
                                break;

                            case 2:
                                System.out.println("Queue elements:");

                                for (int element : queue) {
                                    System.out.println(element);
                                }
                                break;

                            case 3:
                                queueExit = true;
                                break;

                            default:
                                System.out.println("Invalid operation!");
                                break;
                        }
                    }

                    break;

                case 3:
                    exit = true;
                    break;

                default:
                    System.out.println("Invalid option!");
                    break;
            }
        }

        scanner.close();
    }
}
