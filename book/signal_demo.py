from django.dispatch import Signal, receiver

ping_signal = Signal(["context"])

class SignalDemo:
    def ping(self):
        print("PING")
        ping_signal.send(sender=self.__class__, PING=True, val=27)  # kwargs from here

@receiver(ping_signal)
def pong(**kwargs):
    print(kwargs)
    if kwargs.get("PING"):  # if kwargs has ping 
        print("PONG")

demo = SignalDemo()
demo.ping()

