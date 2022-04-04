from typing import List


class Solution:
    def _toGoatLatin(self, w):
        if w[0] not in 'aeiouAEIOU':
            w = w[1:] + w[0]
        return w + "ma"

    def toGoatLatin(self, sentence: str) -> str:
        return " ".join([self._toGoatLatin(w) + "a" * (i + 1) for i, w in enumerate(sentence.split(" "))])


if __name__ == "__main__":
    sln = Solution()
    print(sln.toGoatLatin("I speak Goat Latin"))
    print("Imaa peaksmaaa oatGmaaaa atinLmaaaaa")
    print(sln.toGoatLatin("The quick brown fox jumped over the lazy dog"))
    print("heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")