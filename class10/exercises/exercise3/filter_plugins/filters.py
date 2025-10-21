import re

def arp_dict(output):
    arp_dict = {}
    for line in output.strip().splitlines():
        if re.search(r".*Address.*Interface$", line, flags=re.M):
            continue
        ip_addr = line.split()[1]
        mac = line.split()[3]
        arp_dict[ip_addr] = mac

    return arp_dict

class FilterModule(object):
    def filters(self):
        return {"arp_dict": arp_dict}
