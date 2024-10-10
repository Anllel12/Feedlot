from abc import ABC, abstractmethod

class ConnectionAbs(ABC):
    @abstractmethod
    def connect(self):
        pass
    def disconnect(self):
        if self.connect().is_connected():
            self.connect().close()
            print("Database connection closed successfully.")
        else:
            print("No active connection to close.")