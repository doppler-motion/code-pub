//
// Created by Yudong Chen on 2023/6/12.
//

#ifndef CPP_SIMPLEUSE_H
#define CPP_SIMPLEUSE_H

#include <utility>

#include "iostream"
#include "string"

using namespace std;

// 暴力实现
class StudentFunc1 {
public:
    void setStudent(string num, int chi, int mat, int eng) {
        number = std::move(num);
        Chinese = chi;
        Math = mat;
        English = eng;
    }

    static int avery(StudentFunc1 &s) {
        return (s.Chinese + s.Math + s.English) / 3;
    }

    static bool pass(StudentFunc1 &s) {
        bool f = false;
        if (!(s.Chinese < 60 || s.English < 60 || s.Math < 60)) {
            f = true;
        }
        return f;
    }

private:
    string number;
    int Chinese{}, Math{}, English{};
};


// 使用 this 优化
class StudentFunc2
{
public:
    StudentFunc2(string num, int chi, int mat, int eng)
    {
        this -> number = std::move(num);
        this -> Chinese = chi;
        this -> Math = mat;
        this -> English = eng;
    }

    [[nodiscard]] int avery() const
    {
        return (Chinese + Math + English) / 3;
    }

    bool pass() const
    {
        bool f = false;
        if (!(Chinese < 60 || Math < 60 || English < 60))
        {
            f = true;
        }
        return f;
    }

private:
    string number;
    int Chinese, Math, English;
};


void classFunc1() {
    StudentFunc1 student;
    string number;
    int Chinese;
    int Math;
    int English;

    while (cin >> number >> Chinese >> Math >> English) {
        student.setStudent(number, Chinese, Math, English);

        cout << "该生的平均成绩：" << StudentFunc1::avery(student) << endl;

        if (StudentFunc1::pass(student)) {
            cout << "pass" << endl;
        } else {
            cout << "not pass" << endl;
        }
        break;
    }
}

void classFunc2() {
    string number;
    int Chinese;
    int Math;
    int English;

    while (cin >> number >> Chinese >> Math >> English) {
        StudentFunc2 student(number, Chinese, Math, English);

        cout << "该生的平均成绩：" << student.avery() << endl;

        if (student.pass()) {
            cout << "pass" << endl;
        } else {
            cout << "not pass" << endl;
        }
        break;
    }
}

#endif //CPP_SIMPLEUSE_H
