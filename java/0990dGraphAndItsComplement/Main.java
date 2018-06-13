import java.io.*;
import java.util.*;

public class Main {

	static StringTokenizer st;
	static BufferedReader br;

	public static void main(String[] args) {
		br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		Scanner sc = new Scanner(System.in);
		short n = Short.parseShort(next());
		short a = Short.parseShort(next());
		short b = Short.parseShort(next());
		sc.close();
		if ((a > 1 && b > 1) || (n < 4 && n > 1 && a == 1 && b == 1)) {
			out.println("NO");
			out.close();
			return;
		}
		out.println("YES");
		boolean[][] result = new boolean[n][];
		boolean origin = a > b;
		for (short i = 0; i < n; i++) {
			result[i] = new boolean[n];
			for (short j = 0; j < n; j++) {
				result[i][j] = i == j ? false : !origin;
			}
		}
		short lines_count = (short) (n - (origin ? a : b));
		for (short i = 0, iNext = 1; i < lines_count; i = iNext, iNext++) {
			result[i][iNext] = result[iNext][i] = origin;
		}
		for (short i = 0; i < n; i++) {
			for (short j = 0; j < n; j++) {
				out.print(result[i][j] ? 1 : 0);
			}
			out.println();
		}
		out.close();
	}

	static String next() {
		while (st == null || !st.hasMoreElements()) {
			try {
				st = new StringTokenizer(br.readLine());
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return st.nextToken();
	}
}
