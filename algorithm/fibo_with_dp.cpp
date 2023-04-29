#include <iostream>

long long cache[1000];
long long output;
long long times;

long long fibo_with_dp(long long num)
{
    times++;
    if (num == 1 || num == 2)
    {
        return 1;
    }
    if (cache[num] != -1)
    {
        return cache[num];
    }
    output = fibo_with_dp(num - 1) + fibo_with_dp(num - 2);
    cache[num] = output;
    return output;
}
long long fibo(long long num)
{
    times++;
    if (num == 1 || num == 2)
    {
        return 1;
    }
    return fibo(num - 1) + fibo(num - 2);
}

int main()
{
    // main 함수에서 cache 배열 초기화
    std::memset(cache, -1, sizeof(cache));
    times = 0;
    std::cout << fibo(50) << std::endl;
    std::cout << "재귀 횟수: " << times << std::endl;
    times = 0;
    std::cout << fibo_with_dp(50) << std::endl;
    std::cout << "재귀 횟수: " << times << std::endl;
    return 0;
}