# json_parser_app
JSON成形するPythonGUIアプリ


# サンプルJSON
{"user":{"id":12345,"name":"Taro Yamada","is_active":true,"roles":["admin","editor","viewer"]},"products":[{"id":"A001","name":"Keyboard","price":2980,"tags":["electronics","input","peripheral"]},{"id":"B002","name":"Monitor","price":19800,"specs":{"size":"24inch","resolution":"1920x1080","ports":["HDMI","DisplayPort","VGA"]}}],"settings":{"theme":"dark","notifications":{"email":true,"sms":false,"push":["system","reminders"]}},"logs":[{"timestamp":"2025-08-26T10:00:00Z","action":"login"},{"timestamp":"2025-08-26T10:15:32Z","action":"update_profile"},{"timestamp":"2025-08-26T10:45:00Z","action":"logout"}]}


#

有効化
.venv\Scripts\activate.bat



pip install ttkbootstrap


python json_parser_app.py



EXE化
pip install pyinstaller
cd C:\dev\json_parser_app\1.0
pyinstaller --onefile --noconsole json_parser_app.py


