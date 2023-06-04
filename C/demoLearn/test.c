//
// Created by 陈玉东 on 2023/4/5.
//
#include <stdio.h>

// 函数声明
void func(void);

static int count=10;  // 定义全局变量

int main()
{
    while (count--)
    {
        func();
    }
}

void func(void )
{
    int i = 5;
    i++;
    printf(" i 的值为 %d, count的值为： %d\n", i, count);
}
