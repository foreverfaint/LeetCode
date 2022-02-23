#include <iostream>
#include <limits>

using namespace std;


bool isFirstMatch(string s, string p) {
    return s[0] == p[0] || p[0] == '.';
}


class Solution {
public:
    bool isMatch(string s, string p) {
        int l_p = p.length();
        int l_s = s.length();

        if (l_p == 0) {
            return l_s == 0;
        }

        if (l_p == 1) {
            return l_s == 1 && isFirstMatch(s, p);
        }

        if (p[1] == '*') {
            return (this->isMatch(s, p.substr(2))) || (l_s > 0 && isFirstMatch(s, p) && this->isMatch(s.substr(1), p));
        }

        return l_s > 0 && isFirstMatch(s, p) && this->isMatch(s.substr(1), p.substr(1));
    }
};


void assert(Solution &sln, bool expected, string s, string p) {
    bool actual = sln.isMatch(s, p);
    cout << (expected == actual ? "Pass" : "Fail") << " isMatch(" << s << "," << p << ") -> " << actual << endl;
}


int main() {
    Solution s;
    assert(s, true, "aaa", "a*a");
    assert(s, false, "ab", ".*c");
    assert(s, false, "aa", "a");
    assert(s, true, "aa", "a*");
    assert(s, true, "ab", ".*");
    assert(s, true, "abab", ".*");
    assert(s, true, "ab", "a.");
    assert(s, true, "ab", "a*b");
    assert(s, true, "aab", "c*a*b");
    assert(s, false, "aab", "c*a*c");
    return 0;
}