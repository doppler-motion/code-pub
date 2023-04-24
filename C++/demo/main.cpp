#include <iostream>
using namespace std;

#define LENGTH 10
#define WIDTH 10
#define NEWLINE '\n'

// 函数声明
void func(void);

static int cnt = 10; // 全局变量

int main() {
    cout << "Hello, World!" << std::endl;


    int area;
    area = LENGTH * WIDTH;
    cout << area;
    cout << NEWLINE;

    long long a = 100000000;

    cout << a;
    cout << NEWLINE;

    while(cnt--)
    {
        func();
    }

    return 0;
}

// 函数定义
void func( void )
{
    static int i = 5;  // 局部静态变量
    i++;
    cout << "变量i为" << i;
    cout << " , 变量 count 为 " << cnt << endl;
}