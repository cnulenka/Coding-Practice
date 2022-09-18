class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        stack<int> st;
        int n = T.size();
        vector<int> res(n);
        for(int i = n-1; i>=0; i--)
        {
            while(!st.empty() && T[st.top()] <= T[i])
                st.pop();
            
            if(st.empty())
                res[i] = 0;
            else
                res[i] = st.top() - i;
            
            st.push(i);
        }
        
        return res;
    }
};