#include<bits/stdc++.h>

using namespace std;

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

vector<vi> grid;

int main(){
    int N, E, u, v, w;
    cin>>N;
    grid.assign(N, vi());

    ifstream infile("p107_network.txt");

    for(int i=0; i<N; i++){
        string s;
        getline(infile,s);
        s += ",";
        //cout<<s<<endl;
        string temp="";
        for(int j=0; j<s.length(); j++){
            if(s[j]==','){
                if(temp == "-")
                    grid[i].push_back(-1);
                else{
                    stringstream ss(temp);
                    int x = 0;
                    ss>>x;
                    grid[i].push_back(x);    
                }
                temp = "";
            }
            else
                temp += s[j];
        }
        
    }


    infile.close();
    int total = 0;
    /*
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++)
            cout<<grid[i][j]<<" ";
        cout<<endl;
    } 
    */      

    
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++){
            if(grid[i][j]!=-1){    
                EdgeList.push_back(make_pair(grid[i][j], ii(i,j)));
                grid[j][i] = -1;
        }
    }
    sort(EdgeList.begin(), EdgeList.end());
    E = EdgeList.size();
    int mst_cost = 0;
    UnionFind UF(N);
    for(int i=0; i<E; i++){
        pair<int, ii> front = EdgeList[i];
        total += front.first; 
        if(!UF.isSameSet(front.second.first, front.second.second)){
            mst_cost += front.first;
            UF.unionSet(front.second.first, front.second.second);
        }
    }
    
    cout<< total - mst_cost <<endl;
    
    return 0;
}
