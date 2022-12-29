'''
import psutil
result01 = psutil.cpu_times()
result02 = psutil.cpu_stats()

result05 = psutil.net_io_counters(pernic=True)# nowrap=True)
print(result05)
print(result01)
print(result02)'''

import  psutil

nettwork_status = psutil.net_io_counters(pernic=False)
bytes_sent = getattr(nettwork_status, 'bytes_sent')
bytes_recv = getattr(nettwork_status, 'bytes_recv')

print(bytes_sent)
print(bytes_recv)

print(" Bytes Sent-{0} | Bytes Received ")











