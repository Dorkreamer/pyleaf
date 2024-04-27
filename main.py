from datetime import timedelta
from subprocess import check_output
from logos import imgs
from platform import release
from colorama import Fore, Back
from os import name

if name.lower() == "nt":
    from platform import system
    from platform import version
    from platform import node
    from subprocess import run

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
    
    @staticmethod
    def kernel_version():
        return release()

class NT:
    @staticmethod
    def os_name():
        return f"{system()} {release()}"
    
    @staticmethod
    def kernel_version():
        return version()

    @staticmethod
    def uptime():
        minutes = check_output("powershell -NoLogo -NoProfile [TimeSpan]::FromMilliseconds([Math]::Abs([Environment]::TickCount)).TotalMinutes")
        minutes = str(minutes).lstrip("b'")
        minutes = minutes.rstrip("\\r\\n'")
        minutes = round(float(minutes))
        
        days = minutes // (60 * 24)
        remaining_minutes = minutes % (60 * 24)
        hours = remaining_minutes // 60
        remaining_minutes %= 60
        
        # Format into a pretty string
        uptime_string = f"{days}d {hours}h {remaining_minutes}m"
        
        return uptime_string

    @staticmethod
    def hostname():
        return node()

    @staticmethod
    def get_ip():
        try:
            # Execute the 'ipconfig' command to get network configuration information
            result = run(["ipconfig"], capture_output=True, text=True)
            # Split the output by lines
            output_lines = result.stdout.split('\n')
            # Initialize a variable to store the local IPv4 address
            local_ipv4 = None
            # Iterate through each line of the output
            for line in output_lines:
                # Check if the line contains 'IPv4 Address'
                if 'IPv4 Address' in line:
                    # Extract the IPv4 address from the line
                    local_ipv4 = line.split(':')[-1].strip()
            return local_ipv4
        except Exception as e:
            return None


def main():
    if name.lower() != "nt":
        os_name = Linux.os_name().lower()
        kernel_version = Linux.kernel_version
        uptime = Linux.uptime()
        hostname = Linux.hostname()
        ip_address = Linux.get_ip()
    else:
        os_name = NT.os_name()
        kernel_version = NT.kernel_version()
        uptime = NT.uptime()
        hostname = NT.hostname()
        ip_address = NT.get_ip()

    logo = imgs[os_name[0].lower()][os_name.lower().split(" ")[0]]
    image = logo["logo"]
    text_color = logo["text"]
    
    info = [
        f"{text_color}os{Fore.RESET} │ {os_name}",
        f"{text_color}kv{Fore.RESET} │ {kernel_version}",
        f"{text_color}up{Fore.RESET} │ {uptime}",
        f"{text_color}ip{Fore.RESET} │ {ip_address}" if ip_address is not None else "N/A",
        f"{text_color}hn{Fore.RESET} │ {hostname}"
    ]
    
    # Print each line of logo with aligned system information
    for i in range(len(info) if len(info) > len(image) else len(image)):
        logo_line = image[i] if i < len(image) else ""
        info_line = info[i] if i < len(info) else ""
        print(f"{logo_line} {info_line}")

if __name__ == "__main__":
    main()
