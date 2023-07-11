import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print("on_modified")

    def on_created(self, event):
        if not event.is_directory:
            print("on_created")

    def on_deleted(self, event):
        print("on_deleted")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, 'D:\\新建文件夹\\source1', recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
