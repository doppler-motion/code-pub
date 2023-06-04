class Solution:
    def addNegabinary(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        sum1, sum2 = 0, 0
        sum1 = sum([(-2) ** (n1 - 1 - i) for i, item in enumerate(arr1) if item == 1])
        sum2 = sum([(-2) ** (n2 - 1 - i) for i, item in enumerate(arr2) if item == 1])

        print(sum1)
        print(sum2)

        return list(map(int, list(str(bin(sum1 + sum2)[2:]))))


if __name__ == "__main__":
    s = Solution()
    arr1 = [0]
    arr2 = [1, 0]
    print(s.addNegabinary(arr1, arr2))
