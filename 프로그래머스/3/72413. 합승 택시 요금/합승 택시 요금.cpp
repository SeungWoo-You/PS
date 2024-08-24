#include <string>
#include <vector>
#include <queue>

#define INF 998877665544332211

using namespace std;

typedef long long LLT;

class Taxi {
private:
    int N;
    vector<vector<pair<int, int>>> G;
    
public:
    Taxi(int N, vector<vector<int>>* fares) {
        this->N = N;
        G.resize(N + 1);
        
        for (int i = 0; i < fares->size(); i++) {
            int u = (*fares)[i][0];
            int v = (*fares)[i][1];
            int w = (*fares)[i][2];
            G[u].push_back({v, w});
            G[v].push_back({u, w});
        }
    }
    
    void find(int src, vector<LLT>* dists) {
        priority_queue<pair<int, int>> PQ;
        dists->clear();
        dists->resize(N + 1, INF);
        (*dists)[src] = 0;
        PQ.push({0, src});
        
        while (!PQ.empty()) {
            int d = -PQ.top().first;
            int u = PQ.top().second;
            PQ.pop();
            
            if (d > (*dists)[u]) continue;
            
            for (auto& [v, w] : G[u]) {
                if ((*dists)[v] > d + w) {
                    (*dists)[v] = d + w;
                    PQ.push({-(*dists)[v], v});
                }
            }
        }
        
        return;
    }
};

LLT solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    LLT answer = INF;
    
    Taxi taxi(n, &fares);
    
    vector<LLT> a_dists, b_dists, common_dists;
    taxi.find(a, &a_dists);
    taxi.find(b, &b_dists);
    taxi.find(s, &common_dists);
    
    for (int i = 1; i <= n; i++)
        answer = min(answer, a_dists[i] + b_dists[i] + common_dists[i]);
    
    return answer;
}