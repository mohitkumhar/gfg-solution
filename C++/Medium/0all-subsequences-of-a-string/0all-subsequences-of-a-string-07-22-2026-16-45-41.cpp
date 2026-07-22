class Solution {
	public:
	void solve(int i, string curr_str, vector<string> &result, string s)
	{
		if (i == s.length())
			{
			result.push_back(curr_str);
			return;
		}
		
		// take
		solve(i + 1, curr_str + s[i], result, s);
		
		// skip
		solve(i + 1, curr_str, result, s);
	}
	
	vector<string> powerSet(string &s) {
		int n = s.length();
		vector<string> result;
		solve(0, "", result, s);
		
		sort(result.begin(), result.end());
		return result;
		
	}
};
