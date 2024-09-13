from django.shortcuts import render
from django.http import HttpResponse
from .signals import my_signal
import threading

def my_view(request):
    # Print the current thread (should be MainThread)
    print(f"View running in thread: {threading.current_thread().name}")
    
    # Dispatch the signal
    my_signal.send(sender=None)

    return HttpResponse("Signal dispatched!")
