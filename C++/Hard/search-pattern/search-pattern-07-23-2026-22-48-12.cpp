class Solution {
	public:
	vector<int> search(string &pat, string &txt) {
		
		int n = txt.length();
		int m = pat.length();
		
		vector<int> LPS(m, 0);
		LPS[0] = 0;
		int length_idx = 0;
		
		int k = 1;
		
		while (k < m)
			{
			if (pat[k] == pat[length_idx])
				{
				length_idx++;
				LPS[k] = length_idx;
				k++;
			}
			else
				{
				if (length_idx == 0)
					{
					LPS[k] = 0;
					k++;
				}
				else
					length_idx = LPS[length_idx - 1];
			}
		}
		
		int i = 0;
		int j = 0;
		
		vector<int> result;
		
		while (i < n)
			{
			if (txt[i] == pat[j])
				{
				i++;
				j++;
				if (j == m)
					{
					result.push_back(i - m);
					j = LPS[j - 1];
				}
			}
			else
				{
				if (j == 0)
					i++;
				else
					j = LPS[j - 1];
			}
		}
		return result;
	}
};
