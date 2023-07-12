import os 
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir="C:/Users/mstalin/Downloads"
class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hi,{event.src_path}as been created")
    def on_deleted(self,event):
        print(f"opps someone deleted,{event.src_path}")
    def on_modified(self,event):
        print(f"hi there,{event.src_path}as been modified")
    def on_moved(self,event):
        print(f"someone moved,{event.src_path}to{event.dest_path}")
eventHandler=FileEventHandlepyr()
observer=Observer()
observer.schedule(eventHandler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("stop")
    observer.stop()
