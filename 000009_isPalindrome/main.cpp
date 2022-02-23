#include <iostream>
#include <limits>

using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int s = 0;
        int y = x;
        while (y > 0) {
            if (s > (std::numeric_limits<int>::max() / 10 - (y % 10))) {
                return false;
            }
            s = 10 * s + (y % 10);
            y = y / 10;
        }

        return (s == x);
    }
};


void assert(Solution &s, bool expected, int x) {
    bool actual = s.isPalindrome(x);
    cout << (expected == actual ? "Pass" : "Fail") << " isPalindrome(" << x << ") -> " << actual << endl;
}


int main() {
    Solution s;
    assert(s, true, 121);
    assert(s, false, -121);
    assert(s, false, -10);
    return 0;
}

