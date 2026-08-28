from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/template")
def template():
    return render_template("index.html")

@app.route("/ml")
def machine_learning():
    text = """# What is Machine Learning?

Machine Learning is a part of Artificial Intelligence. In Machine Learning, a computer learns from data instead of following rules written by a programmer.

## How does it work?

In simple words:

1. The computer receives many examples of data, such as pictures of cats and dogs.
2. An algorithm looks for patterns in this data.
3. Using these patterns, the model learns to make predictions about new data that it has never seen before. For example, it can decide if a new picture shows a cat or a dog.

* Main types of Machine Learning

* **Supervised Learning:** The model learns from data that already has the correct answers or labels.
* **Unsupervised Learning:** The model looks for patterns in data without labels.
* **Reinforcement Learning:** The model learns by trying different actions and receiving rewards or punishments.

* Examples of use

* Movie or product recommendations.
* Spam detection in emails.
* Voice and image recognition.
* Price or demand prediction.

## In summary

Machine Learning is a way to teach a machine to learn from experience, using data. It can make decisions or predictions without a programmer writing every rule directly.

"""
    return Response(text, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)