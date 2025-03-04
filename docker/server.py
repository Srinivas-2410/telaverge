import asyncio
import websockets

async def server_handler(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    # Start WebSocket server on 0.0.0.0 and port 8080
    async with websockets.serve(server_handler, "0.0.0.0", 8080):
        print("WebSocket Server started on ws://0.0.0.0:8080")
        await asyncio.Future()  # Keep running indefinitely

if __name__ == "__main__":
    asyncio.run(main())  # ✅ Ensures the event loop is properly managed

