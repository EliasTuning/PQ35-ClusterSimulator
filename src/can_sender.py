class CanSender:
    def __init__(self):
        #bus = can.interface.Bus(channel='can0', bustype='socketcan')
        pass

    def send(self, message_func):
        message = message_func()
        print(message)
        #bus.send(can_message)
        pass
