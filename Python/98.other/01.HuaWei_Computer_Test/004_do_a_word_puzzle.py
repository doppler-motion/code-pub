# 猜字谜

import sys


def encoding(word):
    result = ",".join(sorted(set(word)))
    return result


def do_job2():
    questions = sys.stdin.readline().strip().split(",")
    answers = sys.stdin.readline().strip().split(",")
    dictionary = {encoding(answer): answer for answer in answers}
    answer_list = [dictionary.get(encoding(question), "not found") for question in questions]
    print(",".join(answer_list))


if __name__ == "__main__":
    do_job2()
