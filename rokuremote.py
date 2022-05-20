from roku import Roku
from time import sleep
import requests

#find roku on mac: ipconfig, arp -a, find name
ROKU_IP_ADDRESS: str = "192.168.106.244"

roku = Roku(ROKU_IP_ADDRESS)


start: bool = False
hulu_login: bool = False

def set_hulu_auth():
    global hulu_login
    hulu_login = True

def set_hulu_auth_off():
    global hulu_login
    hulu_login = False

def set_start():
    global start
    start = True

def set_start_off():
    global start
    start = False

def watch_hulu():
    hulu = roku['Hulu']
    hulu.launch()
    sleep(10)

def watch_netflix():
    netflix = roku['Netflix']
    netflix.launch()
    sleep(10)

def play_xbox():
    xbox = roku['Xbox One']
    xbox.launch()
    sleep(10)

def watch_tv():
    live = roku['Live TV']
    live.launch()
    sleep(10)

def watch_disney_plus():
    disney = roku['Disney Plus']
    disney.launch()
    sleep(10)

def watch_espn():
    espn = roku['ESPN']
    espn.launch()
    sleep(10)

def watch_hbo_max():
    hbo = roku['HBO Max']
    hbo.launch()
    sleep(10)

def watch_youtube():
    youtube = roku['Youtube']
    youtube.launch()
    sleep(10)

def watch_peacock():
    peacock = roku['Peacock TV']
    peacock.launch()
    sleep(10)

def display_apps():
    print(roku.apps)

def home():
    roku.home()
    sleep(5)

def select():
    roku.select()
    sleep(2.5)

def get_active():
    print(roku.active_app)

def search_roku():
    roku.search()
    sleep(4)

def right():
    roku.right()
    sleep(.5)

def left():
    roku.left()
    sleep(.5)

def up():
    roku.up()
    sleep(.5)

def down():
    roku.down()
    sleep(.5)

def remote_right(x=1):
    for i in range(x):
        roku.right()
        if x > 1:
            sleep(1)
        else:
            sleep(2)

def remote_left(x=1):
    for i in range(x):
        roku.left()
        if x > 1:
            sleep(1)
        else:
            sleep(2)

def remote_up(y=1):
    for i in range(y):
        roku.up()
        if y > 2:
            sleep(.5)
        elif y > 1:
            sleep(1)
        else:
            sleep(2)

def remote_down(y=1):
    for i in range(y):
        roku.down()
        if y > 2:
            sleep(.5)
        elif y > 1:
            sleep(1)
        else:
            sleep(2)

def hbo_max_search():
    watch_hbo_max()
    select()
    remote_left(4)
    remote_up(1)
    select()

def hulu_search():
    watch_hulu()
    if hulu_login:
        select()
    remote_up(1)
    remote_left(1)
    select()

def southpark():
    hbo_max_search()
    for char in "southpark":
        letter(char)
    if start:
        select()

def modernfamily(remote=False):
    hulu_search()
    for char in "modern family":
        letter(char)
    # remote_down(2)
    # select()
    # remote_right(2)
    # select()
    # remote_up(2)
    # remote_right(1)
    # select()
    remote_right(6)
    select()
    # select()
    if start:
        select()
    if remote:
        select()

def workaholics():
    hulu_search()
    for char in "worka":
        letter(char)
    remote_right(6)
    select()
    if start:
        select()


def game_of_thrones():
    hbo_max_search()

def letter(x):
    requests.post(f"http://{ROKU_IP_ADDRESS}:8060/keypress/Lit_{x}")

def volume_down():
    requests.post(f'http://{ROKU_IP_ADDRESS}:8060/keypress/volumeDown')

def volume_up():
    requests.post(f'http://{ROKU_IP_ADDRESS}:8060/keypress/volumeUp')

def power():
    requests.post(f'http://{ROKU_IP_ADDRESS}:8060/keypress/PowerOff')

def music(remote=False):
    spotify = roku['Spotify Music']
    spotify.launch()
    sleep(10)
    select()
    if remote:
        select()
    select()
    if start:
        select()

