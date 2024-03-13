import requests
import time
import os

C2_ADDRESS  = "http://127.0.0.1"
C2_PORT     = 6667

def connect_to_c2():
    os.system(f"MoonlyC2 ")  # Set console title
    url = f"{C2_ADDRESS}:{C2_PORT}"
    while True:
        try:
            response = requests.get(url)
            print(f"Response from C2: {response.text}")
            time.sleep(5)
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == '__main__':
    connect_to_c2()