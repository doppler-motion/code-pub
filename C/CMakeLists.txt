cmake_minimum_required(VERSION 3.23)
project(C)

set(CMAKE_C_STANDARD 99)

add_executable(main.c demoLearn/utils_test.h demoLearn/sortFunc.h demoLearn/exchangeNum.h)
add_executable(DataStructure&Algorithm/ch03/LinkList.c)
add_executable(LineList DataStructure&Algorithm/ch03/LineList.c)
add_executable(StaticList DataStructure&Algorithm/ch03/StaticList.c)

add_executable(test tmp/test.c)
add_executable(test1 ch04/test.c)