#include<bits/stdc++.h>

using namespace std;
#define long long int int;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

vector<vii> AdjList;

vector<pair<int, ii> > EdgeList;

class UnionFind {                                              // OOP style
private:
  vi p, rank, setSize;                       // remember: vi is vector<int>
  int numSets;
public:
  UnionFind(int N) {
    setSize.assign(N, 1); numSets = N; rank.assign(N, 0);
    p.assign(N, 0); for (int i = 0; i < N; i++) p[i] = i; }
  int findSet(int i) { return (p[i] == i) ? i : (p[i] = findSet(p[i])); }
  bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }
  void unionSet(int i, int j) { 
    if (!isSameSet(i, j)) { numSets--; 
    int x = findSet(i), y = findSet(j);
    // rank is used to keep the tree short
    if (rank[x] > rank[y]) { p[y] = x; setSize[x] += setSize[y]; }
    else                   { p[x] = y; setSize[y] += setSize[x];
                             if (rank[x] == rank[y]) rank[y]++; } } }
  int numDisjointSets() { return numSets; }
  int sizeOfSet(int i) { return setSize[findSet(i)]; }
};

int main(){
    int N, E, u, v, w;
    cin>>N>>E;
    for(int i=0; i<E; i++){
        cin>>u>>v>>w;
        u = u-1;
        v = v-1;
        EdgeList.push_back(make_pair(w, ii(u,v)));
    }
    sort(EdgeList.begin(), EdgeList.end());

    int mst_cost = 0;
    UnionFind UF(N);
    for(int i=0; i<E; i++){
        pair<int, ii> front = EdgeList[i];
        if(!UF.isSameSet(front.second.first, front.second.second)){
            mst_cost += front.first;
            UF.unionSet(front.second.first, front.second.second);
        }
    }
    
    cout<< mst_cost <<endl;
    
    return 0;
}

