if (!readline) { var { readline, print } = require('./index.js'); }

const
	ZERO_CHAR_CODE = '0'.charCodeAt();

/**
 * Returns an array of length 10
 * that stores the number of occurrences of each digit in the number
 * @param { string } number 
 * @returns { [number] }
 */
function getDigitsNumber(num) {
	var result = new Array(10).fill(0);
	for (var char of num) {
		var digit = char.charCodeAt() - ZERO_CHAR_CODE;
		if (digit >= 0 && digit <= 9) {
			result[digit]++;
		}
	}
	return result;
}

/**
 * Returns an array of digits of number
 * @param { string } number 
 * @returns { [number] }
 */
function getDigits(num) {
	var result = new Array(num.length).fill(0);
	for (var i = 0; i < num.length; i++) {
		var digit = num.charCodeAt(i) - ZERO_CHAR_CODE;
		if (digit < 0 || digit > 9) throw 'is not number';
		result[i] = digit;
	}
	return result;
}

/**
 * Returns a number (as string) consisting of digits of a and not exceeding b
 * @param { string } a 
 * @param { string } b 
 * @returns { string }
 */
function rearrangeNumbers(a, b) {
	var aNums = getDigitsNumber(a);
	var bNums = getDigits(b);
	var result = '';
	if (a.length != b.length) {
		for (var i = 9; i >= 0; i--) result += ('' + i).repeat(aNums[i]);
	} else {
		var rNums = new Array(a.length);
		var ind, lastInd;
		ind = lastInd = 0;
		var isLess = false;
		for (var i = 0; i < a.length; i++) {
			var needToBreak = true;
			var iFrom = isLess ? 9 : bNums[i];
			for (var j = iFrom; j >= 0; j--) {
				if (aNums[j] > 0) {
					if (j < bNums[i]) {
						isLess = true;
						lastInd = i;
					}
					ind = i;
					rNums[i] = j;
					aNums[j]--;
					needToBreak = false;
					break;
				}
			}
			if (needToBreak) break;
		}
		while (ind + 1 < a.length) {
			var needToStepBack = true;
			var iFrom = isLess ? 9 : bNums[ind + 1];
			for (var i = iFrom; i >= 0; i--) {
				if (aNums[i] > 0) {
					aNums[i]--;
					ind++;
					rNums[ind] = i;
					if (!isLess && i < iFrom) {
						isLess = true;
						lastInd = ind;
					}
					needToStepBack = false;
				}
			}
			if (needToStepBack) {
				aNums[rNums[ind]]++;
				ind--;
				// if (isLess && ind < lastInd) {
				if (isLess && ind == lastInd) {
					isLess = false;
				}
			}
		}
		for (var i = 0; i < a.length; i++) {
			result += '' + rNums[i]
		}
	}
	return result;
}

function main() {
	var a = readline();
	var b = readline();
	print(rearrangeNumbers(a, b));
}

main();
