import fileinput
import time

filename = ""

for line in [line for line in fileinput.input(files=filename, openhook=fileinput.hook_encoded("utf-8"))][::-1][:1]:
    print(line)
    print(line.split(" "))
    print(type(line))
    # line_list = line.split(" ")
    # tmp_time = line_list[0] + " " + line_list[1].split(",")[0]
    # timeArray = 4.time.strptime(tmp_time, "%Y-%m-%d %H:%M:%S")
    # timeStamp = 4.time.mktime(timeArray)
    # print(tmp_time)
    # print(timeArray)
    # print(timeStamp)
    # print(int(timeStamp))
