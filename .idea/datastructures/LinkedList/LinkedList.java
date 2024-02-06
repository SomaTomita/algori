package datastructures.LinkedList;

public class LinkedList {

    private Node head;
    private Node tail;
    private int length;


    class Node {
        int value;
        Node next;
        // コンストラクター newした(実体化した)時に出てくる。
        Node(int value) {
            this.value = value;
        }
    }


    public LinkedList(int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public Node getHead() {
        return head;
    }

    public Node getTail() {
        return tail;
    }

    public int getLength() {
        return length;
    }

    public void printList() {
        Node temp = head;
        while (temp != null) {
            System.out.println(temp.value);
            temp = temp.next;
        }
    }


    public void printAll() {
        if (length == 0) {
            System.out.println("Head: null");
            System.out.println("Tail: null");
        } else {
            System.out.println("Head: " + head.value);
            System.out.println("Tail: " + tail.value);
        }
        System.out.println("Length:" + length);
        System.out.println("\nLinked List:");
        if (length == 0) {
            System.out.println("empty");
        } else {
            printList();
        }
    }


    public void makeEmpty() {
        head = null;
        tail = null;
        length = 0;
    }

    // 新しいノードをリンクリストの末尾に追加
    public void append(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            //  リンクリストが空の場合、新しいノードがリストの最初
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        //        ノードの数の追跡(追加して一つ増えましたよ。)
        length++;
    }


    public Node removeLast() {
        if(length == 0) return null;
        Node temp = head;
        Node pre = head;
        while(temp.next != null) {
            pre  = temp;
            temp = temp.next;
        }
        //        tempだけが1つ先に言ってるので、preを最後に指定。
        tail = pre;
        //        1つ前(pre)からtempを指しているvalueと切り離す
        tail.next = null;
        length--;
        if (length == 0) {
            head = null;
            tail = null;
        }
        return temp;
    }


    public void prepend(int value) {
        Node newNode = new Node(value);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
        // 新しいnewNode = nullのところをリストのheadに結びつける。その後にnewNode(追加されたのを先頭に)をheadに置き換え。
            newNode.next = head;
            head = newNode;
        }
        length++;
    }


    public Node removeFirst() {
        if (length == 0)return null;
        Node temp = head;
        head = head.next;
        //        上記でheadを次に動かした後、最初を指しているtempをnextにいるheadから切り離す。
        temp.next = null;
        length--;
        if(length == 0) {
            tail = null;
        }
        //        リターンはどっかに持っていくイメージ
        return temp;
    }


    public Node get(int index) {
        if (index < 0 || index >= length) {
            return null;
        }
        //        tempを一番前に持ってくる
        Node temp = head;
        //        forループはi = 0から始まるので、例えばget(2)の場合、0が1回目のループ(→)、1が2回目のループ(→)で終了。0→1→2
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    public boolean set(int index, int value) {
        Node temp = get(index);
        if (temp != null) {
            //    indexで指定した現在のvalueを引数のvalueに変える。
            temp.value = value;
            // 操作の成功を表すtrue
            return true;
        }
        return false;
    }

    public boolean insert(int index, int value) {
        //　マイナスとリスト以上のいindex指定は弾く。
        if (index < 0 || index > length) return false;
        // リストの0番目(先頭)にinsertするなら
        if (index == 0) {
            prepend(value);
            return true;
        }
        // リストの最後にinsertするなら
        if (index == length) {
            append(value);
            return true;
        }
        // insertの引数のvalueを新しく作る。
        Node newNode = new Node(value);
        Node temp = get(index - 1);
        // 新しく作ったnewnodeの次の値をtemp(indexの一個前)の次の値とする。
        newNode.next = temp.next;
        temp.next = newNode;

        length++;
        return true;
    }

    public Node remove(int index) {
        if (index < 0 || index >= length) return null;
        if (index == 0) return removeFirst();
        if (index == length - 1) return removeLast();

        Node prev = get(index - 1);
        Node temp = prev.next;
        // tempは値を指している状態で、tempの次とprevの次を紐づける。
        prev.next = temp.next;
        temp.next = null;
        length--;
        return temp;
    }

    public void reverse() {
       Node temp = head;
       head = tail;
       tail = temp;
       Node after = temp.next;
       Node before = null;
       for (int i = 0; i < length; i++) {
           after = temp.next;
           // 矢印を逆に向けるイメージ
           temp.next = before;
           before = temp;
           temp = after;
       }
    }
}