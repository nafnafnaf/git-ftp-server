import tkinterx as tk
from tkinterx import ttk
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Create a dummy authorizer for managing 'anonymous' user access
authorizer = DummyAuthorizer()
authorizer.add_anonymous(r"~/Desktop/ftppython")

# Instantiate FTP handler class
handler = FTPHandler
handler.authorizer = authorizer

# Define a custom welcome message
handler.banner = "Welcome to my FTP server"

# Create a GUI window
window = tk.Tk()
window.title("FTP Server GUI")

# Define the FTP server status as 'OFF'
server_status = False

# Define a function to start the FTP server
def start_server():
    global server_status
    server_status = True
    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

# Define a function to stop the FTP server
def stop_server():
    global server_status
    server_status = False
    server.close_all()

# Add buttons to start and stop the FTP server
start_button = ttk.Button(window, text="Start Server", command=start_server)
start_button.grid(row=0, column=0)

stop_button = ttk.Button(window, text="Stop Server", command=stop_server)
stop_button.grid(row=0, column=1)

# Start the GUI
window.mainloop()
