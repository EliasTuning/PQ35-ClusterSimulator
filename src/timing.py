
from typing import Dict, Optional


class MessageTiming:
    """Return hardcoded timing (ms) for known message names."""

    def __init__(self) -> None:
        # Hardcoded from the provided list and CSV lookup
        self._name_to_ms: Dict[str, int] = {
            "Lenkhilfe_1": 20,
            "Motor_5": 20,
            "Motor_1": 10,
            "Bremse_2": 20,
            "Bremse_1": 10,
            "Airbag_1": 20,
            "Getriebe_2": 10,
            "Motor_2": 20,
        }

    def get_timing(self, message_name: str) -> Optional[int]:
        """Return timing in ms for the given message name, or None if unknown."""
        return self._name_to_ms.get(message_name)

    def as_dict(self) -> Dict[str, int]:
        """Return a copy of the name->timing(ms) mapping."""
        return dict(self._name_to_ms)

