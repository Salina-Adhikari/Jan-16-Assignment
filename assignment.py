""

import os
import shutil
import subprocess

def generate_system_report(output_file):
    try:
        # Get current working directory
        cwd = os.getcwd()

        # Get disk usage of the current directory
        disk_usage = shutil.disk_usage(cwd)

        # Get system information
        system_info = subprocess.run(['systeminfo'], capture_output=True, text=True).stdout

        # Write the report to a file
        with open(output_file, 'w') as file:
            file.write(f"Current Working Directory: {cwd}\n")
            file.write(f"Disk Usage:\n")
            file.write(f"  Total: {disk_usage.total / (1024 ** 3):.2f} GB\n")
            file.write(f"  Used: {disk_usage.used / (1024 ** 3):.2f} GB\n")
            file.write(f"  Free: {disk_usage.free / (1024 ** 3):.2f} GB\n")
            file.write(f"System Information:\n{system_info}\n")

        print(f"System diagnostics report saved to '{output_file}'")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
generate_system_report("system_report.txt")



