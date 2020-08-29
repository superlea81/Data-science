import copy


def radixSort(data, radix, d):
    rate = 1
    for i in range(d):  # 循环四次 因为最大是4位数
        tmp = copy.deepcopy(data)
        buckets = [0 for _ in range(radix)]
        for j in range(len(data)):
            sub_key = int((tmp[j] / rate) % radix)
            buckets[sub_key] += 1

        for k in range(1, len(buckets)):
            buckets[k] = buckets[k] + buckets[k - 1]

        for x in range(len(data) - 1, -1, -1):
            sub_key = int((tmp[x] / rate) % radix)
            buckets[sub_key] -= 1
            data[buckets[sub_key]] = tmp[x]
        rate *= radix
    return data


if __name__ == '__main__':
    data = [1100, 192, 221, 12, 23]
    print(data)
    print("排序后的数组：")
    print(radixSort(data, 10, 4))
