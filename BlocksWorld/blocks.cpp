#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;

struct State {
    vector<pair<char, string>> on;
    vector<string> moves;
};

bool isGoal(const State &s, const vector<pair<char, string>> &goal) {
    for (auto &g : goal) {
        char block = g.first;
        string target = g.second;
        bool found = false;
        for (auto &p : s.on) {
            if (p.first == block && p.second == target) {
                found = true;
                break;
            }
        }
        if (!found) return false;
    }
    return true;
}


vector<char> getClearBlocks(const State &s) {
    vector<char> allBlocks;
    vector<char> hasSomethingOnTop;
    for (auto &p : s.on) {
        allBlocks.push_back(p.first);
        if (p.second != "Table") {
            hasSomethingOnTop.push_back(p.second[0]);
        }
    }
    vector<char> clear;
    for (char b : allBlocks) {
        if (find(hasSomethingOnTop.begin(), hasSomethingOnTop.end(), b) == hasSomethingOnTop.end()) {
            clear.push_back(b);
        }
    }
    return clear;
}

vector<State> Children(const State &current) {
    vector<State> nextStates;
    vector<char> clear = getClearBlocks(current);
    for (char x : clear) {
        string under;
        for (auto &p : current.on) {
            if (p.first == x) {
                under = p.second;
                break;
            }
        }
        if (under != "Table") {
            State newState = current;
            for (auto &p : newState.on) {
                if (p.first == x) {
                    p.second = "Table";
                    break;
                }
            }
            string move = "Move " + string(1, x) + " to Table";
            newState.moves.push_back(move);
            nextStates.push_back(newState);
        }
        for (char y : clear) {
            if (y == x) continue;
            State newState = current;
            for (auto &p : newState.on) {
                if (p.first == x) {
                    p.second = string(1, y);
                    break;
                }
            }
            string move = "Move " + string(1, x) + " onto " + string(1, y);
            newState.moves.push_back(move);
            nextStates.push_back(newState);
        }
    }
    return nextStates;
}

bool dfs(State start, const vector<pair<char, string>> &goal, int depthLimit) {
    stack<State> st;
    st.push(start);
    while (!st.empty()) {
        State current = st.top();
        st.pop();
        if (isGoal(current, goal)) {
            cout << "Goal reached!\nSequence of moves:\n";
            for (auto &m : current.moves) {
                cout << m << endl;
            }
            return true;
        }
        if ((int)current.moves.size() < depthLimit) {
            vector<State> nextStates = Children(current);
            for (auto &ns : nextStates) {
                st.push(ns);
            }
        }
    }
    return false;
}

int main() {
    int n;
    cout << "Enter number of blocks: ";
    cin >> n;
    State start;
    vector<pair<char, string>> goal;
    cout << "\nEnter start state (format: Block On):\n";
    for (int i = 0; i < n; i++) {
        char block;
        string on;
        cin >> block >> on;
        start.on.push_back({block, on});
    }
    cout << "\nEnter goal state (format: Block On):\n";

    for (int i = 0; i < n; i++) {
        char block;
        string on;
        cin >> block >> on;
        goal.push_back({block, on});
    }
    int depthLimit;
    cout << "\nEnter depth limit: ";
    cin >> depthLimit;
    if (!dfs(start, goal, depthLimit)) {
        
        cout << "Goal not found within depth limit.\n";
    }
    return 0;
}
