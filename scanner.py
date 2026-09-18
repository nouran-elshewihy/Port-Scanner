import socket
from datetime import datetime

print("-" * 40)
print("Simple Port Scanner")
print("-" * 40)

host = input("Target IP: ")
p_start = int(input("Start Port: "))
p_end = int(input("End Port: "))

print(f"\nScanning target: {host}")
print(f"Time started: {datetime.now()}")
print("-" * 40)

try:
    for p in range(p_start, p_end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.8)
        
        res = s.connect_ex((host, p))
        if res == 0:
            print(f"[OPEN] Port {p} is open")
        s.close()

except KeyboardInterrupt:
    print("\n[!] Scan stopped by user.")
except socket.gaierror:
    print("\n[!] Host could not be resolved.")
except socket.error:
    print("\n[!] Could not connect to server.")

print("-" * 40)
print("Scan finished.")
