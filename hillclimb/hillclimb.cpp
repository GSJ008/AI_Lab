#include <bits/stdc++.h>
using namespace std;

typedef vector<vector<int>> Board;


int heuristic(Board curr, Board goal) {
    int d = 0;
    int row = curr.size();
    int col = curr[0].size();
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            if (curr[i][j] != goal[i][j]) d++;
        }
    }
    return d;
}


pair<int,int> find_pos(Board s) {
    for (int i = 0; i < s.size(); i++) {
        for (int j = 0; j < s[i].size(); j++) {
            if (s[i][j] == 0) return {i,j};
        }
    }
    return {-1,-1};
}


bool compare(Board a, Board b) {
    return a == b;
}


Board up(Board s) {
    pair<int,int> pos = find_pos(s);
    int row = pos.first;
    int col = pos.second;
    if (row > 0) {
        swap(s[row][col], s[row-1][col]);
    }
    return s;
}

Board down(Board s) {
    pair<int,int> pos = find_pos(s);
    int row = pos.first;
    int col = pos.second;
    if (row < (int)s.size()-1) {
        swap(s[row][col], s[row+1][col]);
    }
    return s;
}

Board left(Board s) {
    pair<int,int> pos = find_pos(s);
    int row = pos.first;
    int col = pos.second;
    if (col > 0) {
        swap(s[row][col], s[row][col-1]);
    }
    return s;
}

Board right(Board s) {
    pair<int,int> pos = find_pos(s);
    int row = pos.first;
    int col = pos.second;
    if (col < (int)s[0].size()-1) {
        swap(s[row][col], s[row][col+1]);
    }
    return s;
}


void search(Board start, Board goal) {
    vector<pair<int,Board>> q;
    vector<Board> visited;

    q.push_back({heuristic(start,goal), start});

    while (!q.empty()) {
        sort(q.begin(), q.end());   
        auto curr = q[0];
        q.erase(q.begin());

        int hval = curr.first;
        Board state = curr.second;

        if (compare(state, goal)) {
            cout << "Found!" << endl;
            cout << "Visited states: " << visited.size() << endl;
            return;
        }

        visited.push_back(state);

        
        vector<Board> children;
        children.push_back(up(state));
        children.push_back(down(state));
        children.push_back(left(state));
        children.push_back(right(state));

        for (auto &child : children) {
            int h = heuristic(child, goal);
            pair<int,Board> node = {h, child};

            
            if (find(visited.begin(), visited.end(), child) == visited.end() &&
                find_if(q.begin(), q.end(), [&](auto &p){ return p.second == child; }) == q.end()) {
                q.push_back(node);
            }
        }

        sort(q.begin(), q.end());
        if (!q.empty() && q[0].first > hval) {
            cout << "Heuristic of child greater than parent: " 
                 << q[0].first << " > " << hval << endl;
            return;
        }
    }

    cout << "Not Found." << endl;
}


int main() {
    Board s = {{1,2,3},{4,5,6},{8,7,0}};
    Board g = {{1,2,3},{4,5,6},{7,8,0}};

    auto start_time = chrono::high_resolution_clock::now();
    search(s,g);
    auto end_time = chrono::high_resolution_clock::now();

    auto duration = chrono::duration_cast<chrono::milliseconds>(end_time - start_time);
    cout << "Execution time: " << duration.count() << " ms" << endl;

    return 0;
}