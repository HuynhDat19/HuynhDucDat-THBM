import psutil
import platform
import socket
import logging
import time

logging.basicConfig(filename='system_monitor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def log_info(category, message):
    logger.info(f"{category}: {message}")
    printf(f"{category}: {message}")

def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()

    log_info("CPU ", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")

def monitor_system_info():
    os_info = platform.uname()
    hostname = socket.gethostname()

    log_info("System Info", f"Hostname: {hostname}")
    log_info("System Info", f"Operating System: {os_info.system} {os_info.release}")
    log_info("System Info", f"Python Version: {platform.python_version()}")

def monitor_network():
    net_stats = psutil.net_io_counters()
    log_info("Network", f"Bytes Sent: {net_stats.bytes_sent}, Bytes Received: {net_stats.bytes_recv}")

def monitor_software():
  software_list = psutil.process_iter(['pid', 'name', 'username'])
  log_info("Software", "Running Software:")
    for software in software_list:
       software_name = software.info['name']
        software_pid = software.info['pid']
        software_username = software.info['username']
        log_info("Software", f"Name: {software_name}, PID: {software_pid}, Username: {software_user}")

def monitor_system():
    log_info("System", "Starting system monitoring...")
    while True:
        monitor_cpu_memory()
        monitor_system_info()
        monitor_network()
        monitor_software()
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()