import time
import os
import subprocess

def monitor_file(filepath):
    """Monitor a file for changes and run it when modified."""
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist!")
        return

    # Get the initial modification time
    last_mod_time = os.path.getmtime(filepath)
    print(f"Monitoring {filepath} for changes... (Ctrl+C to stop)")

    while True:
        try:
            # Check if the file has been modified
            current_mod_time = os.path.getmtime(filepath)
            if current_mod_time != last_mod_time:
                print(f"\n🔁 Detected change in {filepath} — reloading...")
                last_mod_time = current_mod_time

                # Run the script
                print(f"🚀 Running {filepath}...")
                result = subprocess.run(["python", filepath], capture_output=True, text=True)

                # Print output
                if result.stdout:
                    print(f"📤 Output:\n{result.stdout}")
                if result.stderr:
                    print(f"❌ Error:\n{result.stderr}")
                print(f"{'-'*50}")

            time.sleep(3)  # Check every 3s

        except KeyboardInterrupt:
            print("\n🛑 Stopped monitoring.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    monitor_file("basic.py")