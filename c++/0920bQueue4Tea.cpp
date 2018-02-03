#define ushort unsigned short
#include <iostream>
using namespace std;
int main() {
	ushort testsCount;
	cin >> testsCount;
	for (ushort testNumber = 1; testNumber <= testsCount; testNumber++) {
		ushort
			studentsCount,
			currentTime = 0;
		cin >> studentsCount;
		for (ushort studentNumber = 1; studentNumber <= studentsCount; studentNumber++) {
			ushort enqueueTime, dequeueTime;
			cin >> enqueueTime >> dequeueTime;
			if (enqueueTime > currentTime) currentTime = enqueueTime;
			if (currentTime <= dequeueTime) {
				cout << currentTime << ' ';
				currentTime++;
			} else cout << "0 ";
		}
		cout << endl;
	}
}