#include <iostream>
#include <vector>
using namespace std;

int input;
int wons[4] = {500, 100, 50, 10};

vector<int> calc_coin(int money)
{
    vector<int> coins = vector<int>(4);
    coins[0] = money / 500;
    coins[1] = (money % 500) / 100;
    coins[2] = (money % 100) / 50;
    coins[3] = (money % 50) / 10;

    return coins;
}

int main()
{
    cout << "**잔돈 드립니다**" << endl;
    cout << "얼마를 드릴까요? : ";
    cin >> input;
    vector<int> amount = calc_coin(input);
    for (int i = 0; i < 4; i++)
    {
        cout << wons[i] << "원 : " << amount.at(i) << "개" << endl;
    }
    return 0;
}
