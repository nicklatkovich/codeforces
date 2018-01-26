using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Application {
	class JamieAndBinarySequence {

		public static Tuple<bool, short[ ]> solve(ulong n, uint k) {
			ulong m = 0;
			Dictionary<short, ulong> cnt = new Dictionary<short, ulong>( );
			for (short i = 0; i <= 63; i++) {
				if (((n >> i) & 1) > 0) {
					if (!cnt.ContainsKey(i)) {
						cnt[i] = 0;
					}
					cnt[i]++;
					m++;
				}
			}
			if (m > k) {
				return new Tuple<bool, short[ ]>(false, new short[ ] { 0 });
			}
			for (short i = 63; i >= -63; i--) {
				ulong temp = cnt.ContainsKey(i) ? cnt[i] : 0;
				if (m + temp <= k) {
					short decI = (short)(i - 1);
					m += temp;
					if (!cnt.ContainsKey(decI)) {
						cnt[decI] = 0;
					}
					cnt[decI] += temp * 2;
					cnt[i] = 0;
				} else {
					break;
				}
			}
			SortedMultiSet<short> ms = new SortedMultiSet<short>( );
			for (short i = 63; i >= -63; i--) {
				if (cnt.ContainsKey(i)) {
					for(ulong j = 0; j < cnt[i]; j++) {
						ms.Add(i);
					}
				}
			}
			while (ms.Size < k) {
				short u = ms.ElementAt(0);
				ms.Remove(u);
				ms.Add((short)(u - 1));
				ms.Add((short)(u - 1));
			}
			short[] result = new short[ms.Size];
			{
				ulong i = 0;
				while (ms.Size > 0) {
					result[i++] = ms.Pop( );
				}
			}
			return new Tuple<bool, short[ ]>(true, result);
		}

		static void Main( ) {
			string[] inputS = Console.ReadLine( ).Split(' ');
			ulong[] input = new ulong[inputS.Length];
			for (ushort i = 0; i < inputS.Length; i++) {
				input[i] = ulong.Parse(inputS[i]);
			}
			Tuple<bool, short[ ]> result = solve(input[0], (uint)input[1]);
			Console.WriteLine(result.Item1 ? "Yes" : "No");
			if (result.Item1) {
				foreach (short element in result.Item2) {
					Console.Write(element);
					Console.Write(' ');
				}
				Console.WriteLine( );
			}
		}
	}

	public class SortedMultiSet<T> : IEnumerable<T> {

		private SortedDictionary<T, int> _dict; 
		private ulong _size = 0ul;

		public ulong Size => _size;

		public SortedMultiSet( ) {
			_dict = new SortedDictionary<T, int>( );
		}

		public SortedMultiSet(IEnumerable<T> items) : this( ) {
			Add(items);
		}

		public bool Contains(T item) {
			return _dict.ContainsKey(item);
		}

		public void Add(T item) {
			if (_dict.ContainsKey(item)) {
				_dict[item]++;
			} else {
				_dict[item] = 1;
			}
			_size++;
		}

		public void Add(IEnumerable<T> items) {
			foreach (var item in items) {
				Add(item);
			}
		}

		public void Remove(T item) {
			if (!_dict.ContainsKey(item)) {
				throw new ArgumentException( );
			}
			if (--_dict[item] == 0) {
				_dict.Remove(item);
			}
			_size--;
		}

		public T Peek( ) {
			if (!_dict.Any( )) {
				throw new NullReferenceException( );
			}
			return _dict.Last( ).Key;
		}

		public T Pop( ) {
			T item = Peek( );
			Remove(item);
			return item;
		}

		public IEnumerator<T> GetEnumerator( ) {
			foreach(var kvp in _dict) {
				for(int i = 0; i < kvp.Value; i++) {
					yield return kvp.Key;
				}
			}
		}

		IEnumerator IEnumerable.GetEnumerator( ) {
			return this.GetEnumerator( );
		}
	}
}

