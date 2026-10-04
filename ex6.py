import subprocess
import os

def run(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
    except:
        return "Unable to execute command"

print("Windows Privilege Escalation Checker")
print("------------------------------------")

# 1. Current user
print("\n1. Current User")
print(run("whoami"))

# 2. User privileges
print("\n2. User Privileges")
print(run("whoami /priv"))

# 3. User groups
print("\n3. User Groups")
print(run("whoami /groups"))

# 4. System information
print("\n4. System Information")
print(run("systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\""))

# 5. Running processes
print("\n5. Running Processes")
print(run("tasklist"))

# 6. Windows services
print("\n6. Windows Services")
print(run("sc query"))

# 7. Environment variables
print("\n7. Important Environment Variables")
print("USERNAME =", os.environ.get("USERNAME"))
print("USERPROFILE =", os.environ.get("USERPROFILE"))
print("PATH =", os.environ.get("PATH"))

print("\nScan Completed Successfully.")
