from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define a basic route
@app.route('/')
def hello_world():
    return "Hello, World!"

# Run the app when executed directly
if __name__ == "__main__":
    app.run(debug=True)