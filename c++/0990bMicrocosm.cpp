#include <algorithm>
#include <iostream>

int main()
{
    uint32_t n, K;
    std::cin >> n >> K;
    uint32_t* a = new uint32_t[n];
    for (uint32_t i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    std::sort(a, a + n);
    uint32_t result = n;
    for (uint32_t j = 0, jNext = 1; jNext < n; j = jNext, jNext++) {
        bool can_be_eated = false;
        uint32_t eats_count = 1;
        for (uint32_t i = jNext; i < n; i++, j = jNext, jNext++, eats_count++) {
            if (a[i] > a[j] + K) {
                break;
            }
            if (a[i] > a[j]) {
                can_be_eated = true;
                break;
            }
        }
        if (can_be_eated) {
            result -= eats_count;
        }
    }
    std::cout << result << std::endl;
    return 0;
}
