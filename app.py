from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/keyboard')
def Keyboard(request):

    json_str = (request.body).decode('utf-8')
    received_json = json.loads(json_str)

    content_name = received_json['content']
    # 누른 버튼 이름
    user_name = received_json['user_key']
    # 유저네임


if __name__ == '__main__':
    app.run()
