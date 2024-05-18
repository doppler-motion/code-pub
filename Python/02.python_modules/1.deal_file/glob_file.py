import glob

file_list = glob.glob("/etc/sysconfig/network-scripts/ifcfg-*")

print(file_list)
