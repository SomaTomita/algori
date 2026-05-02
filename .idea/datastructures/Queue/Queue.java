package datastructures.Queue;

public class Queue {

    class Node {
        int value;
        Node next;

        Node(int value) {
            this.value = value;
        }
    }


    private Node first;
    private Node last;
    private int length;

    public Queue(int value) {
        Node newNode = new Node(value);
        first = newNode;
        last = newNode;
        length = 1;
    }



    public Node getFirst() {
        return first;
    }

    public Node getLast() {
        return last;
    }

    public int getLength() {
        return length;
    }

    public void printList() {
        Node temp = first;
        while (temp != null) {
            System.out.println(temp.value);
            temp = temp.next;
        }
    }

    public void printAll() {
        if (length == 0) {
            System.out.println("First: null");
            System.out.println("Last: null");
        } else {
            System.out.println("First: " + first.value);
            System.out.println("Last: " + last.value);
        }
        System.out.println("Length:" + length);
        System.out.println("\nQueue:");
        if (length == 0) {
            System.out.println("empty");
        } else {
            printList();
        }
    }

    public void makeEmpty() {
        first = null;
        last = null;
        length = 0;
    }



    // 末尾(last)に新ノードを繋いで last を更新 (FIFO の "in")
    public void enqueue(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            // 空キューなら first/last を同じノードに
            first = newNode;
            last = newNode;
        } else {
            last.next = newNode;
            last = newNode;
        }
        length++;
    }

    // 先頭(first)を取り出して first を 1 つ進める (FIFO の "out")
    public Node dequeue() {
        if (length == 0) return null;
        Node temp = first;
        if (length == 1) {
            // 唯一のノードを取ったら空キュー
            first = null;
            last = null;
        } else {
            first = first.next;
            // 取り出したノードを残りのキューから切り離す
            temp.next = null;
        }
        length--;
        return temp;
    }
}
