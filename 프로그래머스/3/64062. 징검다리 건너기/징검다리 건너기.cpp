#include <string>
#include <vector>

#define INF (~0U >> 2)

using namespace std;

class SegTree{
  private:
    int k, N;
    vector<int> T;
    
  public:
    SegTree(vector<int>* stones) {
        N = stones->size();
        T.resize(2 * N, 0);
        
        for (int i = 0; i < N; i++)
            update(i, (*stones)[i]);
    }
    
    void update(int p, int x) {
        for (T[p += N] = x; p > 1; p >>= 1)
            T[p >> 1] = max(T[p], T[p ^ 1]);
    }
    
    int query(int l, int r) {
        int res = 0;
        
        for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
            if (l % 2) res = max(res, T[l++]);
            if (r % 2) res = max(res, T[--r]);
        }
        
        return res;
    }
};

int solution(vector<int> stones, int k) {
    int answer = INF;
    
    
    SegTree ST(&stones);
    int N = stones.size();
    
    for (int i = 0; i < N - k + 1; i++) {
        int l = i, r = i + k;
        answer = min(answer, ST.query(l, r));
    }
    
    return answer;
}