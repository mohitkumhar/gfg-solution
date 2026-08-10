class Solution {
	public:
	long subarrayXor(vector<int> &arr, int k) {
		// code here
		
		int n = arr.size();
		map<int, int> prefixXOR {{0, 1}};
		
		int currXOR = 0;
		int count = 0;
		
		for (int i = 0; i < n; i++)
			{
			currXOR ^= arr[i];
			
			if (prefixXOR.find(currXOR ^ k) != prefixXOR.end())
				count += prefixXOR[currXOR ^ k];
			prefixXOR[currXOR]++;
		}
		
		return count ;
	}
};
