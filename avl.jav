import java.util.Scanner;

class Node {
    int key, height;
    Node left, right;

    Node(int d) {
        key = d;
        height = 1;
    }
}

class AVLTree {
    Node root;

    int height(Node N) {
        if (N == null)
            return 0;
        return N.height;
    }

    int max(int a, int b) {
        return (a > b) ? a : b;
    }

    Node rightRotate(Node y) {
        Node x = y.left;
        Node T2 = x.right;

        x.right = y;
        y.left = T2;

        y.height = max(height(y.left), height(y.right)) + 1;
        x.height = max(height(x.left), height(x.right)) + 1;

        return x;
    }

    Node leftRotate(Node x) {
        Node y = x.right;
        Node T2 = y.left;

        y.left = x;
        x.right = T2;

        x.height = max(height(x.left), height(x.right)) + 1;
        y.height = max(height(y.left), height(y.right)) + 1;

        return y;
    }

    int getBalance(Node N) {
        if (N == null)
            return 0;
        return height(N.left) - height(N.right);
    }

    Node insert(Node node, int key) {
        if (node == null)
            return (new Node(key));

        if (key < node.key)
            node.left = insert(node.left, key);
        else if (key > node.key)
            node.right = insert(node.right, key);
        else
            return node;

        node.height = 1 + max(height(node.left), height(node.right));

        int balance = getBalance(node);

        if (balance > 1 && key < node.left.key)
            return rightRotate(node);

        if (balance < -1 && key > node.right.key)
            return leftRotate(node);

        if (balance > 1 && key > node.left.key) {
            node.left = leftRotate(node.left);
            return rightRotate(node);
        }

        if (balance < -1 && key < node.right.key) {
            node.right = rightRotate(node.right);
            return leftRotate(node);
        }

        return node;
    }

    Node minValueNode(Node node) {
        Node current = node;

        while (current.left != null)
            current = current.left;

        return current;
    }

    Node deleteNode(Node root, int key) {
        if (root == null)
            return root;

        if (key < root.key)
            root.left = deleteNode(root.left, key);
        else if (key > root.key)
            root.right = deleteNode(root.right, key);
        else {
            if ((root.left == null) || (root.right == null)) {
                Node temp = null;
                if (temp == root.left)
                    temp = root.right;
                else
                    temp = root.left;

                if (temp == null) {
                    temp = root;
                    root = null;
                } else
                    root = temp;
            } else {
                Node temp = minValueNode(root.right);
                root.key = temp.key;
                root.right = deleteNode(root.right, temp.key);
            }
        }

        if (root == null)
            return root;

        root.height = max(height(root.left), height(root.right)) + 1;

        int balance = getBalance(root);

        if (balance > 1 && getBalance(root.left) >= 0)
            return rightRotate(root);

        if (balance > 1 && getBalance(root.left) < 0) {
            root.left = leftRotate(root.left);
            return rightRotate(root);
        }

        if (balance < -1 && getBalance(root.right) <= 0)
            return leftRotate(root);

        if (balance < -1 && getBalance(root.right) > 0) {
            root.right = rightRotate(root.right);
            return leftRotate(root);
        }

        return root;
    }

    void preOrder(Node node) {
        if (node != null) {
            System.out.print(node.key + " ");
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.print(node.key + " ");
            inOrder(node.right);
        }
    }

    void postOrder(Node node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            System.out.print(node.key + " ");
        }
    }

    void printArray(Node node, int index, int[] arr) {
        if (node != null) {
            arr[index] = node.key;
            printArray(node.left, 2 * index + 1, arr);
            printArray(node.right, 2 * index + 2, arr);
        }
    }

    void printArrayRepresentation(Node node) {

        if (node == null) {
            System.out.println("The tree is empty. There are no elements to print.");
            return;
        }
        
        int height = root.height;
        int size = (int) Math.pow(2, height) - 1;

        int[] arr = new int[size];
        printArray(node, 0, arr);

        for (int i = 0; i < size; i++) {
            if (arr[i] != 0)
                System.out.print(arr[i] + " ");
            else
                System.out.print("0 ");
        }
    }

    void clear(Node node) {
        if (node == null) return;

        clear(node.left);
        clear(node.right);

        node = null;
    }

    void clearTree() {
        clear(root);
        root = null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        AVLTree tree = new AVLTree();

        boolean restart = true;
        while (restart) {
            boolean continueLoop = true;
            while (continueLoop) {
                System.out.println("1. Insert a node");
                System.out.println("2. Delete a node");
                System.out.println("3. Display 1-D array representation");
                System.out.println("4. Display Preorder, Inorder, Postorder traversals");
                System.out.println("5. Restart AVL tree");
                System.out.println("6. Exit");

                System.out.print("Enter your choice: ");
                int choice = sc.nextInt();

                switch (choice) {
                    case 1:
                        System.out.print("Enter the value to be inserted: ");
                        int key = sc.nextInt();
                        tree.root = tree.insert(tree.root, key);
                        break;
                    case 2:
                        System.out.print("Enter the value to be deleted: ");
                        int deleteKey = sc.nextInt();
                        tree.root = tree.deleteNode(tree.root, deleteKey);
                        break;
                    case 3:
                    System.out.println("1-D array representation:");
                    tree.printArrayRepresentation(tree.root);
                    System.out.println();
                    break;
                case 4:
                    System.out.println("Preorder traversal:");
                    tree.preOrder(tree.root);
                    System.out.println();
                    System.out.println("Inorder traversal:");
                    tree.inOrder(tree.root);
                    System.out.println();
                    System.out.println("Postorder traversal:");
                    tree.postOrder(tree.root);
                    System.out.println();
                    break;
                case 5:
                    System.out.println("Restarting the AVL tree...");
                    tree.clearTree();
                    break;
                case 6:
                    System.out.println("Exiting the program...");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice");
            }

            System.out.print("Do you want to continue (yes/no)? ");
            String response = sc.next();
            if (response.equalsIgnoreCase("no")) {
                continueLoop = false;
            }
        }
    }
}
}
