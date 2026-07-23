class Solution {
	public:
	int getLPSLength(string &s) {
		int n = s.length();
		
		vector<int> LPS(n, 0);
		LPS[0] = 0;
		int length_idx = 0;
		
		int i = 1;
		
		while (i < n)
			{
			if (s[i] == s[length_idx])
				{
				length_idx++;
				LPS[i] = length_idx;
				i++;
			}
			else
				{
				if (length_idx == 0)
					{
					LPS[i] = 0;
					i++;
				}
				else
					length_idx = LPS[length_idx - 1];
			}
		}
		return LPS[n - 1];
	}
};
