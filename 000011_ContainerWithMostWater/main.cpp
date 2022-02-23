#include <iostream>
#include <vector>

using namespace std;


int calArea(int left, int right, vector<int>& height) {
    return (right - left) * min(height[right], height[left]);
}


class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int max = calArea(left, right, height);
        cout << right << "-" << left << " -> " << right - left << endl;
        cout << "min(" << height[right] << "," << height[left] << ") -> " << min(height[right], height[left]) << endl;
        cout << max << endl;

        while (left < right) {
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
    
            
            int area = calArea(left, right, height);
            if (area > max) {
                max = area;
            }              
        }

        return max;
    }
};


void assert(Solution &sln, int expected, vector<int>& height) {
    int actual = sln.maxArea(height);
    cout << (expected == actual ? "Pass" : "Fail") << " maxArea(";
    for (int h: height) {
        cout << h << ",";
    }
    cout << ") -> " << actual << endl;
}


int main() {
    Solution s;

    vector<int> vect_1{ 1,8,6,2,5,4,8,3,7 };
    assert(s, 49, vect_1);

    vector<int> vect_2{ 1,1 };
    assert(s, 1, vect_2);

    return 0;
}