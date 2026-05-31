import os

def run(args):
    path = args[0] if args else '.'
    if not os.path.isdir(path):
        print(f"  [!] Not a directory: {path}")
        return
    print(f"\n\033[1;36m[ SCAN: {path} ]\033[0m")
    total_files = 0
    total_size = 0
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        level = root.replace(path, '').count(os.sep)
        indent = '  ' * level
        print(f"{indent}\033[1;33m{os.path.basename(root)}/\033[0m")
        subindent = '  ' * (level + 1)
        for f in files:
            fpath = os.path.join(root, f)
            try:
                size = os.path.getsize(fpath)
                total_size += size
                total_files += 1
                print(f"{subindent}{f}  ({size:,} bytes)")
            except OSError:
                print(f"{subindent}{f}  (unreadable)")
    print(f"\n  Total: {total_files} files, {total_size:,} bytes\n")
