class Solution {
	public:
	double minMaxDist(vector<int> &stations, int k) {
		// Code here
		
		int n = stations.size();
		if (n <= 1)
			return 0.0;
		
		priority_queue<tuple<double, int, int>> pq;
		
		for (int i = 0; i < n - 1; i++)
			{
			double gap = stations[i + 1] - stations[i];
			pq.push(make_tuple(gap, i, 1));
		}
		
		for (int i = 0; i < k; i++)
			{
			
			tuple<double, int, int> top = pq.top();
			
			double currGap = get<0>(top);
			int index = get<1>(top);
			int count = get<2>(top);
			
			pq.pop();
			
			count++;
			
			double originalGap = stations[index + 1] - stations[index];
			
			double newGap = originalGap / count;
			
			pq.push(make_tuple(newGap, index, count));
		}
		
		tuple<double, int, int> top = pq.top();
		
		double maxDist = get<0>(top);
		
		return maxDist;
		
	}
};
