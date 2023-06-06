#include "stdio.h"
#include "demoLearn//utils_test.h"
#include "demoLearn/sortFunc.h"
#include "demoLearn/exchangeNum.h"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

#define WIDTH 9
#define LENGTH 10
#define NEWLINE "\n"

#define FIB_NUM 10


// 函数声明
void exNum();  // 数值交换

void sortFunc();  // 排序函数

void pointer();  // 指针学习

void operator();  // 运算符

void tmp();  // 临时测试函数

// 变量声明
int varList[] = {100, 200, 300};
int sortArray[] = {10, 102, 32, 87, 90, 23, 45, 101};  // 排序数组
int sortArrayLength = (int) sizeof(sortArray) / sizeof(int);


int main() {
    printf("Hello, World!\n");
    printf("中文\n");

    tmp();

//    exNum();
//    sortFunc();

    return TRUE;
}

void tmp() {
    int area;
    area = WIDTH * LENGTH;
    printf("the value of area: %d", area);
    printf(NEWLINE);

    printf("\n------------------\n");
    printf("指针数组的理解\n");
    char *a[] = {"China", "French", "America", "German"};
    printf("数组元素的首地址\n");
    printf("%p %p %p %p\n", a[0], a[1], a[2], a[3]);
    printf("数组元素单元本身的地址\n");
    printf("%p %p %p %p\n", &a[0], &a[1], &a[2], &a[3]);

    printf("\n------------------\n");
    printf("比较for循环中，++i，i++的区别\n");
    int maxSize = 10;
    for (int i=0; i < maxSize; ++i){
        printf("%d ", i);
    }
    printf("\n");
    for (int i=0; i < maxSize; i++){
        printf("%d ", i);
    }
    printf("\n");

}

void fibTest() {
    printf("\n------------------\n\n");
    printf("斐波那契数列\n");

    int ret;
    ret = fib(FIB_NUM);
    printf("%d阶斐波纳契数列和为：%d\n", FIB_NUM, ret);
}

void sum0To100() {
    printf("\n------------------\n\n");
    printf("1到100求和\n");
    int sum = 0, n = 100;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("sum: %d\n", sum);

    int sum1, m = 100;
    sum1 = (1 + m) * m / 2;
    printf("sum1: %d\n", sum1);
}

void exNum() {
    //数值交换
    printf("\n------------------\n\n");
    printf("数值交换\n");
    int a4 = 3, b4 = 5;

    printf("普通交换\n");
    exchangeNum(a4, b4);

    printf("利用指针交换\n");
    exchangeNumByPointer(&a4, &b4);

    printf("利用异或交换数值\n");
    exchangeNumByXOR(a4, b4);

    printf("a4: %d, b4: %d\n", a4, b4);
}

void sortFunc() {
    printf("\n------------------\n\n");
    printf("冒泡排序\n");

    printf("sortArray 冒泡排序前：\n");
    display(sortArray, sortArrayLength);

    bubbleSort(sortArray, sortArrayLength);
    printf("sortArray 冒泡排序后：\n");
    display(sortArray, sortArrayLength);

    printf("打乱数组\n");
    disorganise(sortArray, sortArrayLength);

    printf("\n------------------\n\n");
    printf("快速排序\n");

    printf("sortArray 快速排序前：\n");
    display(sortArray, sortArrayLength);

    // 快速排序
    quickSort(sortArray, 0, sortArrayLength - 1);
    printf("myArray2 快速排序后：\n");
    display(sortArray, sortArrayLength);
}

void operator() {
    printf("\n------------------\n\n");
    printf("自增自减运算符\n");

    int A = 20, C;
    C = A++;
    printf("先赋值后运算：\n");
    printf("Line 1 - C 的值是 %d\n", C);
    printf("Line 2 - A 的值是 %d\n", A);
    A = 20;
    C = A--;
    printf("Line 3 - C 的值是 %d\n", C);
    printf("Line 4 - A 的值是 %d\n", A);

    printf("先运算后赋值：\n");
    A = 20;
    C = ++A;
    printf("Line 5 - C 的值是 %d\n", C);
    printf("Line 6 - A 的值是 %d\n", A);
    A = 20;
    C = --A;
    printf("Line 7 - C 的值是 %d\n", C);
    printf("Line 8 - A 的值是 %d\n", A);

    printf("\n------------------\n\n");
    printf("数组取值检验\n");
    int idx = 4;
    int array3[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    printf("array3[idx]: %d\n", array3[idx]);
    printf("array3[idx++]: %d\n", array3[idx++]);
    idx = 4;
    printf("array3[++idx]: %d\n", array3[++idx]);
}

void pointer() {
    printf("\n------------------\n\n");
    printf("获取指针变量\n");

    int var = 20; // 实际声明的变量
    int *ip; // 指针变量
    ip = &var;

    printf("var 变量的地址：%p\n", &var);
    printf("ip 变量的地址：%p\n", ip);
    printf("*ip 存储的值：%d\n", *ip);

    printf("\n------------------\n\n");
    printf("指针递增");
    const int MAX = 3;
    int j, *ptr;

    // 指针中的数组地址
    ptr = varList;
    // 递增指针的值
    for (j = 0; j < MAX; j++) {
        printf("存储地址：varList[%d] = %p\n", j, ptr);
        printf("存储值：varList[%d] = %d\n", j, *ptr);
        ptr++;
    }

    printf("\n------------------\n\n");
    printf("指针递减");

    int k, *ptr_del;
    // 递减指针的值
    // 指向元组最后一个元素
    ptr_del = &varList[MAX - 1];
    for (k = MAX; k > 0; k--) {
        printf("存储地址：varList[%d] = %p\n", k, ptr_del);
        printf("存储值：varList[%d] = %d\n", k, *ptr_del);

        ptr_del--;
    }

    printf("\n------------------\n\n");
    printf("指针比较");

    int l = 0, *ptr_compare;

    // 比较指针的值
    ptr_compare = varList;
    while (ptr_compare <= &varList[MAX - 2]) {
        printf("存储地址：varList[%d] = %p\n", l, ptr_compare);
        printf("存储值：varList[%d] = %d\n", l, *ptr_compare);
        // 指向上一个元素值
        ptr_compare++;
        l++;
    }

    printf("\n------------------\n\n");
    printf("指针数组\n");

    int *ptr_arr[MAX];
    int i_arr;
    for (i_arr = 0; i_arr < MAX; i_arr++) {
        printf("the value of varList[%d]: %d, pointer address: %p\n", i_arr, varList[i_arr], &varList[i_arr]);
        ptr_arr[i_arr] = &varList[i_arr];
    }
    for (i_arr = 0; i_arr < MAX; i_arr++) {
        printf("指针数据位置 %d 存储地址 %p 存储值为 %d\n", i_arr, ptr_arr[i_arr], *ptr_arr[i_arr]);
    }

    printf("\n------------------\n\n");
    printf("指向指针的指针\n");

    int var_pointer_pointer;
    int *ptr_pointer_pointer;
    int **ptr_double_pointer;

    var_pointer_pointer = 100;
    ptr_pointer_pointer = &var_pointer_pointer;
    ptr_double_pointer = &ptr_pointer_pointer;

    printf("通过**ptr获取值\n");
    printf("var_pointer_pointer value : %d, address: %p\n", var_pointer_pointer, &var_pointer_pointer);
    printf("通过*ptr_pointer_pointer 获取值：%d, 地址是：%p\n", *ptr_pointer_pointer, ptr_pointer_pointer);
    printf("通过**ptr_double_pointer 获取值：%d, 地址是：%p\n", **ptr_double_pointer, *ptr_double_pointer);

    printf("\n------------------\n\n");
    printf("指针传递给函数\n");

    // 定义含有6个元素的数组
    int arr_list1[] = {1, 29, 10, 100, 34, 78};
    int size = 6;
    double avg;

    // 传递一个数组的指针作为参数
    avg = getAvg(arr_list1, size);
    printf("输出返回的平均值：%f\n", avg);

    printf("获取当前时间\n");
    unsigned long nowSec;
    getTime(&nowSec);
    printf("当前时间：%ld\n", nowSec);

    printf("\n------------------\n\n");
    printf("函数返回指针\n");
    printf("****************************\n");
    printf("C语言不支持返回局部变量的指针，除非声明静态变量\n");
    printf("****************************\n");

    // 一个指向整数的指针
    int *p;
    int iP;
    p = getRandom();

    for (iP = 0; iP < 10; iP++) {
        printf("*(p + [%d])的值是：%d\n", iP, *(p + iP));
    }

    printf("\n------------------\n\n");
    printf("函数指针：指向函数的指针变量\n");
    int (*pFunc)(int, int) = &getMax; // &可以去掉
    int a1 = 29, a2 = 30, a3 = 100, a_max;

    a_max = pFunc(pFunc(a1, a2), a3);
    printf("the max value of a1, a2, a3: %d\n", a_max);

    printf("回调函数：函数指针作为某个函数的参数\n");

    int myArray[10];
    populate_array(myArray, 10, getNextRandomValue);
    for (int i = 0; i < 10; i++) {
        printf("%d ", myArray[i]);
    }
    printf("\n");
}

