

public class Heap {
    // リストはヒープデータ構造を表現しており、完全二分木の形
    private List<Integer> heap;

    public Heap() {
        // ArrayListインスタンスで初期化
        this.heap = new ArrayList<>();
    }

    // ヒープ内のデータを見る
    public List<Integer> getHeap() {
        return new ArrayList<>(heap);
    }

    private int leftChild(int index) {
        return 2 * index + 1;
    }

    private int rightChild(int index) {
        return 2 * index + 2;
    }

    // 親のノードを探す
    private int parent(int index) {
        return (index - 1) / 2;
    }

    //　仮にheap = [10, 20, 30, 40, 50]であるとする。
    private void swap(int index1, int index2) {
        // index1 = 1の時　temp = 20
        int temp = heap.get(index1);
        // index2 = 3の時、index 1の20を40へ置き換える。　heap=[10, 40, 30, 40, 50]
        heap.set(index1, heap.get(index2));
        // index2の要素を一時保存した値temp = 20 に置き換え。  heap=[10, 40, 30, 20, 50]
        heap.set(index2, temp);
    }


    public void insert(int value) {
        // 配列の最後にvalueを追加後、配列に合わせて-1して追加した値にcurrentインデックスをつける。
        heap.add(value);
        int current = heap.size() - 1;

        // currentインデックスが0以上(root出ない場合)　・　currentインデックスにあるvalueがparentより大きい場合ループする。
        while (current > 0　&& heap.get(current) > heap.get(parent(current))) {
            swap(current, parent(current));
            // swapされたらaddしたvalueをインデックスで追跡。
            current = parent(current);
        }
    }

    public void sinkDown(int index) {
        int maxIndex = index;
        while (true) {
            int leftIndex = leftChild(index);
            int rightIndex = rightChild(index);

            if (leftIndex < heap.size() && heap.get(leftIndex) > heap.get(maxIndex)) {
                maxIndex = leftIndex;
            }
            if (rightIndex < heap.size() && heap.get(rightIndex) > heap.get(maxIndex)) {
                maxIndex = rightIndex;
            }

            if (maxIndex != index) {
                swap(index, maxIndex);
                index = maxIndex;
            }else {
                return;
            }
        }
    }

    //　ルートの削除
    public Integer remove() {
        if (heap.size() == 0){
            return null;
        }
        if (heap.size() == 1){
            return heap.remove(0);
        }

        // root(最も大きい数)を取得
        int maxValue = heap.get(0);
        // ヒープの最後の要素をルートに移動
        heap.set(0, heap.get(heap.size() - 1));
        heap.remove(heap.size() - 1); // 最後の要素を削除
        sinkDown(0);
        return maxValue;
    }


}

