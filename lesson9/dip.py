from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotifier(Notifier):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSNotifier(Notifier):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, notifiers):
        self.notifiers = notifiers

    def notify(self, message):
        for notifier in self.notifiers:
            notifier.send(message)

email_notifier = EmailNotifier()
sms_notifier = SMSNotifier()
manager = NotificationManager([email_notifier, sms_notifier])
manager.notify("Hi, user!")
