#include <bits/stdc++.h>
using namespace std;

// Magic square mapping
const int magic[9] = {8,1,6, 3,5,7, 4,9,2};

void printBoard(const vector<char>& b) {
    cout << "\nBoard:\n";
    for (int r = 0; r < 3; ++r) {
        cout << " ";
        for (int c = 0; c < 3; ++c) {
            int i = r * 3 + c;
            cout << (b[i] == ' ' ? char('1' + i) : b[i]);
            if (c < 2) cout << " | ";
        }
        cout << "\n";
        if (r < 2) cout << "---+---+---\n";
    }
    cout << "\n";
}

bool checkWin(const vector<char>& b, char p) {
    int wins[8][3] = {
        {0,1,2},{3,4,5},{6,7,8}, // rows
        {0,3,6},{1,4,7},{2,5,8}, // cols
        {0,4,8},{2,4,6}          // diagonals
    };
    for (auto &line : wins) {
        if (b[line[0]] == p && b[line[1]] == p && b[line[2]] == p) return true;
    }
    return false;
}

vector<int> collectMagic(const vector<char>& board, char player) {
    vector<int> nums;
    for (int i = 0; i < 9; ++i)
        if (board[i] == player) nums.push_back(magic[i]);
    return nums;
}

bool completes15(const vector<int>& nums, int cand) {
    for (int i = 0; i < (int)nums.size(); ++i)
        for (int j = i+1; j < (int)nums.size(); ++j)
            if (nums[i] + nums[j] + cand == 15) return true;
    return false;
}

int computerMove(vector<char>& board) {
    vector<int> aiNums = collectMagic(board, 'O');
    vector<int> humanNums = collectMagic(board, 'X');

    // Win
    for (int i = 0; i < 9; ++i)
        if (board[i] == ' ' && completes15(aiNums, magic[i])) return i;

    // Block
    for (int i = 0; i < 9; ++i)
        if (board[i] == ' ' && completes15(humanNums, magic[i])) return i;

    // Center
    if (board[4] == ' ') return 4;

    // Corner
    for (int idx : {0,2,6,8})
        if (board[idx] == ' ') return idx;

    // Side
    for (int idx : {1,3,5,7})
        if (board[idx] == ' ') return idx;

    // First empty
    for (int i = 0; i < 9; ++i)
        if (board[i] == ' ') return i;

    return -1;
}

int main() {
    vector<char> board(9, ' ');
    bool userTurn = true;
    int moves = 0;

    cout << "Tic-Tac-Toe (Magic Square AI)\n";
    cout << "You are X, computer is O.\n";

    while (true) {
        printBoard(board);

        if (userTurn) {
            cout << "User's turn\n";
            cout << "Your move (1-9): " << flush;
            int pos;
            if (!(cin >> pos)) {
                cerr << " Input error, exiting.\n";
                return 0;
            }
            cerr << " You entered: " << pos << "\n";
            if (pos < 1 || pos > 9 || board[pos-1] != ' ') {
                cout << "Invalid move, try again.\n";
                continue;
            }
            board[pos-1] = 'X';
            moves++;
            if (checkWin(board, 'X')) {
                printBoard(board);
                cout << "You WIN!\n";
                break;
            }
        } else {
            cout << " Computer's turn\n";
            int cm = computerMove(board);
            cerr << " Computer chooses index " << cm << " (pos " << cm+1 << ")\n";
            if (cm == -1) break;
            board[cm] = 'O';
            moves++;
            if (checkWin(board, 'O')) {
                printBoard(board);
                cout << "Computer WINS.\n";
                break;
            }
        }

        if (moves >= 9) {
            printBoard(board);
            cout << "It's a draw.\n";
            break;
        }
        userTurn = !userTurn;
    }

    cout << "Game over.\n";
    return 0;
}