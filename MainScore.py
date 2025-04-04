from flask import Flask
import Utils as utils


app = Flask(__name__)



@app.route('/')
def score_server():
    try:
        with open(utils.SCORES_FILE_NAME, 'r') as file:
            score = file.read()
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        """
    except Exception as e:
        return f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
            <body>
                <h1><div id="score" style="color:red">{e}</div></h1>
            </body>
        </html>

        """

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)