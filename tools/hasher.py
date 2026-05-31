import hashlib, os

def run(args):
    if not args:
        print("  [!] Usage: mia.py hash <file>")
        return
    path = args[0]
    if not os.path.isfile(path):
        print(f"  [!] File not found: {path}")
        return
    sha256 = hashlib.sha256()
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            sha256.update(chunk)
            md5.update(chunk)
    size = os.path.getsize(path)
    print(f"\n\033[1;36m[ HASH: {os.path.basename(path)} ]\033[0m")
    print(f"  Size   : {size:,} bytes")
    print(f"  MD5    : {md5.hexdigest()}")
    print(f"  SHA256 : {sha256.hexdigest()}")
    print()
