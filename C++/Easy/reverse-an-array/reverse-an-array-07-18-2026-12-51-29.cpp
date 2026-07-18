class Solution {
	public:
	void swap(int &a, int &b) {
		int temp = a;
		a = b;
		b = temp;
	}
	
	void reverseArray(vector<int> &arr) {
		int i = 0;
		int j = arr.size() - 1;
		
		while (i < j) {
			swap(arr[i], arr[j]);
			i++;
			j--;
		}
	}
};
