#include <iostream>
#include <vector>
#include <cmath>
#include <set>
using namespace std;

struct State {
    int x, y;
    double g, h, f;
    bool solved;
    bool isAndNode;
    vector<State*> children;
};

double heuristic(State* s, State* goal) {
    return abs(s->x - goal->x) + abs(s->y - goal->y);
}

void AOStar(State* node, State* goal, vector<State*>& allStates, set<pair<int,int>>& visited) {
    if (node->solved) return;
    if (visited.count({node->x, node->y})) return;
    visited.insert({node->x, node->y});

    vector<State*> successors;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    for (int k = 0; k < 4; k++) {
        int nx = node->x + dx[k];
        int ny = node->y + dy[k];
        if (nx >= 0 && ny >= 0 && nx < 5 && ny < 5) {
            State* child = new State{nx, ny, node->g + 1, 0, 0, false, false};
            child->h = heuristic(child, goal);
            child->f = child->g + child->h;
            successors.push_back(child);
            allStates.push_back(child);
            node->children.push_back(child);
        }
    }

    if (successors.empty()) {
        node->f = 1e9; 
        return;
    }

    double minCost = 1e9;
    for (State* child : node->children) {
        AOStar(child, goal, allStates, visited);
        minCost = min(minCost, child->f);
    }

    node->f = node->g + minCost;
    if (node->x == goal->x && node->y == goal->y) node->solved = true;
}

int main() {
    int sx, sy, gx, gy;
    cout << "Enter start coordinates (x y): ";
    cin >> sx >> sy;
    cout << "Enter goal coordinates (x y): ";
    cin >> gx >> gy;

    State* start = new State{sx, sy, 0, 0, 0, false, false};
    State* goal  = new State{gx, gy, 0, 0, 0, false, false};

    vector<State*> allStates;
    allStates.push_back(start);

    set<pair<int,int>> visited;
    AOStar(start, goal, allStates, visited);

    cout << "Final cost from start to goal: " << start->f << endl;

    for (State* s : allStates) delete s;
    return 0;
}