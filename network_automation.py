import time
import random
from netmiko import ConnectHandler

# --- Catalyst 8000v IP address---
ROUTER_IP = "10.10.20.48"

router = {
    'device_type': 'cisco_ios',
    'host': ROUTER_IP,
    'username': os.environ.get('ROUTER_USER', 'developer'),
    'password': os.environ.get('ROUTER_PASS', 'C1sco12345'),
    'secret': os.environ.get('ROUTER_SECRET', 'C1sco12345')
}

failover_active = False

def read_temperature():
    return round(random.uniform(20.0, 90.0), 2)

def check_and_reroute():
    global failover_active
    temp = read_temperature()
    print(f"[IoT Sensor] Current Temperature: {temp}°C")
    
    try:
        net_connect = ConnectHandler(**router)
        net_connect.enable()

        if temp > 75 and not failover_active:
            print("[ALERT] Overheating! Activating network failover...")
            net_connect.send_config_set([
                'interface Loopback1',
                'description *** FAILOVER ACTIVE - TEMP HIGH ***'
            ])
            failover_active = True
            print("[Network] Loopback1 updated to FAILOVER state.")

        elif temp <= 70 and failover_active:
            print("[INFO] Temperature normalized. Restoring network...")
            net_connect.send_config_set([
                'interface Loopback1',
                'description *** FAILOVER INACTIVE - TEMP NORMAL ***'
            ])
            failover_active = False
            print("[Network] Loopback1 restored to NORMAL state.")
        
        net_connect.disconnect()
    except Exception as e:
        print(f"[ERROR] Could not connect to router: {e}")

if __name__ == "__main__":
    print("=== IoT Network Monitor Started ===")
    print(f"Target Router: {ROUTER_IP}")
    while True:
        check_and_reroute()
        time.sleep(10)
