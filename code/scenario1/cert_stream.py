import websocket
import itertools
import sys

try:
    import thread
except ImportError:
    import _thread as thread
import time

sys.stdout = open('cert_stream.json', 'w')

def on_message(ws, message):
    print(message)
    sys.stdout.write(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    pass
    
def on_open(ws):
    def run(*args):
        for i in itertools.repeat(1):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:4000/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
