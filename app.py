from flask import Flask, jsonify
from flask import request
from sql import Sql
from errors import Errors
from authority import Auth

app = Flask(__name__)
sql = Sql
errors = Errors
auth = Auth


@app.route('/user-info', methods=['GET'])
def get_user():
    header = request.headers.get('api-key')
    s = auth.auth(header=header)
    param = int(request.args.get('id'))
    if s['error'] is not None:
        return s, 401
    else:
        if param not in (None, ""):
            dic = sql.user_get(user=param)
            data = {
                'id': dic[0],
                'firstname': dic[1],
                'lastname': dic[2],
                'gender': dic[3],
                'email': dic[4],
                'password': dic[5]
            }
            return jsonify(data)
        else:
            return errors.error_param()


@app.route('/user', methods=['POST', 'PUT'])
def post_user():
    header = request.headers.get('api-key')
    s = auth.auth(header=header)
    if s['error'] is not None:
        return s, 401
    else:
        if request.method == 'POST':
            fname = request.json.get('firstname')
            lname = request.json.get('lastname')
            gender = request.json.get('gender')
            gender = gender.upper()
            email = request.json.get('email')
            email = email.lower()
            password = request.json.get('password')
            if bool(sql.unique_email(email)) is True:
                return errors.unique_email()
            else:
                if email in (None, "") \
                        or password in (None, "") \
                        or fname in (None, "")\
                        or lname in (None, "")\
                        or gender in (None, "")\
                        or gender not in ("F", "M"):
                    return errors.error_param()
                else:
                    id = sql.user_post(fname=fname,
                                      lname=lname,
                                      gender=gender,
                                      email=email,
                                      password=password)
                    dic = sql.user_get(user=id)
                    data = {
                        'id': dic[0],
                        'firstname': dic[1],
                        'lastname': dic[2],
                        'gender': dic[3],
                        'email': dic[4]
                    }
                    return jsonify(data)
        if request.method == 'PUT':
            if s['error'] is not None:
                return s, 401
            else:
                fname = request.json.get('firstname')
                lname = request.json.get('lastname')
                gender = request.json.get('gender')
                gender = gender.upper()
                id = request.json.get('id')
                email = request.json.get('email')
                password = request.json.get('password')
                if email in (None, "") \
                        or password in (None, "") \
                        or fname in (None, "") \
                        or lname in (None, "") \
                        or gender in (None, "") \
                        or gender not in ("F", "M"):
                    return errors.error_param()
                else:
                    sql.update_user(id=id, fname=fname,
                                    lname=lname,
                                    gender=gender)
                dic = sql.user_get(user=id)
                data = {
                    'id': dic[0],
                    'firstname': dic[1],
                    'lastname': dic[2],
                    'gender': dic[3],
                    'email': dic[4],
                    'password': dic[5]
                }
                return jsonify(data)


@app.route('/users', methods=['GET'])
def get_users():
    header = request.headers.get('api-key')
    limit = request.args.get('limit', default=10, type=int)
    order = request.args.get('order', default='id', type=str)
    sort = request.args.get('sort', default='desc', type=str)
    s = auth.auth(header=header)
    if s['error'] is not None:
        return s, 401
    else:
        dic = sql.users(order=order, limit=limit, sort=sort)
        users = []
        for i in dic:
            data = {
                'id': i[0],
                'firstname': i[1],
                'lastname': i[2],
                'gender': i[3],
                'email': i[4],
                'password': i[5]
            }
            users.append(data)
        return jsonify(users)


@app.route('/createPost', methods=['POST'])
def create_post():
    header = request.headers.get('api-key')
    s = auth.auth(header=header)
    if s['error'] is not None:
        return s, 401
    else:
        postid = sql.last_id_post()[0]
        postid += 1
        text = request.json.get('text')
        datatime = request.json.get('datetime')
        status = request.json.get('status')
        user = request.json.get('user')
        sql.add_post(id=postid,text=text,user=user,datetime=datatime,status=status)
        dic = sql.last_id_post()
        data = {
            "id": dic[0],
            "text": dic[1],
            "user": dic[2],
            "data": dic[3],
            "status": dic[4]
        }
        return data


@app.route('/posts', methods=['GET'])
def all_posts():
    header = request.headers.get('api-key')
    s = auth.auth(header=header)
    if s['error'] is not None:
        return s, 401
    else:
        data = sql.all_posts()
        posts = []
        for i in data:
            data = {
                "id": i[0],
                "text": i[1],
                "user": i[2],
                "data": i[3],
                "status": i[4]
            }
            posts.append(data)
        return jsonify(posts)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8888')
