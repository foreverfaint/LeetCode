from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)

        from queue import Queue
        q = Queue()
        q.put_nowait((start, 0))

        seen  = set()
        while not q.empty():
            curr, cnt = q.get_nowait()
            
            if curr == end:
                return cnt

            if curr in seen:
                continue
            seen.add(curr)

            for i in range(len(curr)):
                for c in "ACGT":
                    if c == curr[i]:
                        continue
                    new_gene = curr[:i] + c +curr[i+1:]
                    if new_gene not in bank:
                        continue
                    q.put_nowait((new_gene, cnt + 1))
        
        return -1




if __name__ == "__main__":
    sln = Solution()
    print(sln.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(sln.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
    print(sln.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]))