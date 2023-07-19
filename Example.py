from flask import *
from redis import Redis

app = Flask(__name__)
redis = Redis(host='localhost', port=6379, db=0)
# redis.flushall()

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/todoList')
def renderTodoList():
    keys = redis.keys()
    todoListItems = [[hash[b"deadline"].decode(), hash[b"task"].decode()] for hash in [redis.hgetall(key) for key in keys]]
    print(todoListItems)
    todoListHTML = render_template('todoList.html', todoList=todoListItems)
    return todoListHTML

@app.route('/process_data', methods=['POST'])
def process_data():
    keys = redis.keys()
    deadline = request.form['deadline']
    task = request.form['task']
    
    print(len(keys),deadline,task)
    
    if(task and deadline):
    # データの処理などを行う

        redis.hset("id:"+str(len(keys)),"deadline",deadline)
        redis.hset("id:"+str(len(keys)),"task",task)
        
        response = {'success': True,'deadline':deadline,'task':task}
        
        return jsonify(response)
    
    else:
        response = {'success': False}
        return jsonify(response)

if __name__ == '__main__':
    app.run()

# 共同編集者：佐藤優悟

# Redis に接続します
# Redisサーバーのホスト名, ポート番号, データベース番号 を指定します
#r = redis.Redis(host='localhost', port=6379, db=0)


# 'hoge' というキーで 'moge' という値を追加します
#r.set('hoge','moge')


# 追加した値を取得して表示します
#hoge = r.get('hoge')
##
#print(hoge.decode())

# 追加した値を削除します
#result = r.delete('hoge')
