#include <iostream>
#include <vector>

using namespace std;

void bubbleSort(vector<int> &v, int n) {
    int swapCount = 0;
    int flag = 1;
    for (int i = 0; flag; i++) {
        flag = 0;
        for (int j = n - 1; j >= i + 1; j--) {
            if (v[j] < v[j - 1]) {
                swap(v[j], v[j - 1]);
                swapCount++;
                flag = 1;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << v[i];
        if (i != n - 1) cout << " ";
        else cout << endl;
    }
    cout << swapCount << endl;
}

int main() {
    int n, t;
    cin >> n;
    vector<int> v;

    for (int i = 0; i < n; i++) {
        cin >> t;
        v.push_back(t);
    }

    bubbleSort(v, n);
    return 0;
}
