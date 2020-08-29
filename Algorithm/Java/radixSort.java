package BasicAlgorithm.Sort;
import java.util.Arrays;

public class radixSort {
    public static void main(String[] args) {
        int[] data = new int[] { 1100, 192, 221, 12, 23 };
        print(data);
        radixSort(data, 10, 4);
        System.out.println("排序后的数组：");
        print(data);
    }

    public static void radixSort(int[] data, int radix, int d) {
        // 缓存数组
        int[] tmp = new int[data.length];
        // buckets用于记录待排序元素的信息
        // buckets数组定义了max-min个桶
        int[] buckets = new int[radix];    // 十个桶， 因为区间是0到9
        for (int i = 0, rate = 1; i < d; i++) {
            // 重置count数组，开始统计下一个关键字
            Arrays.fill(buckets, 0);
            // 将data中的元素完全复制到tmp数组中
            System.arraycopy(data, 0, tmp, 0, data.length);
            // 计算每个待排序数据的子关键字
            for (int j = 0; j < data.length; j++) {
                int subKey = (tmp[j] / rate) % radix; // 0 2 1 2 3 个位数 第二次循环
                buckets[subKey]++;
            }
            // 1 1 2 1 0 0 0 0 0 0
            for (int j = 1; j < radix; j++) {
                buckets[j] = buckets[j] + buckets[j - 1];
            }
            // 1 2 4 5 5 5 5 5 5 5
            /*
            for (int k = 0; k < radix; k++) {
                System.out.println(buckets[k]);
            }
            System.out.println("--------");
            多行注释中，打印出k可以帮助理解
            因为如果不用buckets[j] = buckets[j] + buckets[j - 1];
            第一个关键字也就是个位数上是1 1 2 1 0 0 0 0 0 0
            没法根据buckets[subkey]定位到该存放的位置
            用前面的加后面的，最大是5，也就是整个data的长度
            在用tmp给data赋值的时候，先减去1，有效的的避免数组越界。
            */
            // 按子关键字对指定的数据进行排序
            for (int m = data.length - 1; m >= 0; m--) {
                int subKey = (tmp[m] / rate) % radix;
                //System.out.println(subKey);
                //System.out.println(buckets[subKey]);
                data[--buckets[subKey]] = tmp[m];  // 23 12 221 192 1100倒着遍历 --buckets[subkey] = 4 3 1 2 0

            }
            //System.out.println("------------");
            rate *= radix;
        }
    }

    public static void print(int[] data) {
        for (int i = 0; i < data.length; i++) {
            System.out.print(data[i] + " ");
        }
        System.out.println();
    }
}
