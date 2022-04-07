from typing import List


class Solution:
    def to_structure(self, log):
        fields = log.split(" ")
        return {
            "identity": fields[0],
            "content": " ".join(fields[1:]),
            "isLetterLog": all(["a" <= c <= "z" for c in fields[1]]),
            "raw": log,
        }

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [self.to_structure(log) for log in logs]
        letter_logs = sorted([log for log in logs if log["isLetterLog"]], key=lambda x: (x["content"], x["identity"]))
        digit_logs = [log for log in logs if not log["isLetterLog"]]
        return [log["raw"] for log in letter_logs + digit_logs]


if __name__ == "__main__":
    sln = Solution()
    print(sln.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
    print(sln.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))
    print(sln.reorderLogFiles(["dig1 8 1 5 1","let1 art zero can","dig2 3 6","let2 own kit dig","let3 art zero"]))