# auto_runner.py

import time
import os
import subprocess

def monitor_file(filepath):
    """Monitor a file for changes and run it when modified, with full interactivity."""
    if not os.path.exists(filepath):
        print(f"File {filepath} does not exist!")
        return

    print(f"Monitoring {filepath} for changes... (Ctrl+C to stop)")
    print("💡 You can now input text when the script runs.")

    last_mod_time = os.path.getmtime(filepath)

    while True:
        try:
            current_mod_time = os.path.getmtime(filepath)
            if current_mod_time != last_mod_time:
                print(f"\n🔁 Detected change in {filepath} — reloading...")
                last_mod_time = current_mod_time

                print(f"🚀 Running {filepath}... (Type your input below)")
                print("-" * 50)

                # Run with inherited stdin/stdout/stderr (interactive!)
                result = subprocess.run(["python", filepath], stdin=None, stdout=None, stderr=None)

                print("-" * 50)
                if result.returncode == 0:
                    print("✅ Script finished successfully.")
                else:
                    print(f"❌ Script exited with code: {result.returncode}")

            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n🛑 Stopped monitoring.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    monitor_file("guess_the_number.py")
