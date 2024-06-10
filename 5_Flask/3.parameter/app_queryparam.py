from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'charlie', 'age': 35, 'phone': '345-345-3456'},
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    # query = request.args.get('q')
    # page = request.args.get('page', default=1, type=int)
    # print(query, page)
    # return f"검색중: {query} on 페이지 {page}...", 200

    # 미션1. 위에 있는 users에서 query 구문이 name인 사람을 찾아서 출력하시오..
    result = users
    name_query = request.args.get('name')
    age_query = request.args.get('age')
    phone_query = request.args.get('phone')
    # for u in users:
    #     if u['name'].lower() == name_query.lower():
    #         users = u
    if name_query:
        result = [ u for u in users if name_query.lower() == u['name'].lower()]
    # result = [ u for u in users if name_query.lower() == u['name'].lower()
    #           and str(u['age']) == age_query and u['phone'][-4:] == phone_query]

    # 미션2. 나이도 검색... age
    if age_query:
        try:
            age_query = int(age_query)
            result = [ u for u in result if age_query == u['age']]
        except ValueError:
            return jsonify({'error': 'Age parameter must be an integer'}), 400

    
    # 미션3. 전화번호 끝 4자리로 검색.. phone
    if phone_query:
        result = [ u for u in result if phone_query == u['phone'][-4:]]
        
    return jsonify(result)

# @app.route('/user/<name>')
# def search_user(name):
#     user = None
#     # 유저찾기 함수
#     for u in users :
#         if u['name'].lower() == name.lower():
#             user = u
#             break
    
#     # 결과가 있을 때는, 지금처럼 응답과 200을 보내고
#     if user:
#         return jsonify(user), 200
#     # 결과가 없을 때는, 응답값에 404를보낸다.
#     else:
#         return jsonify({'error':'user not ound'}), 404

if __name__ == "__main__": 
    app.run(debug=True)