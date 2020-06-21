from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Darren Neo',
        'title' : 'Results',
        'content': 'First Post Content',
        'date_posted': 'June 21, 2020'
    },
    {
        'author': 'Darren Neo',
        'title' : '2nd Result',
        'content': '2nd Post Content',
        'date_posted': 'June 22, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)
