from flask import Flask,render_template
from utils import get_score,BAD_RETURN_CODE
def score_server():
    current_score = get_score()
    if current_score is not None:
        return render_template('score.html',SCORE=current_score), 201
    else:
        return render_template('error.html',ERROR=BAD_RETURN_CODE), BAD_RETURN_CODE
    

app = Flask(__name__,template_folder='templates')
@app.route("/")
def score_server():
    return score_server()



if __name__ == '__main__':
    app.run()


