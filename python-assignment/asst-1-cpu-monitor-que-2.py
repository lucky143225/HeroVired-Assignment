"""pip3 install psutil --break-system-packages --> Mine office laptop both 2 and 3 versions are isntalled, I can't change anything without admin permission"""

import psutil
import time

# the CPU usage threshold
CPU_USAGE_THRESHOLD = 10.0    #considering 10% to test in my laptop, not sure how to increase cpu % to 80

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent(interval=1)

def check_cpu_usage(threshold):
    """
    Checks if the CPU usage exceeds the given threshold.
    Returns True if the threshold is exceeded, False otherwise.
    """
    cpu_usage = get_cpu_usage()
    return cpu_usage > threshold

def monitor_cpu_usage(threshold):
    """
    Monitors the CPU usage and alerts if the usage exceeds the given threshold.
    Runs indefinitely until interrupted.
    """
    print("Monitoring CPU usage...")
    
    try:
        while True:
            if check_cpu_usage(threshold):
                print(f"Alert! CPU usage exceeds threshold: {get_cpu_usage()}%")
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nMonitoring interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu_usage(CPU_USAGE_THRESHOLD)

