import time
from datetime import datetime as dt

hosts_temp = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.youtube.com", "youtube.com", "www.hotmail.com", "hotmail.com"]

try:
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
            print("Working...")
            with open(hosts_path, 'r+') as f:
                content = f.read()
                for website in website_list:
                    if website in content:
                        pass
                    else:
                        f.write(redirect + " " + website + "\n")
        else:
            with open(hosts_path, 'r+') as f:
                content = f.readlines()
                f.seek(0)
                for line in content:
                    if not any(website in line for website in website_list):
                        f.write(line)
                f.truncate()
            print("Resting...")
        time.sleep(5)

except KeyboardInterrupt:
    print("Exited the program.")

finally:
    with open(hosts_path, 'r+') as f:
        content = f.readlines()
        f.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                f.write(line)
        f.truncate()