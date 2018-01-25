using System;

namespace Application {
	class Browser {

		static void Main( ) {
			string[] inputS = Console.ReadLine( ).Split(' ');
			ushort[] input = new ushort[4];
			for (ushort i = 0; i < 4; i++) input[i] = ushort.Parse(inputS[i]);
			ushort
			n = input[0],
			pos = input[1],
			l = input[2],
			r = input[3],
			a = 1,
			b = n,
			result = 0;
			bool toLeft = Math.Abs(l - pos) < Math.Abs(r - pos);
			while (a != l || b != r) {
				if (toLeft) {
					if (a != l) {
						result += (ushort)(Math.Abs(l - pos) + 1);
						a = pos = l;
					}
				} else {
					if (b != r) {
						result += (ushort)(Math.Abs(r - pos) + 1);
						b = pos = r;
					}
				}
				toLeft = !toLeft;
			}
			Console.WriteLine(result);
		}
	}
}

