import os
import datetime
import subprocess
import socket
import logos
import platform

import colorama
from colorama import Fore, Back

# Initialize colorama
colorama.init(autoreset=True)

class Linux:
    _os_name = None
    _ip_address = None

    @staticmethod
    def os_name():
        if Linux._os_name is None:
            with open("/etc/os-release", "r") as f:
                for line in f:
                    if line.lower().startswith("id="):
                        Linux._os_name = line.split("=")[-1].strip()
                        break
        return Linux._os_name

    @staticmethod
    def get_ip():
        if Linux._ip_address is None:
            try:
                ip = subprocess.check_output(['hostname', '-i']).decode().strip().split(" ")[0]
                Linux._ip_address = ip
            except Exception as e:
                print("Error:", e)
                Linux._ip_address = None
        return Linux._ip_address

def print_image(image):
    # Get the text and background colors from the image dictionary
    fore_color = image.get("fore_color", "white")
    bg_color = image.get("bg_color", "black")
    
    # Set the foreground and background colors
    fg_color_code = getattr(Fore, fore_color.upper(), Fore.WHITE)
    bg_color_code = getattr(Back, bg_color.upper(), Back.BLACK)
    
    # Print each line of the image with the specified colors
    logo = ""
    for line in image.get("lines", []):
        logo += f"{bg_color_code}{fg_color_code}{line}{Fore.RESET}{Back.RESET}\n"
    return logo

def uptime():
    # Get the system uptime in seconds
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    # Convert uptime to a timedelta object
    uptime_timedelta = datetime.timedelta(seconds=uptime_seconds)

    # Extract days, hours, and minutes from the timedelta
    days, seconds = divmod(uptime_timedelta.total_seconds(), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, _ = divmod(seconds, 60)

    # Format the uptime string
    uptime_string = f"{int(days)}d {int(hours)}h {int(minutes)}m"

    return uptime_string

def main():
    image = logos.imgs.get(Linux.os_name())

    text_color = image.get("text_color", "white")
    text_color_code = getattr(Fore, text_color.upper(), Fore.WHITE)

    ip_address = Linux.get_ip()
    info = [
        f"{text_color_code}os{Fore.RESET} : {Linux.os_name()}",
        f"{text_color_code}kv{Fore.RESET} : {platform.release()}",
        f"{text_color_code}up{Fore.RESET} : {uptime()}",
        f"{text_color_code}ip{Fore.RESET} : {ip_address}" if ip_address is not None else "",
        f"{text_color_code}hn{Fore.RESET} : {socket.gethostname()}"
    ]

    # Print the logo with colored text and background
    logo_lines = print_image(image).split('\n')
    
    # Determine the number of lines to print
    num_lines = max(len(logo_lines), len(info))
    
    # Print each line of logo with aligned system information
    for i in range(num_lines):
        logo_line = logo_lines[i] if i < len(logo_lines) else ""
        info_line = info[i] if i < len(info) else ""
        print(f"{logo_line} {info_line}")

if __name__ == "__main__":
    main()
