//
// Created by Yudong Chen on 2023/6/9.
//

#ifndef CPP_VECTORUSE_H
#define CPP_VECTORUSE_H
#include "iostream"
#include "vector"

using namespace std;

void vectorUse() {
    // 定义一个vector
    vector<int> ve;
    int i;

    // 输出原始的大小
    cout << "ve size: " << ve.size() << endl;

    // 向vector中添加元素
    for (i = 0; i < 5; i++) {
        ve.push_back(i);
    }

    // 加入元素后的大小
    cout << "after insert nums, ve size: " << ve.size() << endl;

    // 打印元素
    for (int j = 0; j < 5; j++){
        cout << "第 ["<< j <<"] 个元素的值： %d" << ve[j] << endl;
    }

    // 使用迭代器访问元素
    vector<int>::iterator v = ve.begin();
    while (v != ve.end()){
        cout << "value of v =" << *v << endl;
        v++;
    }
}

#endif //CPP_VECTORUSE_H
