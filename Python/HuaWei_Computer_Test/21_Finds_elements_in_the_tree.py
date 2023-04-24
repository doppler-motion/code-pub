# 查找树中元素

from typing import List


def parse_one_line(text: str) -> List[int]:
    num_list = text.strip().split()
    return [int(num) for num in num_list]


def handle_tree_nodes(
    nodes: List[List[int]], index: int, n: int, result_list: List[int]
) -> None:
    node = nodes[index]
    if n == 0:
        result_list.append(node[0])
        return

    if len(node) == 1:
        return

    for i in range(1, len(node)):
        handle_tree_nodes(nodes, node[i], n - 1, result_list)


if __name__ == "__main__":
    size = int(input())
    nodes = []
    for i in range(size):
        nodes.append(parse_one_line(input()))
    xy = parse_one_line(input())
    result = ""
    if xy[0] < 0 or xy[1] < 0:
        result = "{}"
    else:
        result_list = []
        handle_tree_nodes(nodes, 0, xy[0], result_list)
        if xy[1] >= len(result_list):
            result = "{}"
        else:
            result = "{" + str(result_list[xy[1]]) + "}"
    print(result)

