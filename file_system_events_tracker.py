import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Note: You may change this 
from_dir = "C:/Users/NAVIPET 13/Downloads"

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops, Someone deleted {event.src_path}")

    def on_modified(self, event):
        print(f"Someone modified {event.src_path}")

    def on_moved(self, event):
        print(f"Did you moved or renamed {event.src_path}")

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")

except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
    