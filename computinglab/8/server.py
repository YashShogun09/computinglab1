import asyncio, websockets

async def handle(websocket):
    lol = 0
    print("listening for messages...")
    while True:
        m = await websocket.recv()   # receive as string
        msg = int(m)                 # convert to int

        # update lol each time
        lol = lol - 10 + msg

        # condition check
        if lol > 50:
            print("server overload")
        else:
            print("req processed")

        print("lol =", lol)

async def main():
    async with websockets.serve(handle, "localhost", 8765):
        print("listening on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())
