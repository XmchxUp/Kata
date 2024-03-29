#include <iostream>
#include <vector>

using namespace std;

void myPrint(vector<int>& nums) {
    for (int i = 0; i < nums.size() - 1; i++) cout << nums[i] << " ";
    cout << nums.back() << endl;
}

void insertSort(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        int j = i - 1;
        int t = nums[i];
        myPrint(nums);
        while (j >= 0 && t < nums[j]) {
            nums[j + 1] = nums[j];
            j--;
        }
        nums[j + 1] = t;
    }
    myPrint(nums);
}

int main() {
    int n;
    cin >> n;

    vector<int> nums;
    for (int i = 0; i < n; i++) {
        int t;
        cin >> t;
        nums.push_back(t);
    }
    insertSort(nums);
    return 0;
}
