#include <bits/stdc++.h>
using namespace std;

struct Puzzle {
    char state[3][3];
    int parent;
};

char goal[3][3] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', ' '}
};

bool isGoal(char s[3][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (s[i][j] != goal[i][j])
                return false;
    return true;
}

void printState(char s[3][3]) {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            cout << s[i][j] << " ";
        cout << "\n";
    }
    cout << "------\n";
}

string encode(char s[3][3]) {
    string key = "";
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            key += (s[i][j] == ' ') ? '0' : s[i][j];
    return key;
}

vector<Puzzle> genMove(Puzzle p, int parentIndex) {
    int blankX = -1, blankY = -1;
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
        int nx = blankX + dx[k];
        int ny = blankY + dy[k];
        if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
            Puzzle newP;
            for (int r = 0; r < 3; r++)
                for (int c = 0; c < 3; c++)
                    newP.state[r][c] = p.state[r][c];
            swap(newP.state[blankX][blankY], newP.state[nx][ny]);
            newP.parent = parentIndex;
            states.push_back(newP);
        }
    }
    return states;
}

void solve(Puzzle start) {
    vector<Puzzle> allStates;
    stack<int> st;
    set<string> visited;

    start.parent = -1;
    allStates.push_back(start);
    st.push(0);
    visited.insert(encode(start.state));

    while (!st.empty()) {
        int idx = st.top();
        st.pop();
        Puzzle &curr = allStates[idx];

        if (isGoal(curr.state)) {
            cout << "Goal reached!\n";
            vector<int> path;
            for (int i = idx; i != -1; i = allStates[i].parent)
                path.push_back(i);
            reverse(path.begin(), path.end());

            for (int id : path)
                printState(allStates[id].state);

            return;
        }

        vector<Puzzle> moves = genMove(curr, idx);
        for (auto &next : moves) {
            string key = encode(next.state);
            if (!visited.count(key)) {
                visited.insert(key);
                allStates.push_back(next);
                st.push(allStates.size() - 1);
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
