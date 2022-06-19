from settings import known_device_hosts
from roku import Roku
#ROKU_IP_ADDRESS = "192.168.86.75"
#find roku on mac: ipconfig, arp -a, find name
#print(ROKU_IP_ADDRESS)
DEFAULT_ROKU_PORT: int = 8060
# port is int class, host is str class
def scan_devices() -> list[str]:
    options = Roku.discover(timeout=10)
    available = []
    for option in options:
        for known_device in known_device_hosts:
            if option.host == known_device[0]:
                print(f'{known_device[1]} was found.')
                available.append(option.host)
    return available

def unknown_devices():
    options = Roku.discover(timeout=10)
    print(options)


def selection(available, known_device_hosts):
    for items in available:
        for i in range(len(known_device_hosts)):
            if available == known_device_hosts[i]:
                device_IP = available
                device_name = known_device_hosts[i][1]
                print(f'Enter {i} to select {device_name}. IP: {device_IP}')
                #print(f'found: {available} {known_device_hosts[i][1]}')
    print(f'all: {available}')
       # print(f"Enter {i} to connect to {known_device_hosts[i][1]}")
    user_selection = input("Selection: ")
    user_selection = int(user_selection)
    #if 0 <= user_selection < len(available):
    global ROKU_IP_ADDRESS
    ROKU_IP_ADDRESS = available[user_selection - 1]
    print(ROKU_IP_ADDRESS)
    return ROKU_IP_ADDRESS

            
        #print(type(option.host))
        #print(type(option.port))
def main() -> str:
    available = scan_devices()
    #ROKU_IP_ADDRESS = "192.168.86.75"
    ROKU_IP_ADDRESS=selection(available, known_device_hosts)
    return ROKU_IP_ADDRESS
    #return f'{ROKU_IP_ADDRESS}:{DEFAULT_ROKU_PORT}'
    



#unknown_devices()