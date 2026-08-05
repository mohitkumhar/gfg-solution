class Solution {
	public:
	void rotateMatrix(vector<vector<int>> & mat) {
		
		int n = mat.size();
		
		for (vector<int> &m : mat)
			reverse(m.begin(), m.end());
		
		for (int i = 0; i < n; i++)
			for (int j = i + 1; j < n; j++)
				swap(mat[i][j], mat[j][i]);
		
	}
};
