import java.io.*;
import java.util.*;

public class StreetLights {

	static StringTokenizer st;
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = Integer.parseInt(next());
		int m = Integer.parseInt(next());
		int k = Integer.parseInt(next());
		int[] s = new int[m];
		boolean[] isEmpty = new boolean[n];
		for (int i = 0; i < n; i++) {
			isEmpty[i] = true;
		}
		for (int i = 0; i < m; i++) {
			s[i] = Integer.parseInt(next());
			isEmpty[s[i]] = false;
		}
		int[] a = new int[k];
		for (int i = 0; i < k; i++) {
			a[i] = Integer.parseInt(next());
		}
		int[] steps = new int[n];
		for (int i = 0; i < n; i++) {
			if (isEmpty[i]) {
				steps[i] = i;
			} else {
				steps[i] = i > 0 ? steps[i - 1] : -1;
			}
		}
		long result = -1;
		for (int i = 0; i < k; i++) {
			int count = 0;
			{
				int power = i + 1;
				int saveLenght = -1;
				for (int pos = 0; pos < n; pos = steps[pos] + power) {
					if (steps[pos] <= saveLenght) {
						count = -1;
						break;
					}
					saveLenght = steps[pos];
					count++;
				}
			}
			long price = (long) count * a[i];
			if (count != -1 && (result == -1 || price < result)) {
				result = price;
			}
		}
		sc.close();
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		out.println(result);
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
