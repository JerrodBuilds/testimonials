from testimonials import app

@app.route('/')
def index():
    return 'hello'

@app.route('/api/testimonials')
def testimonials():
    return {'testimonal': ['great', 'its ok', 'bad']}