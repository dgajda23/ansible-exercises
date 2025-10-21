import re

def show_ip_arp(output):
    arp_list = []
    for line in output.strip().splitlines():
        if re.search(r"^Address.*Interface$", line, flags=re.M):
            continue
        mac = line.split()[2]
        arp_list.append(mac)

    return arp_list

class FilterModule(object):
    def filters(self):
        return {"show_ip_arp": show_ip_arp}            
