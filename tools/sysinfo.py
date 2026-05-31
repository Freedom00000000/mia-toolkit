import platform, psutil, datetime

def run(args):
    print("\n\033[1;36m[ SYSTEM INFO ]\033[0m")
    print(f"  OS       : {platform.system()} {platform.release()} ({platform.architecture()[0]})")
    print(f"  Node     : {platform.node()}")
    print(f"  Python   : {platform.python_version()}")
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    print(f"  CPU      : {cpu}% used | {psutil.cpu_count()} cores")
    print(f"  RAM      : {mem.used // (1024**2)} MB used / {mem.total // (1024**2)} MB total ({mem.percent}%)")
    print(f"  Disk     : {disk.used // (1024**3)} GB used / {disk.total // (1024**3)} GB total ({disk.percent}%)")
    print(f"  Time     : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
