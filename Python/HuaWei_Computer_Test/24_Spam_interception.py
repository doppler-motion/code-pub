# 垃圾信息拦截

import sys

n = int(input())

connections = []
for i in range(n):
    id_from, id_to = map(int, input().split())
    connections.append([id_from, id_to])

target_id = int(input())

send_mail_persons = set()
get_mail_persons = set()
send_mail_count = dict()
get_mail_count = dict()
sent_mails_num = 0
received_mails_num = 0
for conn in connections:
    if conn[0] == target_id:
        send_mail_persons.add(conn[1])
        sent_mails_num += 1
        send_mail_count[conn[1]] = send_mail_count.get(conn[1], 0) + 1
    elif conn[1] == target_id:
        received_mails_num += 1
        get_mail_persons.add(conn[0])
        get_mail_count[conn[0]] = get_mail_count.get(conn[0], 0) + 1

is_spam = False
send_mail_persons.difference_update(get_mail_persons)
num_unique_receivers = len(send_mail_persons)
num_sent_mails_minus_received = sent_mails_num - received_mails_num
if num_unique_receivers > 5:
    is_spam = True
elif num_sent_mails_minus_received > 10:
    is_spam = True
else:
    for receiver_id, sent_count in send_mail_count.items():
        if receiver_id in get_mail_count:
            if sent_count - get_mail_count[receiver_id] > 5:
                is_spam = True
                break

print(str(is_spam) + " " + str(num_unique_receivers) + " " + str(num_sent_mails_minus_received))
