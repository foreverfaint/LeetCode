from typing import List


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))


if __name__ == "__main__":
    sln = Solution()
    print(sln.defangIPaddr("1.1.1.1"))
    print(sln.defangIPaddr("255.100.50.0"))