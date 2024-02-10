public class BinarySearchTree {

    private Node root;

    public static class Node {
        public int value;
        public Node left;
        public Node right;

        private Node(int value) {
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
        while (true) {
            if (newNode.value == temp.value) return false;
            if (newNode.value < temp.value) {
                if (temp.left == null) {
                    temp.left = newNode;
                    return true;
                }
                temp = temp.left;
            } else {
                if (temp.right == null) {
                    temp.right = newNode;
                    return true;
                }
                temp = temp.right;
            }
        }
    }

    public boolean contains(int value) {
        if (root == null) return false;
        Node temp = root;
        while (temp != null) {
            if (value < temp.value) {
                temp = temp.left;
            } else if (value > temp.value) {
                temp = temp.right;
            } else {
                return true;
            }
        }
        return false;
    }


    // callstack
    private boolean rContains(Node currnetNode, int value) {
        if (currentNode == null) return false;

        // 現在のノード（currentNode）の値が検索している値（value）に等しければtrue
        if(currentNode.value == value) return true;

        if(value < currentNode.value) {
            return rContains(currentNode.left, value);
        }　else {
            return rContains(currentNode.right, value);
        }
    }


    //オーバーロード
    public boolean rContains(int value) { return rContains(root, value); }



    private Node rInsert(Node currentNode, int value) {
        // ベースケース　（リーフノードに到達したか、treeが空である場合）
        if (currentNode == null) return new Node(value);

        if (value < currentNode.value) {
            // newされたノードを左のツリーにおく。(元々はnull)
            currentNode.left = rInsert(currentNode.left, value);
        } else if (value > currentNode.value) {
            currentNode.right = rInsert(currentNode.right, value);
        }
        return currentNode;
    }

    public void rInsert(int value) {
        if (root == null) root = new Node(value);
        rInsert(root, value)
    }




    public int minValue(Node currentNode) {
        // 左の子ノードがnullになるまで左側に移動
        while (currentNode.left != null) {
            currentNode = currentNode.left;
        }
        return currentNode.value;
    }

    private Node deleteNode(Node currentNode, int value){
        if (currentNode == null) return null;

        // 値が現在のノードの値より小さい場合: 左の子ノードを起点として削除操作を再帰的に続行
        if (value < currentNode.value) {
            currentNode.left = deleteNode(currentNode.left, value);
        // 値が現在のノードの値より大きい場合: 右の子ノードを起点として削除操作を再帰的に続行
        } else if (value > currentNode.value) {
            currentNode.right = deleteNode(currentNode.right, value);

        } else {
            // 葉ノード（子ノードがない）: 直接削除。
            if (currentNode.left == null && currentNode.right == null) return null;

            // 一つの子ノードを持つノード: 子ノードを親ノードに接続。
            else if (currentNode.left == null) {
                // 左の子ノードが存在しないので、currentNodeの右の子ノードがcurrentNodeの親ノードに直接接続
                currentNode = currentNode.right;
            } else if (currentNode.right == null) {
                // // 削除されるノードに右の子ノードが存在しないので、左の子ノードがcurrentNodeの親ノードに直接接続
                currentNode = currentNode.left;

            } else {
                // 二つの子ノードを持つノード: 右部分木の最小値を持つノードを見つけ、削除したいノードの値をその最小値で置き換え
                int subTreeMin = minValue(currentNode.right);
                // 右のノードにある最小値をcurrentNodeのvalueに書き換える。
                currentNode.value = subTreeMin;
                currentNode.right = deleteNode(currentNode.right, subTreeMin);
            }
        }
        return currentNode;
    }

    public void deleteNode(int value) {
        deleteNode(root, value);
    }
}
