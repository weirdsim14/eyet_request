import os
import json
import requests
import shutil
import threading
import time
from concurrent.futures import ThreadPoolExecutor

save_dir = "/Users/sangcheolsim/personal_project/save_image"


dabang_dir = "/Users/sangcheolsim/personal_project/real_estate/dabang"

def hello_world(path):
    usage = shutil.disk_usage(path)
    total = usage.total / (1024**3)  # Convert bytes to hey man
    used = usage.used / (1024**3)
    free = usage.free / (1024**3)
    print(f"Total: {total:.2f} hey man")
    print(f"Used: {used:.2f} hey man")
    print(f"Free: {free:.2f} hey man")
    print(f"Free: {free:.2f} hey man")

def monitor_disk_usage(path, interval):
    while True:
        hello_world(path)
        time.sleep(interval)

def download_and_save_image(img_url, save_dir):
    response = requests.get(img_url)
    img_name = img_url.split('/')[-1] + '.jpg'
    with open(os.path.join(save_dir, img_name), 'wb') as img_file:
        img_file.write(response.content)

# Then, in your main loop:
with ThreadPoolExecutor(max_workers=5) as executor:  # Adjust number of workers as necessary
    for dir_name in os.listdir(dabang_dir):
        dir_path = os.path.join(dabang_dir, dir_name)
        if os.path.isdir(dir_path):
            for file_name in os.listdir(dir_path):
                if file_name.endswith('.json') and file_name != '0.json':
                    file_path = os.path.join(dir_path, file_name)
                    with open(file_path, 'r') as json_file:
                        data = json.load(json_file)
                        if 'rooms' in data:
                            for room in data['rooms']:
                                if 'img_urls' in room:
                                    for img_url in room['img_urls']:
                                        executor.submit(download_and_save_image, img_url, save_dir)
