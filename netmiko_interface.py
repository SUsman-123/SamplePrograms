'''import ifaddr

adapters = ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter"+adapter.nice_name)
    for ip in adapter.ips:
        print("%s/%s"%(ip.ip, ip.network_prefix))'''
'''
import ifaddr
adapters = ifaddr.get_adapters(include_unconfigured=True)
for adapter in adapters:
    print("IPs of network adapter"+adapter.nice_name)
    if adapter.ips:
        for ip in adapter.ips:
           print("%s/%s"%(ip.ip, ip.network_prefix))
        else:
            print("No IPs Configured")'''



























