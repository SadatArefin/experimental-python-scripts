# README.md

# WebSocket Chat Server

This project is a simple WebSocket chat server that allows multiple clients to connect and communicate in real-time. It is designed to work seamlessly with Hoppscotch for testing WebSocket connections.

## Project Structure

```
websocket-chat-server
├── src
│   ├── server.py          # Main entry point for the WebSocket server
│   └── utils
│       └── __init__.py    # Utility functions for the server
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Requirements

To run this project, you need to have Python 3.7 or higher installed. You can install the required dependencies using pip:

```
pip install -r requirements.txt
```

## Usage

To start the WebSocket chat server, run the following command:

```
python src/server.py
```

Once the server is running, you can connect to it using a WebSocket client, such as Hoppscotch, by entering the server URL (e.g., `ws://localhost:8000`) and sending messages.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.