from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        l = len(arr)

        f_sums = [0] * l
        f_sums[0] = arr[0]
        f_m = {f_sums[0]: [0]}
        b_sums = [0] * l
        b_sums[l - 1] = arr[l - 1] 
        b_m = {b_sums[l - 1]: [l - 1]}
        for i in range(1, l):
            f_sums[i] = f_sums[i - 1] + arr[i]
            f_m.setdefault(f_sums[i], [])
            f_m[f_sums[i]].append(i)
            b_sums[l - i - 1] = b_sums[l - i] + arr[l - i - 1]
            b_m.setdefault(b_sums[l - i - 1], [])
            b_m[b_sums[l - i - 1]].append(l - i - 1)

        for f_val, f_idx_list in f_m.items():
            for f_idx in f_idx_list:
                for b_idx in b_m.get(f_val, []):
                    if b_idx > f_idx + 1 and f_sums[b_idx - 1] - f_sums[f_idx] == f_val:
                        return True

        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
    print(sln.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
    print(sln.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))