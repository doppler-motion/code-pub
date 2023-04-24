//
// Created by Yudong Chen on 2023/4/23.
//
#include "stdio.h"

#ifndef C_EXCHANGENUM_H
#define C_EXCHANGENUM_H

void exchangeNum(int a, int b) {
    int tmp;
    printf("交换前：\n");
    printf("a: %d ", a);
    printf("b: %d\n", b);
    tmp = a;
    a = b;
    b = tmp;
    printf("交换后：\n");
    printf("a: %d ", a);
    printf("b: %d\n", b);
}

void exchangeNumByPointer(int *a, int *b) {
    int tmp;
    printf("交换前：\n");
    printf("a: %d ", *a);
    printf("b: %d\n", *b);
    tmp = *a;
    *a = *b;
    *b = tmp;
    printf("交换后：\n");
    printf("a: %d ", *a);
    printf("b: %d\n", *b);
}

void exchangeNumByXOR(int a, int b){
    printf("交换前：\n");
    printf("a: %d, b: %d\n", a, b);
    a = a^b;
    b = a^b;
    a = a^b;
    printf("交换后：\n");
    printf("a: %d, b: %d\n", a, b);
}

#endif //C_EXCHANGENUM_H
