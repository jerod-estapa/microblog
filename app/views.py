from app import app

@app.route('/')
@app.route('/index')
def index():
				return "Well, you're a smart ass with your mouth shut!"
