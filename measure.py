from datetime import datetime, timezone
from pathlib import Path
import psutil


def take_sample():
    cpu = psutil.cpu_percent(interval=0.5)
    ram = psutil.virtual_memory().percent
    home_drive = Path.home().anchor
    disk = psutil.disk_usage(home_drive).percent

    return {
        "measured_at_utc": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": cpu,
        "ram_percent": ram,
        "disk_percent": disk,
    }


if __name__ == "__main__":
    print(take_sample())