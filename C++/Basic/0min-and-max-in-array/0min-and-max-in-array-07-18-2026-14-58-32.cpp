class Solution {
	public:
	vector<int> getMinMax(vector<int> &arr) {
		int mini = INT_MAX;
		int maxi = INT_MIN;
		
		for (int num: arr) {
			if (num < mini) {
				mini = num;
			}
			if (num > maxi) {
				maxi = num;
			}
		}
		return {mini, maxi};
		
	}
};
