# Simple WebSocket Fuzzer
from websocket import create_connection

# Connect to WebSocket API and subscribe to trade feed for XBT/USD and XRP/USD
ws = create_connection("ws://soc-player.soccer.htb:9091/")


# Using readlines()
fuzzing_wordlist = open('wordlist.txt', 'r')

Lines = fuzzing_wordlist.readlines()
  
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print('--> {"id":"82930' + line.rstrip() +'"}')
    ws.send('{"id":"82930' + line.rstrip() + '"}')
    print('<-- ' + ws.recv())
    