from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index_view():
    return render_template('about_proj.html')
@app.route('/about')
def about_view():
    return render_template('about.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    response = "For conversion"
    return render_template('upload_audio.html')

if __name__ == "__main__":
    app.run(debug=True)
