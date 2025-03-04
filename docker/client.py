import asyncio
import websockets

async def client():
    uri = "ws://server-service:8080"
    async with websockets.connect(uri) as websocket:
        count = 1
        while True:
            message = f"Client Message {count}"
            await websocket.send(message)
            print(f"Sent: {message}")
            response = await websocket.recv()
            print(f"Received: {response}")
            await asyncio.sleep(2)
            count += 1

asyncio.run(client())
