class Solution {
	public:
	int countMinReversals(string s) {
		stack<char> stack;
		
		int open_brack = 0;
		int close_brack = 0;
		
		for (char c : s)
			{
			if (c == '}')
				{
				if (!stack.empty() && stack.top() == '{')
					{
					open_brack--;
					stack.pop();
				}
				else
					{
					close_brack++;
					stack.push(c);
				}
			}
			else
				{
				if (c == '{')
					open_brack++;
				else
					close_brack--;
				stack.push(c);
			}
		}
		
		if ((open_brack + close_brack) % 2 == 1)
		    return -1;
		
		return (open_brack + 1) / 2 + (close_brack + 1) / 2;
	}
};
