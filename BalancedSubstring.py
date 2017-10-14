# 873B


class Characteristic:
    def __init__(self, units: int, zeros: int):
        self.units = units
        self.zeros = zeros

    def clone(self):
        return Characteristic(self.units, self.zeros)

    def isBalanced(self) -> bool:
        return self.units == self.zeros


def main() -> None:
    n = int(input())
    s = str(input())
    result = n
    prevCharacteristic = None
    subValue = 0
    while True:
        if result == 0:
            print(0)
            return
        if result == n:
            characteristic = Characteristic(0, 0)
            for char in s:
                if char == '1':
                    characteristic.units += 1
                else:
                    characteristic.zeros += 1
        else:
            characteristic = prevCharacteristic
            for i in range(result, result + subValue):
                if s[i] == '1':
                    characteristic.units -= 1
                else:
                    characteristic.zeros -= 1
        prevCharacteristic = characteristic
        newCharacteristic = characteristic.clone()
        iPrev = -1
        iNext = result - 1
        subValue = result
        for i in range(n - result + 1):
            if i > 0:
                if s[iPrev] == '1':
                    newCharacteristic.units -= 1
                else:
                    newCharacteristic.zeros -= 1
                if s[iNext] == '1':
                    newCharacteristic.units += 1
                else:
                    newCharacteristic.zeros += 1
            if newCharacteristic.isBalanced():
                print(result)
                return
            iPrev += 1
            iNext += 1
            subValue = min(subValue, abs(newCharacteristic.units - newCharacteristic.zeros))
        result -= subValue


main()
