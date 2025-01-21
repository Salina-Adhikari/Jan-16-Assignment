import os
import shutil
if not os.path.isdir("test_directory"):
  os.mkdir("test_directory")
# Change the current working directory to the new directory
os.chdir("test_directory")
print("Current working directory:",os.getcwd())

# Create a text file in the directory
with open("example.txt","w")as file:
    file.write("This is a test file.")
# List files i  the current directory
print("Files in directory:",os.listdir())

 # Copy the file
shutil.copy("example.txt","copy_example.txt")
## Move the copied file to a new location (remaining it in the process)
shutil.move("copy_example.txt","../moved_example.txt")
# # Go back to  the parent directory
os.chdir("..")
shutil.rmtree("test_directory")
os.remove("moved_example.txt")
print("Cleanup complete!")


import subprocess
import os
# Run a simple command and capture its output
result=subprocess.run(["echo","Hello ,World"],capture_output=True,text=True)
print("Command Output:",result.stdout)
# List files in the current directory using 'ls' or 'dir' (platform-specific)
command=["ls"] if os.name!="nt" else ["dir"]
result=subprocess.run(command,capture_output=True,text=True,shell=True)
print("Files in current directory:")
print(result.stdout)
# check for errors
result=subprocess.run(["fake command"],capture_output=True,text=True)
if result.returncode!=0:
   print("Error :",result.stderr)
import os
import shutil

#Define the directory to organiize
directory = "./example_directory"

#Create the directory and some text files
os.makedirs(directory, exist_ok=True)
with open(os.path.join(directory, "file1.txt"), "w") as f:
    f.write("Text file content")
with open(os.path.join(directory, "file2.txt"), "w") as f:
    f.write("Image file content")
with open(os.path.join(directory, "file3.txt"), "w") as f:
    f.write("Audio file content")

#Function to organize files by type
def organize_files_by_type(directory):
    #Get a list of all files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        #Skip directories
        if os.path.isdir(file_path):
            continue
        #Get the file extension
        file_extension = file_name.split(".")[-1]
        #Create a folder for the file type f it doesnot exist
        type_folder = os.path.join(directory, file_extension)
        os.makedirs(type_folder, exist_ok=True)
        #Move the file to the appropriate folder
        shutil.move(file_path, os.path.join(type_folder, file_name))
        print(f"Moved {file_name} to {type_folder}/")

#Call the functioin
organize_files_by_type(directory)

#Display organized structure

for root, dirs, files in os.walk(directory):
    print(f"\nIn {root}:")
    for dir_name in dirs:
        print(f"Directory: {dir_name}")
    for file_name in files:
        print(f"Directory: {file_name}")

# #Clean up
# #shutil.rmtree(directory)
import os
import shutil
from datetime import datetime

# Ensure the folder exists
if not os.path.isdir("my_folder"):
    os.mkdir("my_folder")

zip_file = shutil.make_archive("my_archive", "zip", "my_folder")
tar_file = shutil.make_archive("my_archive", "tar", "my_folder")
gztar_file = shutil.make_archive("my_archive", "gztar", root_dir="my_folder")


current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


old_file_name = zip_file 
new_file_name = f"{current_time}.zip"

try:
    os.rename(old_file_name, new_file_name)
    print(f"Archive renamed to: {new_file_name}")
except FileNotFoundError:
    print(f"The file '{old_file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

import datetime
import os
import shutil

def create_backup(source_directory):
    if not os.path.exists(source_directory):
        print(f"Error: The directory '{source_directory}' does not exist. ")
        return
    #Generate a timestamped backup name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    #Create a zip archive of the source directory
    shutil.make_archive(backup_name, 'zip', source_directory)
    print(f"Backup Created: {backup_name}.zip")

#Example usage
create_backup("./example_directory")

import subprocess
import os
def list_running_processes(output_file):
    try:
        # execute the system comaand to list processes 
        command-['tasklist']if os.name=='nt' else ['ps','aux']
        result=subprocess.run(command,capture_output=True,text=True)

        # Save the output to a file
        with open(output_file,'w')as file:
            file.write(result.stdout)
        print(f"process list saved to '{output_file}'")
    except Exception as e:
        print(f"error:{e}")
# example uasge
list_running_processes




# importing required modules 
import os
import shutil
from datetime import datetime, timedelta

def file_cleanup_bot(directory, days_old):
    # Create "Archive" folder if it doesn't exist
    archive_folder = os.path.join(directory, "Archive")
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    # Get the current time
    current_time = datetime.now()
    
    # Scan files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip the Archive folder itself
        if filename == "Archive":
            continue

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file's last modified time
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            
            # Calculate the age of the file
            file_age = current_time - file_mtime
            
            # Move files older than specified days to "Archive"
            if file_age > timedelta(days=days_old):
                shutil.move(file_path, archive_folder)
                print(f"Moved: {file_path} to {archive_folder}")

    # Ask user to delete the "Archive" folder
    user_input = input("Do you want to delete the 'Archive' folder? (yes/no): ").strip().lower()
    if user_input == "yes":
        shutil.rmtree(archive_folder)
        print("Archive folder deleted.")
    else:
        print("Archive folder kept.")


directory_path = input("Enter the directory path: ").strip()
days = int(input("Enter the number of days: "))
file_cleanup_bot(directory_path, days)

import os
import platform
import shutil
import subprocess

def generate_system_diagnostics_report():
    report = []

    # Current working directory
    cwd = os.getcwd()
    report.append(f"Current Working Directory: {cwd}")

    # Disk usage of the current directory
    total, used, free = shutil.disk_usage(cwd)
    report.append(f"Disk Usage: Total: {total // (1024**3)} GB, Used: {used // (1024**3)} GB, Free: {free // (1024**3)} GB")

    # System information
    os_name = platform.system()
    os_version = platform.version()
    processor = platform.processor()
    memory_info = subprocess.run(['free', '-h'], text=True, capture_output=True).stdout
    report.append(f"Operating System: {os_name} {os_version}")
    report.append(f"Processor: {processor}")
    report.append("Memory Info:\n" + memory_info)

    # Save report to a text file
    report_path = os.path.join(cwd, "system_diagnostics_report.txt")
    with open(report_path, "w") as file:
        file.write("\n".join(report))
    
    print(f"System Diagnostics Report saved to: {report_path}")

# Example usage
generate_system_diagnostics_report()
