from flask import Flask, render_template_string

app = Flask(__name__)

@app.get("/")
def root():
    print("Running sucessfully!")
    return "Running Sucessfully!"

if __name__ == "__main__":
    app.run(debug=True)