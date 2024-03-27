import requests
import time

def ping_every_5_mins():
    while True:
        res = requests.get("https://chatgpt.withsix.co")
        time.sleep(120)

if __name__ == "__main__":
    ping_every_5_mins()