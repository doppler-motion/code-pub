//
// Created by Yudong Chen on 2023/4/23.
//

#include "stdio.h"
#include "stdlib.h"

#ifndef C_SORTFUNC_H
#define C_SORTFUNC_H


void bubbleSort(int array[], int length);

void quickSort(int array[], int left, int right);

// 快速排序, 形参列表为数组，左指针位置，右指针位置，int array[]等价于int *array
void quickSort(int array[], int left, int right) {
    int i = left;
    int j = right;
    int temp = array[left];

    if (i > j) {
        return;
    }

    while (i < j) {
        while (i < j && array[j] >= temp)  // 从右往左寻找小于temp的元素
        {
            j--;
        }

        if (i < j) {
            array[i++] = array[j];
        }

        while (i < j && array[i] < temp)  // 从左往右寻找大于temp的元素
        {
            i++;
        }

        if (i < j) {
            array[j--] = array[i];
        }
    }

    array[i] = temp;

    // 递归调用
    quickSort(array, left, i - 1);  // 排序temp的左边
    quickSort(array, i + 1, right);  // 排序temp的右边

}

// 冒泡排序
void bubbleSort(int array[], int length) {
    int i, j, temp;
    for (i = 0; i < length; i++) {
        for (j = i; j < length; j++) {
            if (array[i] > array[j]) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }
}

#endif //C_SORTFUNC_H
