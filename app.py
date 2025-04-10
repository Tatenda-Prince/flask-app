from flask import Flask, render_template_string

app = Flask(__name__)

chelsea_homepage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chelsea FC - The Pride of London</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #034694;
            color: white;
            text-align: center;
            margin: 0;
            padding: 50px;
        }
        h1 {
            font-size: 3em;
        }
        .logo {
            width: 200px;
            margin-top: 20px;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <img src="https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg" class="logo">
    <h1>Welcome to Chelsea FC!</h1>
    <p>The Pride of London</p>
    <p>🏆 Champions League Winners | 🏆 Premier League Champions | 🏆 FA Cup Legends</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(chelsea_homepage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

