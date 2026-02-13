#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void backtrack(vector<int>& path, int M, const vector<int>& nums) {
    if (path.size() == M) {
        for (int& i : path) {
            cout << i << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = 0; i < nums.size(); i++) {
        path.push_back(nums[i]);
        backtrack(path, M, nums);
        path.pop_back();
    }
    return;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;
    vector<int> nums(N);
    for (auto& i : nums) {
        cin >> i;
    }
    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    vector<int> path;
    backtrack(path, M, nums);
    return 0;
}
