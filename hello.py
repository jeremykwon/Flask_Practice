from flask import (Flask, url_for, render_template, request, redirect, abort)

app = Flask(__name__)  # flask class의 인스턴스 생성. ( 플라스크에서 템플릿이나 정적파일을 찾을때 필요하다)


# url route
@app.route('/')
def hello():
    return "hello, world"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('test'))  # 리다이렉션
    else:
        abort(401)  # 에러


@app.errorhandler(404)
def page_not_found(error):
    """
    에러페이지 변경
    """
    return render_template('page_not_found.html'), 404  # 404일때의 페이지





if __name__ == '__main__':
    # debug true 의 경우 코드 변경시 알아서 서버 재시작
    app.run(host='0.0.0.0', port=9999, debug=True)  # 운영서버에서 debug 모드 사용시 보안문제 발생가능성 있음
