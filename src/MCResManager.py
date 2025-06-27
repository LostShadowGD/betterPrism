import os
import time

def toggler():
    with open("config/instance.txt", "r") as file:
        instance = file.read().strip()

    # Define the path to the ress directory
    ress_dir = os.path.join(os.environ.get("APPDATA"), "PrismLauncher", "instances", instance, "minecraft", "resourcepacks")

    # Collect .jar and .jar.DISABLED files
    ress = [f for f in os.listdir(ress_dir) if f.endswith(".zip") or f.endswith(".zip.DISABLED")]

    # Check if there are any res files
    if not ress:
        print("No .zip or .zip.DISABLED files found in the resource folder.")
        exit()

    # Display the ress with numbers
    print("Available resource packs:")
    for i, res in enumerate(ress, start=1):
        if res.endswith(".DISABLED"):
            print(f"[///{i}///] {res}")
        else:
            print(f"[{i}] {res}")

    print("")

    # User selects a file by number
    try:
        choice = int(input("Enter the number of the resource pack you want to toggle: "))
        if not (1 <= choice <= len(ress)):
            raise ValueError
    except ValueError:
        print("Invalid selection. Exiting.")
        exit()

    selected_file = ress[choice - 1]
    print("")
    print(f"You selected: {selected_file}")
    print("")
    confirm = input("Confirm? (Y/N): ").strip().upper()

    if confirm != "Y":
        print("Operation cancelled.")
        exit()

    # Determine full path and new name
    full_path = os.path.join(ress_dir, selected_file)

    # Toggle the .DISABLED suffix
    if selected_file.endswith(".DISABLED"):
        new_name = selected_file[:-9]  # remove '.DISABLED'
    else:
        new_name = selected_file + ".DISABLED"

    new_path = os.path.join(ress_dir, new_name)

    # Rename the file
    os.rename(full_path, new_path)
    print("")
    print(f"File renamed to: {new_name}")

    print("")
    confirm = input("Would you like to make another selection? (Y/N): ").strip().upper()
    if confirm != "Y":
        print("Closing...")
        time.sleep(1)
        exit()

    for i in range(4):
        print("")


logo = """
█   █  ████   █████ █████ █   █ █████ █   █ ████  █████   █   █  ███  █   █  ███   ████ █████ ████  
██ ██ █         █   █      █ █    █   █   █ █   █ █       ██ ██ █   █ ██  █ █   █ █     █     █   █ 
█ █ █ █         █   ████    █     █   █   █ ████  ████    █ █ █ █████ █ █ █ █████ █  ██ ████  ████  
█   █ █         █   █      █ █    █   █   █ █   █ █       █   █ █   █ █  ██ █   █ █   █ █     █   █ 
█   █  ████     █   █████ █   █   █   █████ █   █ █████   █   █ █   █ █   █ █   █  ███  █████ █   █ """

print("Welcome to:")
print("")
print(logo)
print("")
time.sleep(2)
while True:
    toggler()