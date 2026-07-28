class Solution {
	public:
	void solve(int left, int right, int &count, string &s) {
		while (left >= 0 && right < s.size() && s[left] == s[right]) {
			if (right - left + 1 >= 2)
				count++;
			left--;
			right++;
		}
	}
	
	int countPS(string &s) {
		
		int count = 0;
		int n = s.size();
		
		for (int i = 0; i < n; i++) {
			solve(i, i, count, s);
			solve(i, i + 1, count, s);
		}
		return count;
	}
};
