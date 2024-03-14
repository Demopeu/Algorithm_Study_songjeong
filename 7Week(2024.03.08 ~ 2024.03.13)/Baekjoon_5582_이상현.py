max_ = 0
s1 = input()
s2 = input()

len_s1 = len(s1)
len_s2 = len(s2)

dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] += dp[i - 1][j - 1] + 1
            max_ = max(max_, dp[i][j])

print(max_)

# #include <iostream>
# #include <string>
# #include <vector>
# using namespace std;

# int main() {
# 	int max_ = 0;
# 	string str1, str2;

# 	cin >> str1 >> str2;

# 	int len_s1 = str1.length();
# 	int len_s2 = str2.length();

# 	vector<vector<int>> vec(len_s1 + 1, vector<int>(len_s2 + 1));

# 	for (int row = 0; row < len_s1; ++row) {
# 		for (int col = 0; col < len_s2; ++col) {
# 			if (str1[row] == str2[col]) {
# 				vec[row + 1][col + 1] = vec[row][col] + 1;
# 				max_ = max_ < vec[row + 1][col + 1] ? vec[row + 1][col + 1] : max_;
# 			}
# 		}
# 	}
# 	cout << max_;

# 	return 0;
# }

#   A B C D
# A 1 0 0 0
# A 1 0 0 0
# B 0 2 0 0
# C 0 0 3 0