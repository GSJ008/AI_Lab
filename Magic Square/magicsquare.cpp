#include <bits/stdc++.h>
using namespace std;


vector<vector<int>> generateOdd(int n){
    vector<vector<int>> mat(n, vector<int>(n, 0)); 
    int i = n / 2;
    int j = n - 1;

    for (int num = 1; num <= n * n; num++){
        mat[i][j] = num;
        if(num % n == 0) {
            j--;
        }
        else{
            i--; j++;
        }
        i += n; i %= n;
        j += n; j %= n;
    }
    return mat;
}

vector<vector<int>> generateDoublyEven(int n) {
    vector<vector<int>> mat(n, vector<int>(n));
    int num = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            mat[i][j] = num++;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if ((i % 4 == j % 4) || ((i % 4) + (j % 4) == 3)) {
                mat[i][j] = n * n + 1 - mat[i][j];
            }
        }
    }
    return mat;
}

vector<vector<int>> generateSinglyEven(int n) {
    int halfN = n / 2;
    int subSquareSize = halfN * halfN;
    vector<vector<int>> subSquare = generateOdd(halfN);
    vector<vector<int>> mat(n, vector<int>(n, 0));

    for (int i = 0; i < halfN; i++) {
        for (int j = 0; j < halfN; j++) {
            int val = subSquare[i][j];
            mat[i][j] = val;
            mat[i + halfN][j + halfN] = val + subSquareSize;
            mat[i][j + halfN] = val + 2 * subSquareSize;
            mat[i + halfN][j] = val + 3 * subSquareSize;
        }
    }

    int k = (n - 2) / 4;
    for (int i = 0; i < halfN; i++) {
        for (int j = 0; j < k; j++) {
            swap(mat[i][j], mat[i + halfN][j]);
        }
        for (int j = n - k + 1; j < n; j++) {
            swap(mat[i][j], mat[i + halfN][j]);
        }
    }

    swap(mat[k][0], mat[k + halfN][0]);
    swap(mat[k][k], mat[k + halfN][k]);

    return mat;
}

vector<vector<int>> generateMagicSquare(int n) {
    if (n % 2 == 1) return generateOdd(n);
    if (n % 4 == 0) return generateDoublyEven(n);
    return generateSinglyEven(n);
}

int main() {
    int n;
    cout<<"Enter order of magic square: ";
    cin>>n;
    if(n<3){
        cout<<"Magic square not possible for n < 3"<<endl;
        return 0;
    }
    vector<vector<int>> magicSquare = generateMagicSquare(n);
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << magicSquare[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}