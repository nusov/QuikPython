# QuikPython
Python Bindings to QuikConnector

# Usage
```
from quik.socket import QuikSocket
from quik.connector import QuikConnector

quik_socket = QuikSocket("tcp://127.0.0.1:8001")
quik = QuikConnector(quik_socket)
print(len(quik.tables.all_trades))
```
