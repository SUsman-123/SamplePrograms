from netmiko import ConnectHandler
CSR={
    "device_type": "cisco_ios",
   # "ip": "sandbox-iosxe-latest-1.cisco.com",
    "ip": " sandbox-iosxe-recomm-1.cisco.com",
    "port":22,
    "username": "developer",
    "password": "C1sco12345"
}
'''
with open('devices.txt') as routers:
    for IP in routers:
        CSR ={
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-recomm-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**CSR)
        print('Connecting to' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)
net_connect.disconnect()
'''
net_connect = ConnectHandler(**CSR)
output=net_connect.send_command('show ip int brief')
print(output)
output_clock=net_connect.send_command('show clock ')
print(output_clock)
output_router=net_connect.send_command('show ip ro ')
print(output_router)
output_runhost=net_connect.send_command("show run | i host")
print(output_runhost)
output_runconfig=net_connect.send_command("show run")
print(output_runconfig)
#net_connect.disconnect()