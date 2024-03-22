from datetime import timedelta
from subprocess import check_output
from logos import imgs
from platform import release
from colorama import Fore, Back

class Linux:
    @staticmethod
    def os_name():
        with open("/etc/os-release", "r") as f:
            for line in f:
                if line.lower().startswith("id="):
                    Linux._os_name = line.split("=")[-1].strip()
                    break
        return Linux._os_name

    @staticmethod
    def get_ip():
        try:
            ip = check_output(['hostname', '-i']).decode().strip().split(" ")[0]
            Linux._ip_address = ip
        except Exception as e:
            print("Error:", e)
            Linux._ip_address = None
        return Linux._ip_address

    @staticmethod
    def uptime():
        # Get the system uptime in seconds
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])

        # Convert uptime to a timedelta object
        uptime_timedelta = timedelta(seconds=uptime_seconds)

        # Extract days, hours, and minutes from the timedelta
        days, seconds = divmod(uptime_timedelta.total_seconds(), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, _ = divmod(seconds, 60)

        # Format the uptime string
        uptime_string = f"{int(days)}d {int(hours)}h {int(minutes)}m"

        return uptime_string

    @staticmethod
    def hostname():
        return open("/etc/hostname", "r").read()

def main():
    os_name = Linux.os_name().lower()
    logo = imgs[os_name[0]][os_name]
    image = logo["logo"]
    text_color = logo["text"]
    ip_address = Linux.get_ip()
    
    info = [
        f"{text_color}os{Fore.RESET} │ {os_name}",
        f"{text_color}kv{Fore.RESET} │ {release()}",
        f"{text_color}up{Fore.RESET} │ {Linux.uptime()}",
        f"{text_color}ip{Fore.RESET} │ {ip_address}" if ip_address is not None else "",
        f"{text_color}hn{Fore.RESET} │ {Linux.hostname()}"
    ]
    
    # Print each line of logo with aligned system information
    for i in range(len(info) if len(info) > len(image) else len(image)):
        logo_line = image[i] if i < len(image) else ""
        info_line = info[i] if i < len(info) else ""
        print(f"{logo_line} {info_line}")

if __name__ == "__main__":
    main()