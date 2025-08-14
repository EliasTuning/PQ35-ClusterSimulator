class CanSender:
    def __init__(self):
        pass

    def send(self, message_func):
        message = message_func()
        print(message)
        pass
