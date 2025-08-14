# This is a sample Python script.

# Press Alt+Umschalt+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from pprint import pprint

from src.can_sender import CanSender
from src.messages.message_factory import MessageFactory
from apscheduler.schedulers.background import BackgroundScheduler

from src.timing import MessageTiming


def main():
    # Create APScheduler background scheduler
    scheduler = BackgroundScheduler()
    sender = CanSender()
    generator = MessageFactory()
    message_timing = MessageTiming()
    for message_name, message_func in generator.getMessages().items():
        timing_ms = message_timing.get_timing(message_name)
        timing_sec = timing_ms / 1000

        scheduler.add_job(
            sender.send,
            trigger='interval',
            seconds=timing_sec,
            args=[message_func],
            id=message_name
        )


    # Start scheduler
    scheduler.start()
    print("Scheduler started. Press Ctrl+C to stop.")

    try:
        while True:
            # Main thread doing other work
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping scheduler...")
        scheduler.shutdown()
        print("Scheduler stopped.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
