import asyncio
import websockets

# connected_clients is a set that stores all connected clients
connected_clients = set()

async def handle_client(websocket):
    # Add the client to the connected_clients set
    connected_clients.add(websocket)
    try:
        # Loop that waits for messages from the client
        async for message in websocket:
            # Send the message to all clients except the one that sent it
            other_clients = [client.send(message) for client in connected_clients if client != websocket]
            # Wait for all messages to be sent
            if other_clients:
                await asyncio.wait(other_clients)
    finally:
        # Remove the client from the connected_clients set
        connected_clients.remove(websocket)

async def main():
    # Start the server
    async with websockets.serve(handle_client, "localhost", 8000):
        # Run forever
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())