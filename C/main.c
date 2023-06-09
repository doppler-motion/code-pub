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


// ��������
void exNum();  // ��ֵ����

void sortFunc();  // ������

void pointer();  // ָ��ѧϰ

void operator();  // �����

void tmp();  // ��ʱ���Ժ���

// ��������
int varList[] = {100, 200, 300};
int sortArray[] = {10, 102, 32, 87, 90, 23, 45, 101};  // ��������
int sortArrayLength = (int) sizeof(sortArray) / sizeof(int);


int main() {
    printf("Hello, World!\n");
    printf("����\n");

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
    printf("ָ����������\n");
    char *a[] = {"China", "French", "America", "German"};
    printf("����Ԫ�ص��׵�ַ\n");
    printf("%p %p %p %p\n", a[0], a[1], a[2], a[3]);
    printf("����Ԫ�ص�Ԫ����ĵ�ַ\n");
    printf("%p %p %p %p\n", &a[0], &a[1], &a[2], &a[3]);

    printf("\n------------------\n");
    printf("�Ƚ�forѭ���У�++i��i++������\n");
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
    printf("쳲���������\n");

    int ret;
    ret = fib(FIB_NUM);
    printf("%d��쳲��������к�Ϊ��%d\n", FIB_NUM, ret);
}

void sum0To100() {
    printf("\n------------------\n\n");
    printf("1��100���\n");
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
    //��ֵ����
    printf("\n------------------\n\n");
    printf("��ֵ����\n");
    int a4 = 3, b4 = 5;

    printf("��ͨ����\n");
    exchangeNum(a4, b4);

    printf("����ָ�뽻��\n");
    exchangeNumByPointer(&a4, &b4);

    printf("������򽻻���ֵ\n");
    exchangeNumByXOR(a4, b4);

    printf("a4: %d, b4: %d\n", a4, b4);
}

void sortFunc() {
    printf("\n------------------\n\n");
    printf("ð������\n");

    printf("sortArray ð������ǰ��\n");
    display(sortArray, sortArrayLength);

    bubbleSort(sortArray, sortArrayLength);
    printf("sortArray ð�������\n");
    display(sortArray, sortArrayLength);

    printf("��������\n");
    disorganise(sortArray, sortArrayLength);

    printf("\n------------------\n\n");
    printf("��������\n");

    printf("sortArray ��������ǰ��\n");
    display(sortArray, sortArrayLength);

    // ��������
    quickSort(sortArray, 0, sortArrayLength - 1);
    printf("myArray2 ���������\n");
    display(sortArray, sortArrayLength);
}

void operator() {
    printf("\n------------------\n\n");
    printf("�����Լ������\n");

    int A = 20, C;
    C = A++;
    printf("�ȸ�ֵ�����㣺\n");
    printf("Line 1 - C ��ֵ�� %d\n", C);
    printf("Line 2 - A ��ֵ�� %d\n", A);
    A = 20;
    C = A--;
    printf("Line 3 - C ��ֵ�� %d\n", C);
    printf("Line 4 - A ��ֵ�� %d\n", A);

    printf("�������ֵ��\n");
    A = 20;
    C = ++A;
    printf("Line 5 - C ��ֵ�� %d\n", C);
    printf("Line 6 - A ��ֵ�� %d\n", A);
    A = 20;
    C = --A;
    printf("Line 7 - C ��ֵ�� %d\n", C);
    printf("Line 8 - A ��ֵ�� %d\n", A);

    printf("\n------------------\n\n");
    printf("����ȡֵ����\n");
    int idx = 4;
    int array3[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    printf("array3[idx]: %d\n", array3[idx]);
    printf("array3[idx++]: %d\n", array3[idx++]);
    idx = 4;
    printf("array3[++idx]: %d\n", array3[++idx]);
}

void pointer() {
    printf("\n------------------\n\n");
    printf("��ȡָ�����\n");

    int var = 20; // ʵ�������ı���
    int *ip; // ָ�����
    ip = &var;

    printf("var �����ĵ�ַ��%p\n", &var);
    printf("ip �����ĵ�ַ��%p\n", ip);
    printf("*ip �洢��ֵ��%d\n", *ip);

    printf("\n------------------\n\n");
    printf("ָ�����");
    const int MAX = 3;
    int j, *ptr;

    // ָ���е������ַ
    ptr = varList;
    // ����ָ���ֵ
    for (j = 0; j < MAX; j++) {
        printf("�洢��ַ��varList[%d] = %p\n", j, ptr);
        printf("�洢ֵ��varList[%d] = %d\n", j, *ptr);
        ptr++;
    }

    printf("\n------------------\n\n");
    printf("ָ��ݼ�");

    int k, *ptr_del;
    // �ݼ�ָ���ֵ
    // ָ��Ԫ�����һ��Ԫ��
    ptr_del = &varList[MAX - 1];
    for (k = MAX; k > 0; k--) {
        printf("�洢��ַ��varList[%d] = %p\n", k, ptr_del);
        printf("�洢ֵ��varList[%d] = %d\n", k, *ptr_del);

        ptr_del--;
    }

    printf("\n------------------\n\n");
    printf("ָ��Ƚ�");

    int l = 0, *ptr_compare;

    // �Ƚ�ָ���ֵ
    ptr_compare = varList;
    while (ptr_compare <= &varList[MAX - 2]) {
        printf("�洢��ַ��varList[%d] = %p\n", l, ptr_compare);
        printf("�洢ֵ��varList[%d] = %d\n", l, *ptr_compare);
        // ָ����һ��Ԫ��ֵ
        ptr_compare++;
        l++;
    }

    printf("\n------------------\n\n");
    printf("ָ������\n");

    int *ptr_arr[MAX];
    int i_arr;
    for (i_arr = 0; i_arr < MAX; i_arr++) {
        printf("the value of varList[%d]: %d, pointer address: %p\n", i_arr, varList[i_arr], &varList[i_arr]);
        ptr_arr[i_arr] = &varList[i_arr];
    }
    for (i_arr = 0; i_arr < MAX; i_arr++) {
        printf("ָ������λ�� %d �洢��ַ %p �洢ֵΪ %d\n", i_arr, ptr_arr[i_arr], *ptr_arr[i_arr]);
    }

    printf("\n------------------\n\n");
    printf("ָ��ָ���ָ��\n");

    int var_pointer_pointer;
    int *ptr_pointer_pointer;
    int **ptr_double_pointer;

    var_pointer_pointer = 100;
    ptr_pointer_pointer = &var_pointer_pointer;
    ptr_double_pointer = &ptr_pointer_pointer;

    printf("ͨ��**ptr��ȡֵ\n");
    printf("var_pointer_pointer value : %d, address: %p\n", var_pointer_pointer, &var_pointer_pointer);
    printf("ͨ��*ptr_pointer_pointer ��ȡֵ��%d, ��ַ�ǣ�%p\n", *ptr_pointer_pointer, ptr_pointer_pointer);
    printf("ͨ��**ptr_double_pointer ��ȡֵ��%d, ��ַ�ǣ�%p\n", **ptr_double_pointer, *ptr_double_pointer);

    printf("\n------------------\n\n");
    printf("ָ�봫�ݸ�����\n");

    // ���庬��6��Ԫ�ص�����
    int arr_list1[] = {1, 29, 10, 100, 34, 78};
    int size = 6;
    double avg;

    // ����һ�������ָ����Ϊ����
    avg = getAvg(arr_list1, size);
    printf("������ص�ƽ��ֵ��%f\n", avg);

    printf("��ȡ��ǰʱ��\n");
    unsigned long nowSec;
    getTime(&nowSec);
    printf("��ǰʱ�䣺%ld\n", nowSec);

    printf("\n------------------\n\n");
    printf("��������ָ��\n");
    printf("****************************\n");
    printf("C���Բ�֧�ַ��ؾֲ�������ָ�룬����������̬����\n");
    printf("****************************\n");

    // һ��ָ��������ָ��
    int *p;
    int iP;
    p = getRandom();

    for (iP = 0; iP < 10; iP++) {
        printf("*(p + [%d])��ֵ�ǣ�%d\n", iP, *(p + iP));
    }

    printf("\n------------------\n\n");
    printf("����ָ�룺ָ������ָ�����\n");
    int (*pFunc)(int, int) = &getMax; // &����ȥ��
    int a1 = 29, a2 = 30, a3 = 100, a_max;

    a_max = pFunc(pFunc(a1, a2), a3);
    printf("the max value of a1, a2, a3: %d\n", a_max);

    printf("�ص�����������ָ����Ϊĳ�������Ĳ���\n");

    int myArray[10];
    populate_array(myArray, 10, getNextRandomValue);
    for (int i = 0; i < 10; i++) {
        printf("%d ", myArray[i]);
    }
    printf("\n");
}

