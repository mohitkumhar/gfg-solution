class Solution {
	public:
	
	int solve(int i, int j, string s1, string s2, vector<vector<int>> &memo)
	{
		if (i == s1.length())
			return s2.length() - j;
		if (j == s2.length())
			return s1.length() - i;
		
		if (memo[i][j] != -1)
			return memo[i][j];
		
		if (s1[i] == s2[j])
			{
			memo[i][j] = solve(i + 1, j + 1, s1, s2, memo);
			return memo[i][j];
		}
		
		// insert
		int insert = 1 + solve(i, j + 1, s1, s2, memo);
		
		// replace
		int replace = 1 + solve(i + 1, j + 1, s1, s2, memo);
		
		// delete
		int del = 1 + solve(i + 1, j, s1, s2, memo);
		
		memo[i][j] = min({insert, replace, del});
		return memo[i][j];
	}
	
	int editDistance(string& s1, string& s2) {
		vector<vector<int>> memo(s1.length() + 1, vector<int>(s2.length() + 1, -1));
		int minOperation = solve(0, 0, s1, s2, memo);
		
		return minOperation;
		
	}
};
