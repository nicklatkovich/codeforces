#include <stdint.h>
#include <iostream>

int main() {
	int windows_count, result = 0;
	std::cin >> windows_count;
	bool a, b, c;
	for (int window_index = 0; window_index < windows_count; window_index++) {
		int window_is_active;
		std::cin >> window_is_active;
		a = b;
		b = c;
		c = window_is_active == 1;
		if (a && !b && c) {
			result++;
			c = !c;
		}
	}
	std::cout << result << std::endl;
	return 0;
}
