## PQ35 Cluster Simulator

Simulates CAN messages for VW PQ35 instrument clusters using the provided DBC.

### Quick start (Windows PowerShell)

```bash
# Create and activate a virtual environment
python -m venv venv
./venv/Scripts/Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the simulator
python main.py
```

### Repository contents

- `main.py`: Entry point
- `src/`: Core modules (`can_sender.py`, `message_generator.py`, `timing.py`)
- `vw_pq.dbc`: DBC definitions used for message encoding
- `infos/`: Misc project information

### Notes

- Adjust message behavior in `src/message_generator.py` and timings in `src/timing.py`.

