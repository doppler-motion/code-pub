import netaddr

from netaddr import EUI, mac_unix, mac_cisco, mac_bare

ip_list = []

ip = netaddr.IPNetwork("172.16.135.0/22")

ip_list.append(ip)

print(netaddr.cidr_merge(ip_list))

print(ip)

for item in ip.iter_hosts():
    print(item)

print(type(ip.iter_hosts()))

if "172.16.135.241" in ip.iter_hosts():
    print("This ip is in this segment")

mac = "8CA6.DFEA.868F"

mac = EUI(mac)

# print(mac.info)
# for i in mac.info:
#     print(i)
