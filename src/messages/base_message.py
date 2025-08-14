import time
import can
import cantools


class BaseMessage:
    """Base class for all CAN message generators."""
    
    def __init__(self, dbc_path: str = 'vw_pq.dbc'):
        self._db = cantools.database.load_file(dbc_path)
    
    def get_message(self, name: str):
        """Get a message definition from the DBC file."""
        return self._db.get_message_by_name(name)
    
    def generate_can_message(self, arbitration_id, data):
        """Generate a CAN message with the given arbitration ID and data."""
        can_message = can.Message(
            arbitration_id=arbitration_id,
            is_extended_id=False,
            data=data, 
            timestamp=time.time()
        )
        return can_message
    
    def generate(self):
        """Generate the specific message. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement generate() method")
