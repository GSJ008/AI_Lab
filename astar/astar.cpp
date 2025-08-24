#include <bits/stdc++.h>
using namespace std;

struct Node {
    int x, y;
    double g, f;
    bool operator<(const Node &other) const {
        if (f == other.f) {
            if (g == other.g) {
                if (x == other.x) return y < other.y;
                return x < other.x;
            }
            return g < other.g;
        }
        return f < other.f;
    }
};

int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1};
int dy[8] = {0, 0, 1, -1, 1, -1, 1, -1};
double cost[8] = {1, 1, 1, 1, 1.5, 1.5, 1.5, 1.5};

double heuristic(int x1, int y1, int x2, int y2) {
    int dx_ = abs(x1 - x2);
    int dy_ = abs(y1 - y2);
    int dmin = min(dx_, dy_);
    int dmax = max(dx_, dy_);
    return dmin * 1.5 + (dmax - dmin) * 1.0;
}

bool inBounds(int x, int y, int n, int m) {
    return (0 <= x && x < n && 0 <= y && y < m);
}

vector<pair<int,int>> Astar(vector<vector<int>> &grid, pair<int,int> start, pair<int,int> goal) {
    int n = grid.size(), m = grid[0].size();

    vector<vector<double>> g(n, vector<double>(m, 1e9));
    vector<vector<pair<int,int>>> parent(n, vector<pair<int,int>>(m, {-1,-1}));

    set<Node> openSet;

    g[start.first][start.second] = 0;
    openSet.insert({start.first, start.second, 0, heuristic(start.first, start.second, goal.first, goal.second)});

    while (!openSet.empty()) {
        Node cur = *openSet.begin();
        openSet.erase(openSet.begin());

        int x = cur.x, y = cur.y;

        if (make_pair(x,y) == goal) {
            vector<pair<int,int>> path;
            while (x != -1 && y != -1) {
                path.push_back({x,y});
                auto p = parent[x][y];
                x = p.first; y = p.second;
            }
            reverse(path.begin(), path.end());
            return path;
        }
// hello
        for (int i = 0; i < 8; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (!inBounds(nx, ny, n, m)) continue;
            if (grid[nx][ny] == 1) continue;

            double ng = g[cur.x][cur.y] + cost[i];
            if (ng < g[nx][ny]) {
                auto it = openSet.find({nx, ny, g[nx][ny], g[nx][ny] + heuristic(nx,ny,goal.first,goal.second)});
                if (it != openSet.end()) openSet.erase(it);

                g[nx][ny] = ng;
                parent[nx][ny] = {x,y};
                double f = ng + heuristic(nx, ny, goal.first, goal.second);
                openSet.insert({nx, ny, ng, f});
            }
        }
    }
    return {};
}

int main() {
    int n, m;
    cout << "Enter grid size (rows cols): ";
    cin >> n >> m;

    vector<vector<int>> grid(n, vector<int>(m, 0));

    int sx, sy, gx, gy;
    cout << "Enter start (row col): ";
    cin >> sx >> sy;
    sx--; sy--;

    cout << "Enter goal (row col): ";
    cin >> gx >> gy;
    gx--; gy--;

    int r;
    cout << "Enter number of river cells: ";
    cin >> r;
    cout << "Enter river cells (row col) one by one:\n";
    for (int i = 0; i < r; i++) {
        int rx, ry;
        cin >> rx >> ry;
        rx--; ry--;
        grid[rx][ry] = 1;
    }

    pair<int,int> start = {sx, sy};
    pair<int,int> goal = {gx, gy};

    vector<pair<int,int>> path = Astar(grid, start, goal);

    if (path.empty()) {
        cout << "No path found!\n";
    } else {
        cout << "Path found:\n";
        for (auto &p : path) {
            int x = p.first, y = p.second;
            cout << "(" << x+1 << "," << y+1 << ") ";
            if (!(p == start) && !(p == goal)) {
                grid[x][y] = 2;
            }
        }
        cout << "\n";

        cout << "\nGrid:\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == sx && j == sy) cout << "S ";
                else if (i == gx && j == gy) cout << "G ";
                else if (grid[i][j] == 1) cout << "# ";
                else if (grid[i][j] == 2) cout << "* ";
                else cout << ". ";
            }
            cout << "\n";
        }
    }
    return 0;
}
