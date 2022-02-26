#include <iostream>
#include <string>

using namespace std;

void print_board(char board[3][3])
{
    cout << "-------------"
         << "\n";
    for (int i = 0; i < 3; i++)
    {
        cout << "| ";
        for (int j = 0; j < 3; j++)
        {
            cout << board[i][j] << " | ";
        }
        cout << "\n"
             << "-------------"
             << "\n";
    }
}

int declareWinner(char board[3][3])
{
    int u = 0;
    while (u < 3)
    {
        if (board[u][0] == 'X' && board[u][1] == 'X' && board[u][2] == 'X')
            return 1;
        else if (board[u][0] == 'O' && board[u][1] == 'O' && board[u][2] == 'O')
            return -1;
        if (board[0][u] == 'X' && board[1][u] == 'X' && board[2][u] == 'X')
            return 1;
        else if (board[0][u] == 'O' && board[1][u] == 'O' && board[2][u] == 'O')
            return -1;
        u++;
    }

    if (board[0][0] == 'X' && board[1][1] == 'X' && board[2][2] == 'X')
        return 1;
    else if (board[0][0] == 'O' && board[1][1] == 'O' && board[2][2] == 'O')
        return -1;
    if (board[0][2] == 'X' && board[1][1] == 'X' && board[2][0] == 'X')
        return 1;
    else if (board[0][2] == 'O' && board[1][1] == 'O' && board[2][0] == 'O')
        return -1;
    return 0;
}

int main()
{
    char board[3][3] = {{' ', ' ', ' '}, {' ', ' ', ' '}, {' ', ' ', ' '}};
    int z = 0;
    int x, y;
    int out;

    while (true)
    {
        if (z % 2 == 0)
        {
            print_board(board);
            while (true)
            {
                cout << "enter coordinates \n";
                cin >> x;
                cin >> y;
                if (board[x][y] == ' ')
                {
                    break;
                }
                else
                {
                    cout << "Position taken \n";
                }
            }
            board[x][y] = 'X';
        }

        else
        {
            // while (true)
            // {
            //     cout << "enter coordinates \n";
            //     cin >> x;
            //     cin >> y;
            //     if (board[x][y] == ' ')
            //     {
            //         break;
            //     }
            //     else
            //     {
            //         cout << "Position taken \n";
            //     }
            // }

            while (true)
            {
                x = (rand() % 10) % 3;
                y = (rand() % 10) % 3;
                if (board[x][y] == ' ')
                {
                    break;
                }
            }
            board[x][y] = 'O';
        }

        z++;

        out = declareWinner(board);
        if (out == 1)
        {
            cout << "Player 1 is the winner";
            break;
        }
        else if (out == -1)
        {
            cout << "Player 2 is the winner";
            break;
        }
    }
    return 0;
}
