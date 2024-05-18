import csv
import time

# 当前时间
now_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

with open(f"tmp_{now_time}.csv", "w") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["行号", "Column1", "Cloumn2"])

