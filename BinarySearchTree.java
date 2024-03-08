import java.util.Scanner;

class Node {
    int data;
    Node left, right;

    public Node(int item) {
        data = item;
        left = right = null;
    }
}

class BinaryTree {
    Node root;

    public BinaryTree() {
        root = null;
    }

    public void insert(int data) {
        root = insertRec(root, data);
    }

    private Node insertRec(Node root, int data) {
        if (root == null) {
            root = new Node(data);
            return root;
        }

        if (data < root.data) {
            root.left = insertRec(root.left, data);
        } else if (data > root.data) {
            root.right = insertRec(root.right, data);
        }

        return root;
    }

    public void delete(int data) {
        root = deleteRec(root, data);
    }

    private Node deleteRec(Node root, int data) {
        if (root == null) return root;
    
        if (data < root.data) {
            root.left = deleteRec(root.left, data);
        } else if (data > root.data) {
            root.right = deleteRec(root.right, data);
        } else {
            if (root.left == null) {
                return root.right;
            } else if (root.right == null) {
                return root.left;
            }
    
            root.data = maxValue(root.left);
            root.left = deleteRec(root.left, root.data);
        }
    
        return root;
    }
    
    private int maxValue(Node root) {
        int maxv = root.data;
        while (root.right != null) {
            maxv = root.right.data;
            root = root.right;
        }
        return maxv;
    }
    

    public void inorder() {
        inorderRec(root);
        System.out.println();
    }

    private void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.data + " ");
            inorderRec(root.right);
        }
    }

    public void preorder() {
        preorderRec(root);
        System.out.println();
    }

    private void preorderRec(Node root) {
        if (root != null) {
            System.out.print(root.data + " ");
            preorderRec(root.left);
            preorderRec(root.right);
        }
    }

    public void postorder() {
        postorderRec(root);
        System.out.println();
    }

    private void postorderRec(Node root) {
        if (root != null) {
            postorderRec(root.left);
            postorderRec(root.right);
            System.out.print(root.data + " ");
        }
    }
}

public class BinarySearchTree {
    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Insert");
            System.out.println("2. Delete");
            System.out.println("3. Inorder traversal");
            System.out.println("4. Preorder traversal");
            System.out.println("5. Postorder traversal");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter the number to insert: ");
                    int numToInsert = scanner.nextInt();
                    tree.insert(numToInsert);
                    break;
                case 2:
                    System.out.print("Enter the number to delete: ");
                    int numToDelete = scanner.nextInt();
                    tree.delete(numToDelete);
                    break;
                case 3:
                    System.out.println("Inorder traversal:");
                    tree.inorder();
                    break;
                case 4:
                    System.out.println("Preorder traversal:");
                    tree.preorder();
                    break;
                case 5:
                    System.out.println("Postorder traversal:");
                    tree.postorder();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
