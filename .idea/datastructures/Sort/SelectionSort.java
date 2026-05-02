package datastructures.Sort;

import java.util.Arrays;

public class SelectionSort {

    // 元の typo "selevctionSort" を selectionSort に修正
    public static void selectionSort(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int minIndex = i;
            // 一番最初の i を基準にi+1の j が minIndex を探す
            for (int j = i + 1; j < array.length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            // 自分自身が最小だった時は swap 不要 (無駄な代入を避ける)
            if (i != minIndex) {
                int temp = array[i];
                array[i] = array[minIndex];
                array[minIndex] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {64, 25, 12, 22, 11};
        selectionSort(arr);
        // 期待値: [11, 12, 22, 25, 64]
        System.out.println(Arrays.toString(arr));
    }
}
