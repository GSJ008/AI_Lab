#include <bits/stdc++.h>
using namespace std;

struct Puzzle {
    char state[3][3];
    int parent;
    int h;
};

char goal[3][3] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', ' '}
};

int heuristic(char s[3][3]) {
    int dist = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (s[i][j] != ' ') {
                int val = s[i][j] - '1';
                int goalX = val / 3;
                int goalY = val % 3;
                dist += abs(i - goalX) + abs(j - goalY);
            }
        }
    }
    return dist;
}

bool isGoal(char s[3][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (s[i][j] != goal[i][j])
                return false;
    return true;
}

string encode(char s[3][3]) {
    string key = "";
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            key += (s[i][j] == ' ') ? '0' : s[i][j];
    return key;
}

vector<Puzzle> genMove(Puzzle p, int parentIndex) {
    int blankX, blankY;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (p.state[i][j] == ' ') {
                blankX = i;
                blankY = j;
            }

    int dx[] = {-1, 1, 0, 0};
    int dy[] = {0, 0, -1, 1};

    vector<Puzzle> states;
    for (int k = 0; k < 4; k++) {
        int nx = blankX + dx[k], ny = blankY + dy[k];
        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
            Puzzle newP;
            for (int r = 0; r < 3; r++)
                for (int c = 0; c < 3; c++)
                    newP.state[r][c] = p.state[r][c];
            swap(newP.state[blankX][blankY], newP.state[nx][ny]);
            newP.parent = parentIndex;
            newP.h = heuristic(newP.state);
            states.push_back(newP);
        }
    }
    return states;
}

void solve(Puzzle start) {
    struct cmp {
        bool operator()(const pair<int,int> &a, const pair<int,int> &b) {
            return a.first > b.first;
        }
    };

    vector<Puzzle> allStates;
    priority_queue<pair<int,int>, vector<pair<int,int>>, cmp> pq;
    set<string> visited;

    start.parent = -1;
    start.h = heuristic(start.state);
    allStates.push_back(start);
    pq.push({start.h, 0});
    visited.insert(encode(start.state));

    while (!pq.empty()) {
        int idx = pq.top().second;
        pq.pop();
        Puzzle &curr = allStates[idx];

        if (isGoal(curr.state)) {
            cout << "Goal reached in " << idx << " steps\n";
            vector<int> path;
            for (int i = idx; i != -1; i = allStates[i].parent)
                path.push_back(i);
            reverse(path.begin(), path.end());

            for (int id : path) {
                for (int r = 0; r < 3; r++) {
                    for (int c = 0; c < 3; c++)
                        cout << allStates[id].state[r][c] << " ";
                    cout << "\n";
                }
                cout << "------\n";
            }
            return;
        }

        vector<Puzzle> moves = genMove(curr, idx);
        for (auto &next : moves) {
            string key = encode(next.state);
            if (!visited.count(key)) {
                visited.insert(key);
                allStates.push_back(next);
                pq.push({next.h, allStates.size() - 1});
            }
        }
    }
    cout << "No solution\n";
}

int main() {
    Puzzle start = {
        {{'1', '2', '3'},
         {'4', ' ', '6'},
         {'7', '5', '8'}}
    };
    solve(start);
    return 0;
}
