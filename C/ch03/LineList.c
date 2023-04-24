//
// Created by ydchen on 2022/12/7.
//
#include "stdio.h"
#include "stdlib.h"
#include "math.h"
#include "time.h"

#define OK 1
#define ERROR 0
#define TRUE 1
#define FALSE 0

#define MAXSIZE 20  /* 存储空间初始分配量 */
typedef int ElemType;  /* ElemType 可以依据实际情况而定，这里设置为int */

typedef struct {
    ElemType data[MAXSIZE];  /* 数组存放数据元素 */
    int length;  /* 数组当前长度 */
} SqList;

typedef int Status; /* Status是函数的类型，其值是函数返回的状态值，如OK */

Status visit(ElemType c) {
    printf("%d\n", c);
    return OK;
}

/* 初始化顺序线性表 */
Status InitList(SqList *L) {
    L->length = 0;
    return OK;
}

/* 初始条件：顺序线性表已存在。操作结果：若线性表为空返回True，否则返回FALSE */
Status ListEmpty(SqList L) {
    if (L.length == 0)
        return TRUE;
    else
        return FALSE;
}

/* 初始条件：线性表L已存在。操作结果，将线性表置为空 */
Status ClearList(SqList *L) {
    L->length = 0;
    return OK;
}

/* 初始条件： 线性表L已存在。操作结果，返回列表的长度 */
Status ListLength(SqList L) {
    return L.length;
}

/* 初始条件： 线性表L已存在。 1<=i<=ListLength(L) */
/* 操作结果：用e返回位置i的值，注意i是指位置，第1个位置的数组是从0开始 */
Status GetItem(SqList L, int i, ElemType *e) {
    if (L.length == 0 || i < 1 || i > L.length)
        return ERROR;
    *e = L.data[i - 1];

    return OK;
}

/* 初始条件： 线性表L已存在。*/
/* 操作结果：返回L中第1个与e满足关系的数据元素的位序 */
/* 若这样的数据不存在，返回0 */
int LocateElem(SqList L, ElemType e) {
    int i;
    if (L.length == 0)
        return 0;
    for (i = 0; i < L.length; i++) {
        if (L.data[i] == e)
            break;
    }
    if (i > L.length)
        return 0;
    return i + 1;
}


/* 初始条件： 线性表L已存在。 1<=i<=ListLength(L) */
/* 操作结果：在L中第i个位置插入新的元素e，L的长度加1 */
Status ListInsert(SqList *L, int i, ElemType e) {
    int k;
    if (L->length == MAXSIZE)  /* 顺序线性表已经满 */
        return ERROR;
    if (i < 1 || i > L->length + 1) /* 当i比第1个位置小或者比最后一位值还要大时 */
        return ERROR;
    if (i <= L->length)  /* 若插入元素在表尾 */
    {
        for (k = L->length - 1; k >= i - 1; k--)   /* 将要插入位置之后的数据元素向后移动一位 */
        {
            L->data[k + 1] = L->data[k];
        }
    }
    L->data[i - 1] = e;  /* 将新元素插入 */
    L->length++;

    return OK;
}

/* 初始条件： 线性表L已存在。 1<=i<=ListLength(L) */
/* 操作结果：在L中第i个位置删除元素e，L的长度减1 */
Status ListDelete(SqList *L, int i, ElemType *e) {
    int k;
    if (L->length == 0)  /* 顺序线性表长度为0 */
        return ERROR;
    if (i < 1 || i > L->length + 1) /* 当i比第1个位置小或者比最后一位值还要大时，删除位置不正确 */
        return ERROR;
    *e = L->data[i - 1];
    if (i <= L->length)  /* 若删除元素不在表尾 */
    {
        for (k = i; k < L->length; k++)   /* 将要删除位置之后的数据元素向前移动一位 */
        {
            L->data[k - 1] = L->data[k];
        }
    }
    L->length--;

    return OK;
}


/* 初始条件： 线性表L已存在。 1<=i<=ListLength(L) */
/* 操作结果：依次输出L中的每个元素 */
Status ListTraverse(SqList L) {
    int i;
    for (i = 0; i < L.length; i++) {
        visit(L.data[i]);
    }
    printf("\n");
    return OK;
}

/* 初始条件： 线性表L已存在。 1<=i<=ListLength(L) */
/* 操作结果：将所有在线性表Lb中不在La中的数据元素插入到La中 */
void unionL(SqList *La, SqList Lb) {
    int La_len, Lb_len, i;
    ElemType e;  /* 声明La和Lb中相同的数据元素 */
    La_len = ListLength(*La);  /* 求线性表的长度 */
    Lb_len = ListLength(Lb);
    for (i = 0; i < Lb.length; i++) {
        GetItem(Lb, i, &e);
        if (!LocateElem(*La, e))
            ListInsert(La, ++La_len, e);
    }
    printf("\n");
}


int main() {
    SqList L;
    SqList Lb;

    ElemType e;
    Status s;
    int j, k;
    s = InitList(&L);
    printf("初始化L后：L.length=%d\n", L.length);

    for (j = 1; j <= 5; j++)
        s = ListInsert(&L, 1, j);
    printf("s: %d\n", s);
    printf("在L的表头依次插入1~5后，L.data=\n");
    ListTraverse(L);

    printf("Now L.length=%d\n", L.length);

    s = ListDelete(&L, 2, &e);
    printf("delete one element status : %d\n", s);
    printf("after delete element: \n");
    ListTraverse(L);
    printf("after delete element , L.length: %d\n", L.length);

    s = ListEmpty(L);
    printf("if List is empty status: %d\n", s);

    k = ListLength(L);
    for (j = 3; j <= 6; j++) {
        s = GetItem(L, j, &e);
        if (s == TRUE)
            printf("该位置%d元素为%d\n", j, e);
        else
            printf("该位置%d没有元素\n", j);
    }

    for(j=3;j<=6;j++)
    {
        s = LocateElem(L, j);
        if (s==ERROR)
            printf("列表中没有这个元素\n");
        else
            printf("元素%d的位置为%d\n", j, s);

    }

    s = ClearList(&L);
    printf("clear all element status: %d\n", s);
    printf("now L.length: %d\n", L.length);

    s = ListEmpty(L);
    printf("if list is empty: %d\n", s);

    for (j = 1; j <= 10; j++)
        ListInsert(&L, j, e);
    printf("Now L.length : %d\n", L.length);

    s = InitList(&Lb);
    for (j = 6; j <= 15; j++)
        ListInsert(&Lb, 1, e);
    printf("Now Lb length : %d\n", Lb.length);

    k=0;
    k++;
    printf("k : %d\n", k);

    return TRUE;
}


