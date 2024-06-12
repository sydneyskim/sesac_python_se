from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id': 'alice', 'pw':'1234'},
    {'name': 'Bob', 'id': 'bob', 'pw':'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw':'hellocharlie'},
]

@app.route('/', methods=['GET', 'POST']) # 메소드 명시 안할시 기본으로 get임
def home():
    # id = request.args.get('id') # get방식의 url 파라미터를 처리할 때만 가능
    if request.method == "POST":
        id = request.form['id'] # post 방식 중에서 form-data를 처리할 때 payload를 받아오는 방식
        pw = request.form['password']
    
        user = None
        for u in users:
            if u['id'] == id and u['pw'] == pw:
                print('매치되는 사용자 있음')
                user = u
            
        # next() 함수는, next(iterate조건문, 기본값)형태로 구성됨
        # user = next((user for user in users if user['id'] == id and user['pw'] == pw), None)
                
        # 위에 있는 user 목록과 입력한 id/pw를 비교해서 print로 로그인 허용/불허
        if user:
            print(f"로그인한 사용자는 {user['name']} 입니다.")
            message = None
        else:
            print("로그인 가능한 사용자가 없습니다.")
            message = '로그인 실패'
        # print(f"입력한 id: {id} 입력한 pw: {password}")
        
        return render_template('index.html', user=user, error=message)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)