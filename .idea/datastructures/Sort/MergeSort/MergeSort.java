import java.util.Arrays;

public static int[] merge(int[] array1, int[] array2) {
    int[] conbined = new int[array1.length + array2.length];
    int index = 0;
    int i = 0;
    int j = 0;

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
    while(i < array1.length) {
        conbined[index] = array1[i];
        index++;
        i++;
    }
    while(j < array2.length) {
        conbined[index] = array2[j];
        index++;
        j++;
    }

    return conbined;
}


public static int[] mergeSort(int[] array) {
    if (array.length <= 1) return array;

    int midIndex = array.length / 2;
    int[] left = mergeSort(Arrays.copyOfRange(array, 0, midIndex));
    int[] right = mergeSort(Arrays.copyOfRange(array, midIndex, array.length));

    return merge(left, right);
}


public static void main(String[] args) {
    int[] myArray = {3,1,4,2};
    int [] sortedArray = mergeSort(myArray);

    System.out.println("\nOriginal :" + Arrays.toString( orginalArray ));
    System.out.println("\nSorted :" + Arrays.toString( sortedArray ));
}




// 配列 [3,1,4,2] をマージソートするプロセス：
// 初期配列 [3,1,4,2] は中央で [3,1] と [4,2] に分割されます。
//        [3,1] はさらに [3] と [1] に、[4,2] は [4] と [2] に分割されます。
// 各サブ配列は長さが1なので、それ以上分割できません。ここで再帰が終了し、マージのプロセスが開始されます。
//        [3] と [1] は [1,3] に、[4] と [2] は [2,4] にマージされます。
// 最後に、[1,3] と [2,4] がマージされて、最終的なソート済み配列 [1,2,3,4] が得られます。