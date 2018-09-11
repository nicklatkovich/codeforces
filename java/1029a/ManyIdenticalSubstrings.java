import java.io.*;
import java.util.*;

public class ManyIdenticalSubstrings {

	static StringTokenizer st;
	static BufferedReader br;

	public static void main(String[] args) {
		br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		next();
		short k = Short.parseShort(next());
		String t = next();
		sc.close();
		PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
		out.println(getMinIdenticalSubstring(t, k));
		out.close();
	}

	public static Boolean isMin(String source, short k) {
		for (short i = k; i < source.length(); i++) {
			if (source.charAt(i) != source.charAt(i % k))
				return false;
		}
		return true;
	}

	public static String getMinIdenticalSubstring(String source, short count) {
		short n = (short) (source.length());
		for (short i = 1; i <= n; i++) {
			if (i != n && !isMin(source, i))
				continue;
			String minSubstring = source.substring(0, i);
			String result = "";
			for (short j = 1; j < count; j++)
				result += minSubstring;
			return result + source;
		}
		throw new Error("Min substring not found");
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
