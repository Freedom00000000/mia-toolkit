import time, sys

def run(args):
    if not args:
        print("  [!] Usage: mia.py timer <seconds>")
        return
    try:
        secs = int(args[0])
    except ValueError:
        print("  [!] Seconds must be an integer")
        return
    print(f"\n\033[1;36m[ TIMER: {secs}s ]\033[0m")
    for remaining in range(secs, 0, -1):
        mins, s = divmod(remaining, 60)
        bar = '\u2588' * (remaining * 30 // secs) + '\u2591' * (30 - remaining * 30 // secs)
        sys.stdout.write(f"\r  [{bar}] {mins:02d}:{s:02d} ")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r  [" + '\u2588' * 30 + "] DONE!          \n\n")
