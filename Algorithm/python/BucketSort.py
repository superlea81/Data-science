def BucketSort1(sequence):
    Bucket = [0] * (max(sequence) - min(sequence) + 1)  # 将最大的减去最小的然后加1，分配如此长度的桶
    for i in range(len(sequence)):
        Bucket[sequence[i]-min(sequence)] += 1

    tmp = []

    for i in range(len(Bucket)):
        if Bucket[i] != 0:
            tmp += [min(sequence) + i] * Bucket[i]
    return tmp


def BucketSort2(array, n):
    new_list = [[] for _ in range(n)] # 创建n个空桶
    for data in array:
        index = int(data * n) # 判断应该放在哪个桶
        new_list[index].append(data)

    for i in range(n):
        new_list[i].sort()

    index = 0
    for i in range(n):
        for j in range(len(new_list[i])):
            array[index] = new_list[i][j]
            index += 1
    return array


if __name__ == '__main__':
    sequence1 = [1, 4, 5, 2, 55, 44, 66, 77, 66, 66, 88, 1]
    BucketSort1(sequence1)
    sequence2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    BucketSort2(sequence2, len(sequence2))
