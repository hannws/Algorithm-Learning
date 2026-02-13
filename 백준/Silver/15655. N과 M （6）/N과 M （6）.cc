#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int backtrack(int idx, vector<int>& path, int M, const vector<int>& nums) {
    if (path.size() == M) {
        for (const auto& i : path) {
            cout << i << ' ';
        }
        cout << '\n';
        return 0;
    }

    for (int i = idx; i < nums.size(); i++) {
        path.push_back(nums[i]);
        backtrack(i + 1, path, M, nums);
        path.pop_back();
    }
    return 0;
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
    int len = nums.size();
    vector<int> path;
    backtrack(0, path, M, nums);
    return 0;
}
