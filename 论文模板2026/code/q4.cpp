/* ===========================================================================
 *  【占位示例】本文件仅用于演示附录源码排版，内容与赛题无关。
 *  提交前必须整体替换为本队真实程序，并同步修改附录 A 的文件列表。
 *  编译：g++ -O2 -std=c++17 -o q4 q4.cpp
 * ===========================================================================
 *  问题四示范程序：0-1 背包的动态规划求解（含方案回溯）
 */

#include <algorithm>
#include <iostream>
#include <vector>

int main()
{
    // 物品重量、价值与背包容量（示例数据，实际请换成赛题数据）
    const std::vector<int> weight = {2, 3, 4, 5, 9};
    const std::vector<int> value  = {3, 4, 5, 8, 10};
    const int capacity = 20;

    const int n = static_cast<int>(weight.size());
    // dp[j] = 容量 j 时的最大价值
    std::vector<int> dp(capacity + 1, 0);
    // keep[i][j] = 决策记录，用于回溯最优方案
    std::vector<std::vector<char>> keep(n, std::vector<char>(capacity + 1, 0));

    for (int i = 0; i < n; ++i) {
        for (int j = capacity; j >= weight[i]; --j) {   // 倒序保证每件物品只用一次
            if (dp[j - weight[i]] + value[i] > dp[j]) {
                dp[j] = dp[j - weight[i]] + value[i];
                keep[i][j] = 1;
            }
        }
    }

    // 回溯被选中的物品
    std::vector<int> chosen;
    for (int i = n - 1, j = capacity; i >= 0; --i) {
        if (keep[i][j]) {
            chosen.push_back(i + 1);
            j -= weight[i];
        }
    }
    std::reverse(chosen.begin(), chosen.end());

    std::cout << "背包容量: " << capacity << '\n';
    std::cout << "最大总价值: " << dp[capacity] << '\n';
    std::cout << "选取的物品编号:";
    for (int id : chosen) std::cout << ' ' << id;
    std::cout << std::endl;
    return 0;
}
