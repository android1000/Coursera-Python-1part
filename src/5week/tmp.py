data = b"ok\n\n"
data = b"ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n"
data = b"ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\npalm.cpu 10.6 1501864247\neardrum.cpu 15.4 1501864259\n\n"

data_decoded=data.decode().split("\n")
print(data_decoded)
#data_decoded = data_decoded[1:len(data_decoded)-2]
print(data.decode())
print(data_decoded)
metric_dict={}
for row in data_decoded[1:len(data_decoded) - 2]:
    print(row)
    metric_name, metric_value, timestamp= row.split()
    if metric_name not in metric_dict:
        metric_dict[metric_name]=[]
    metric_dict[metric_name]+=[(int(timestamp),float(metric_value))]

print(metric_dict)

