package datastructures.Hash;

public class Hash {
    private int size = 7;
    private Node[] dataMap;


    public class Node {
        private String key;
        private int value;
        private Node next;

        public Node(String key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    public Hash() {
        dataMap = newNode[size];
    }

    // キーが"cat"の場合のhashメソッドの動作を考えてみよう。
    private int hash(String key) {
        int hash = 0;
        //  keyChars = ['c', 'a', 't']
        char[] keyChars = key.toCharArray();
//        ループ処理:
//        i=0: hash = (0 + 'c' * 23) % dataMap.length
//        i=1: hash = (hash + 'a' * 23) % dataMap.length
//        i=2: hash = (hash + 't' * 23) % dataMap.length
        for (int i = 0; i < keyChars.length; i++) {
            int asciiValue = keyChars[i];
            hash = (hash + asciiValue * 23) % dataMap.length;
        }
//        ハッシュ関数は、キーがどのような文字列であっても、一貫して同じインデックスを返す必要があります。（同じ入力に対しては同じ値が返ってくる）
//        また、異なるキーに対して可能な限り異なるインデックスを返すことで、
//        衝突（異なるキーが同じインデックスにマッピングされる状況）の可能性を減らすことが望まれます。
        return hash;
    }


    public void set(String key, int value) {
        int index = hash(key);
        Node newNode = new Node(key, value);
        // Node配列が空の場合、ハッシュindexにnewNodeを指す。
        if (dataMap[index] == null) {
            dataMap[index] = newNode;
        } else {
            // dataMap[index]はハッシュインデックスの位置にあるリンクリストの先頭ノードを指す。
            Node temp = dataMap[index];
            // リストの最後のノード（つまりtemp.nextがnullのノード）の一つ前まで実行。
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }


    public int get(String key) {
        int index = hash(key);
        // dataMap[index]はhashインデックスの位置にあるリンクリストの先頭ノードを指す。
        Node temp = dataMap[index];
        // tempがnullになるまで、つまりリストの最後まで繰り返す。
        while (temp != null) {
            if (temp.key == key) return temp.value;
            temp = temp.next;
        }
        return 0;
    }


    public ArrayList keys() {
        ArrayList<String> allKeys = new ArrayList<>();
        for (int i = 0; i < dataMap.length; i++) {
            Node temp = dataMap[i];
            while (temp != null) {
                allKeys.add(temp.key);
                temp = temp.next;
            }
        }
        return allKeys;
    }


}
