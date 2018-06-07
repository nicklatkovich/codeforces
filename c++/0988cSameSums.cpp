#include <iostream>
#include <stdint.h>
#include <tuple>
#include <unordered_map>

int main()
{
    uint32_t k;
    std::cin >> k;
    uint32_t* n = new uint32_t[k];
    int64_t* sums = new int64_t[k];
    std::unordered_map<int64_t, std::tuple<uint32_t, uint32_t>> diffs;
    int16_t** a = new int16_t*[k];
    for (uint32_t i = 0; i < k; i++) {
        sums[i] = 0;
        std::cin >> n[i];
        a[i] = new int16_t[n[i]];
        for (uint32_t j = 0; j < n[i]; j++) {
            std::cin >> a[i][j];
            sums[i] += a[i][j];
        }
        for (uint32_t j = 0; j < n[i]; j++) {
            int64_t presum = sums[i] - a[i][j];
            std::unordered_map<int64_t, std::tuple<uint32_t, uint32_t>>::iterator find = diffs.find(presum);
            if (find == diffs.end()) {
                diffs[presum] = std::make_tuple(i, j);
            } else if (std::get<0>(find->second) != i) {
                std::cout << "YES" << std::endl;
                std::cout << i + 1 << " " << j + 1 << std::endl;
                std::cout << std::get<0>(find->second) + 1 << " " << std::get<1>(find->second) + 1 << std::endl;
                return 0;
            }
        }
    }
    std::cout << "NO" << std::endl;
    return 0;
}
