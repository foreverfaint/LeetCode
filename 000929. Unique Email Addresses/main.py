from typing import List


class Solution:
    def refine(self, email):
        local_name, domain_name = email.split("@")
        ans = []
        for c in local_name:
            if c == ".":
                continue
            if c == "+":
                break
            ans.append(c)
        return "".join(ans) + "@" + domain_name

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set([self.refine(email) for email in emails]))


if __name__ == "__main__":
    sln = Solution()
    print(sln.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
    print(sln.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))