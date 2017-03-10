from flask import Flask, request, render_template
import videomash

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'no one')
    age = request.args.get('age', 'no one')
    return render_template("home.html", name=name, age=age)

@app.route('/create')
def create():
    phrase1 = request.args.get('phrase1', '')
    phrase2 = request.args.get('phrase2', '')
    
    outfile = 'static/' + phrase1 + phrase2 + '.mp4'
    outfile = outfile.replace(' ', '_')
    videomash.mash(phrase1, phrase2, outfile)

    return render_template('video.html', vid=outfile)
# @app.route('/')
# def home():
#     name = request.args.get('name', 'no one')
#     age = request.args.get('age', 'no one')
#     return render_template("home.html", name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
