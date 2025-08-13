#include <iostream>
using namespace std;

int x, y;
int amount_x = 0, amount_y = 0;

void fill_x() {
    amount_x = x;
}

void fill_y() {
    amount_y = y;
}

void empty_x() {
    amount_x = 0;
}

void empty_y() {
    amount_y = 0;
}

void pour_x_to_y() {
    int pour = min(amount_x, y - amount_y);
    amount_x -= pour;
    amount_y += pour;
}

void pour_y_to_x() {
    int pour = min(amount_y, x - amount_x);
    amount_y -= pour;
    amount_x += pour;
}

bool reached_goal(int goal) {
    return (amount_x == goal || amount_y == goal);
}

void solve_jugs(int goal) {
    amount_x = 0;
    amount_y = 0;

    while (!reached_goal(goal)) {
        if (amount_x == 0) {
            fill_x();
        } else if (amount_y == y) {
            empty_y();
        } else {
            pour_x_to_y();
        }
        cout << "(" << amount_x << ", " << amount_y << ")\n";
    }
}

int main() {
    cout << "Enter capacity of jug x: ";
    cin >> x;
    cout << "Enter capacity of jug y: ";
    cin >> y;
    cout << "Enter goal volume: ";
    int goal;
    cin >> goal;

    int a = x, b = y;
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    int gcd_val = a;

    if (goal > max(x, y) || goal % gcd_val != 0) {
        cout << "Goal not achievable with given jug sizes.\n";
        return 0;
    }

    cout << "Starting state:\n";
    cout << "(" << amount_x << ", " << amount_y << ")\n";

    solve_jugs(goal);

    cout << "Goal " << goal << " reached.\n";
    return 0;
}