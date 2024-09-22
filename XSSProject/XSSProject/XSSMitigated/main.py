from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    '''
    home
    :return:
    '''
    return  render_template("xssmitigated.html", textEntered="", user = "")
   # return Flask.Markup("xssmitigated.html", textEntered="", user = "")
@app.route("/handle_data", methods=['POST', 'GET'])
def handle_data():
    text = request.form['myTextArea']
    user = request.form['username']
    #print("User: " + user)
    #print(text)
    #text = "N/A"
    return render_template("xssmitigated.html", textEntered=text, user = user + " Entered:")

# Start development web server
if __name__ == '__main__':
    app.run()
