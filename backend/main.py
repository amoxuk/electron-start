from flask import Flask, render_template

# 首先创建一个变量 app, 用于初始化 flask 启动核心
app = Flask(__name__)


@app.route('/')
def homepage():
    # 将本函数绑定到路由根地址, 这样我们访问主地址时, 就能看到这个页面
    return {'word': 'hello world'}


if __name__ == "__main__":
    # 启动, 启动后访问 http://127.0.0.1:5858 查看
    app.run(host='127.0.0.1', port=5000)
