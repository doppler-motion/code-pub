import os


def list_all_file(path, all_files: list):
    files = []
    if os.path.exists(path):
        files = os.listdir(path)
    else:
        print('this path not exist')

    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            list_all_file(os.path.join(path, file), all_files)
        else:
            all_files.append(os.path.join(path, file))

    return all_files


all_file_list = list_all_file(path="/root/1/", all_files=[])

print(all_file_list)
