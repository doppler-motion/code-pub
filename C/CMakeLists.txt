cmake_minimum_required(VERSION 3.23)
project(C)

set(CMAKE_C_STANDARD 99)

add_executable(main main.c tmp/utils_test.h tmp/sortFunc.h tmp/exchangeNum.h)
add_executable(LinkList ch03/LinkList.c)
add_executable(LineList ch03/LineList.c)
add_executable(StaticList ch03/StaticList.c)

add_executable(test tmp/test.c)
add_executable(test1 ch04/test.c)