
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>AIVORA | Welcome</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #080d27, #25205a);
            color: white;
            min-height: 100vh;
        }

        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 25px 8%;
        }

        .logo {
            font-size: 30px;
            font-weight: bold;
            color: #a99bff;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
        }

        .hero {
            min-height: 80vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            padding: 30px;
        }

        .hero h1 {
            font-size: 65px;
            margin-bottom: 20px;
        }

        .hero h1 span {
            color: #a99bff;
        }

        .hero p {
            font-size: 19px;
            color: #d0d0e8;
            max-width: 600px;
            line-height: 1.7;
        }

        button {
            margin-top: 30px;
            padding: 15px 35px;
            background: #8874ff;
            color: white;
            border: none;
            border-radius: 30px;
            font-size: 17px;
            cursor: pointer;
        }

        button:hover {
            background: #6b55e8;
        }

        footer {
            text-align: center;
            padding: 20px;
            color: #aaa;
        }
    </style>
</head>

<body>

    <nav>
        <div class="logo">AIVORA.</div>

        <div>
            <a href="/">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    <section class="hero">
        <h1>Welcome to <span>AIVORA</span></h1>

        <p>
            Turning innovative ideas into intelligent solutions.
            Discover a smarter way to solve real-world problems
            with technology and creativity.
        </p>

        <button onclick="alert('Welcome to AIVORA!')">
            Get Started →
        </button>
    </section>

    <footer>
        © 2026 AIVORA | Built for Make-A-Ton 9.0
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
