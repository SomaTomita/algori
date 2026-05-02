package datastructures.Sort.MergeSort;

import java.util.Arrays;

public class MergeSort {

    // 2 つのソート済み配列を 1 つのソート済み配列に統合する
    public static int[] merge(int[] array1, int[] array2) {
        int[] conbined = new int[array1.length + array2.length];
        int index = 0;
        int i = 0;
        int j = 0;

        // 両方とも残りがある間、先頭の小さい方を取って conbined に詰める
        while (i < array1.length && j < array2.length) {
            if (array1[i] < array2[j]) {
                conbined[index] = array1[i];
                index++;
                i++;
            } else {
                conbined[index] = array2[j];
                index++;
                j++;
            }
        }
        // どちらか(array1,2)に余った数をconbinedに入れていく。
        while (i < array1.length) {
            conbined[index] = array1[i];
            index++;
            i++;
        }
        while (j < array2.length) {
            conbined[index] = array2[j];
            index++;
            j++;
        }

        return conbined;
    }


    // 分割統治: 半分にして再帰、戻ってきたものを merge で統合
    public static int[] mergeSort(int[] array) {
        // ベースケース: 長さ 1 以下なら分割不能 (そのまま戻す)
        if (array.length <= 1) return array;

        int midIndex = array.length / 2;
        int[] left = mergeSort(Arrays.copyOfRange(array, 0, midIndex));
        int[] right = mergeSort(Arrays.copyOfRange(array, midIndex, array.length));

        return merge(left, right);
    }


    public static void main(String[] args) {
        int[] myArray = {3, 1, 4, 2};
        int[] sortedArray = mergeSort(myArray);

        // 元の myArray は変更されない (mergeSort は新しい配列を返すため)。
        // 旧 typo "orginalArray" を myArray に修正
        System.out.println("\nOriginal :" + Arrays.toString(myArray));
        System.out.println("\nSorted :" + Arrays.toString(sortedArray));
    }
}




// 配列 [3,1,4,2] をマージソートするプロセス：
// 初期配列 [3,1,4,2] は中央で [3,1] と [4,2] に分割されます。
//        [3,1] はさらに [3] と [1] に、[4,2] は [4] と [2] に分割されます。
// 各サブ配列は長さが1なので、それ以上分割できません。ここで再帰が終了し、マージのプロセスが開始されます。
//        [3] と [1] は [1,3] に、[4] と [2] は [2,4] にマージされます。
// 最後に、[1,3] と [2,4] がマージされて、最終的なソート済み配列 [1,2,3,4] が得られます。
