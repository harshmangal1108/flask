# Flask is micro web framework of Python
## Installation flask
```bash
pip3 install flask
```
### Using flask
```python3
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello():
   return "Flask App"

app.run=main
```
