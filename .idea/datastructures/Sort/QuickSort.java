import java.util.Arrays;


public class Main {

    private static void swap(int[] array, int firstIndex, int secondIndex) {
        int temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }


    public static int pivot(int[] array, int pivotIndex, int endIndex) {
        int swapIndex = pivotIndex;
        for (int i = pivotIndex + 1; i <= endIndex; i++) {
            // 基準値より小さい場合は、pivotの手前に持ってくる。
            if (array[i] < array[pivotIndex]) {
                swapIndex++;
                swap(array, swapIndex, i);
            }
        }
        swap(array, pivotIndex, swapIndex);

        return swapIndex;
    }


    public static void quickSortHelper(int[] array, int left, int right) {
        if (left < right) {
            int pivotIndex = pivot(array, left, right);
            // pivotから見て左側と右側で分ける。
            quickSortHelper(array, left, pivotIndex-1);
            quickSortHelper(array, pivotIndex+1, right);
        }
    }

    public static void quickSort(int[] array) {
        quickSortHelper(array, 0, array.length-1);
    }


    public static void main(String[] args) {

        int[] myArray = {4,6,1,7,3,2,5};

        int returnedIndex = pivot(myArray, 0, 6);

        System.out.println( "Returned Index: " + returnedIndex);

        System.out.println( Arrays.toString( myArray ) );

    }

}




//[3, 5, 2, 1, 4]の場合；
//ステップ1: 初期呼び出し
//quickSortHelperを配列全体に対して呼び出します。
//
//quickSortHelper([3, 5, 2, 1, 4], 0, 4)
//ステップ2: ピボットの選択
//最初のピボットとして配列の最初の要素3を選択します。ピボット関数pivotを使って、3を正しい位置に移動します。
//
//ピボットの3より小さい要素2と1が3の左側に移動します。
//ピボットの3より大きい要素5と4が3の右側に移動します。
//ピボット関数の実行後の配列は以下のようになります（3が正しい位置に移動）：
//
//[2, 1, 3, 5, 4]
//        3の新しいインデックス（ピボットインデックス）は2です。
//
//ステップ3: 左側のサブ配列のソート
//3の左側にあるサブ配列[2, 1]に対してquickSortHelperを再帰的に呼び出します。
//
//quickSortHelper([2, 1, 3, 5, 4], 0, 1)
//このサブ配列でピボットは2です。1が2の左側に移動します。サブ配列はすでに[1, 2]とソートされています。
//
//ステップ4: 右側のサブ配列のソート
//3の右側にあるサブ配列[5, 4]に対してquickSortHelperを再帰的に呼び出します。
//
//quickSortHelper([1, 2, 3, 5, 4], 3, 4)
//このサブ配列でピボットは5です。4が5の左側に移動します。サブ配列はすでに[4, 5]とソートされています。
//
