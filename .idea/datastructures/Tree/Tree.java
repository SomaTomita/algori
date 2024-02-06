package datastructures.Tree;

public class Tree {

    private Node root;

    class Node {
        public int value;
        public Node left;
        public Node right;

        Node(int value) {
            this.value = value;
        }
    }

    public Node getRoot() {
        return root;
    }


    public boolean insert(int value) {
        Node newNode = new Node(value);
        if (root == null) {
            root = newNode;
            return true;
        }
        Node temp = root;
        // 条件がfalseにならない。
        while (true) {
            // もし数が一緒の時は追加できないので、弾く。
            if (newNode.value == temp.value) return false;

            if (newNode.value < temp.value) {
                if(temp.left == null) {
                    temp.left = newNode;
                    return true;
                }
                // もし左がnull出なかった時は、tempを日だしにづらす。
                temp = temp.left;
            } else {
                if (temp.next == null) {
                    temp.right = newNode;
                    return true;
                }
                temp = temp.right;
            }
        }
    }

}
