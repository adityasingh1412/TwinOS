import platform
import socket
import psutil


def get_system_info():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return {
        "hostname": socket.gethostname(),
        "operating_system": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],

        "cpu": {
            "physical_cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
            "usage_percent": psutil.cpu_percent(interval=1)
        },

        "memory": {
            "total_gb": round(memory.total / (1024**3), 2),
            "used_gb": round(memory.used / (1024**3), 2),
            "available_gb": round(memory.available / (1024**3), 2),
            "percent": memory.percent
        },

        "disk": {
            "total_gb": round(disk.total / (1024**3), 2),
            "used_gb": round(disk.used / (1024**3), 2),
            "free_gb": round(disk.free / (1024**3), 2),
            "percent": disk.percent
        }
    }