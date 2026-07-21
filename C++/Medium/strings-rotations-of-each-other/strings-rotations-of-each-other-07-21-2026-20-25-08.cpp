class Solution {
  public:
    bool areRotations(string &s1, string &s2) {
        // code here
        return s1.length() == s2.length() && (s1 + s1).find(s2) != string::npos;
    }
};