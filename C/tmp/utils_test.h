//
// Created by 陈玉东 on 2023/4/9.
//
#include "stdlib.h"
#include "time.h"
#include "stdio.h"
#include "exchangeNum.h"

#ifndef C_UTILS_TEST_H
#define C_UTILS_TEST_H

// 函数声明
double getAvg(int *arr, int size);

int getMax(int, int);

int getMin(int, int );

int *getRandom();

void getTime(unsigned long *var);

void populate_array(int *array, size_t arraySize, int (*getNextValue)(void));

int getNextRandomValue(void);

int fib(int n);

void display(int array[], int length);



// 函数定义

// 打印数组中的值
void display(int array[], int length) {
    for (int idx = 0; idx < length; idx++) {
        printf("%d ", array[idx]);
    }
    printf("\n");
}

// 随机打乱数组
void disorganise(int array[], int length){
    srand(time(NULL)); // 随机数种子
    int rN1 = (rand() % length);
    int rN2 = (rand() % length);
    for (int i=0; i<20; i++){
        if(rN1 != rN2){
            exchangeNumByPointer(&array[rN1], &array[rN2]);
        }
        rN1 = (rand() % length);
        rN2 = (rand() % length);
    }
}


// 获取数组数值平均值
double getAvg(int *arr, int size) {
    int i, sum = 0;
    double avg;
    for (i = 0; i < size; ++i) {
        sum += arr[i];
    }

    avg = (double) sum / size;

    return avg;
}

// 获取的当前的秒数
void getTime(unsigned long *var) {
    // 获取当前的秒数
    *var = time(NULL);
    return;
}

// 定义函数,生成和返回随机数
int *getRandom() {
    static int r[10];
    int i;

    // 设置随机数种子
    srand((unsigned) time(NULL));
    for (i = 0; i < 10; ++i) {
        r[i] = rand();
        printf("%d\n", r[i]);
    }

    return r;
}

// 获取最大值
int getMax(int a, int b) {
    return a > b ? a : b;
}

// 获取最小值
int getMin(int a, int b) {
    return a > b ? b : a;
}

//
void populate_array(int *array, size_t arraySize, int (*getNextValue)(void)) {
    for (size_t i = 0; i < arraySize; i++)
        array[i] = getNextValue();
}

// 获取随机值
int getNextRandomValue(void) {
    return rand();
}

// 斐波那契数列函数
int fib(int n) {
    if (n == 1 || n == 2) {
        return 1;
    } else {
        return fib(n - 2) + fib(n - 1);
    }
}


#endif //C_UTILS_TEST_H
