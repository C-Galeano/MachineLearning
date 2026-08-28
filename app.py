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

==> Supervised Learning (with labeled data)

Supervised Learning is a type of machine learning where a computer learns from labeled data.
Labeled data means that the information already has a correct answer or category.
During the training process, the computer studies many examples and tries to find patterns in the data.
When the computer makes a prediction, it compares its answer with the correct label and learns from its mistakes.
After training, the model can use what it learned to make predictions about new information that it has never seen before.

For example, supervised learning can be used to detect spam emails. We can give the computer thousands of emails that are already labeled as “spam” or “not spam.”
The computer analyzes these emails and learns patterns, such as certain words, links, or types of messages that are common in spam emails.
Later, when a new email arrives, the computer can analyze it and predict whether it is spam or not.
In this way, supervised learning is similar to learning with a teacher because the computer receives examples with the correct answers and uses them to improve its predictions.

==> Unsupervised learning (no data labeled)

Unsupervised learning is a type of machine learning in which a computer learns from data that is not labeled.
Unlabeled data are those that do not have a correct answer or category previously assigned.
During the training process, the computer analyzes numerous data and tries to find patterns, relationships or groups within the information.
Unlike supervised learning, the computer does not receive a correct answer with which to compare its results. For this reason, it must discover by itself the characteristics and relationships present in the data.
After training, the model can use patterns it has found to organize information, identify groups, or discover relationships that may not be obvious to the naked eye.

For example, unsupervised learning can be used to rank customers based on their buying habits. We can provide the computer with information about thousands of customers, such as what products they buy, how often they make purchases, and how much money they spend, without indicating which group each customer belongs to.
The computer analyzes this information and may discover different groups of clients with similar characteristics. For example, you can find one group of customers who buy frequently, another that spend large amounts of money, and another that make occasional purchases.
In this way, unsupervised learning is similar to discovering groups by oneself, as the computer does not receive the correct categories and must find patterns and relationships in the data autonomously.

==> Reinforcement Learning (no labeled data, but with rewards)

Reinforcement learning is a type of machine learning in which a computer learns by interacting with an environment and receiving rewards or penalties based on the actions it takes.
Unlike supervised learning, the computer is not given a dataset containing the correct answer for every situation. Instead, it must learn through trial and error, discovering which actions produce better results over time.
During the learning process, the computer, called an agent, observes the current situation of its environment and chooses an action. After performing that action, the environment changes and the agent receives a reward or penalty depending on the result.
The objective of the agent is to learn which actions should be taken in different situations in order to obtain the highest possible total reward. To accomplish this, the agent must learn from its previous experiences and improve its decisions over time.
For example, reinforcement learning can be used to teach a computer to play a video game. We can give the computer control over a character and allow it to interact with the game. 
If the character moves toward an objective, defeats an enemy, or completes a level, the computer can receive a positive reward. If it loses a life or makes an incorrect decision, it can receive a negative reward.
At the beginning, the computer may make many random or inefficient decisions because it does not know which actions are useful. However, after playing the game many times, it can remember which actions resulted in positive or negative outcomes and gradually improve its strategy.
In this way, reinforcement learning is similar to learning through experience. Instead of being directly told what the correct action is, the computer experiments with different possibilities, receives feedback from the environment, and learns which decisions are more effective.

"""
    return Response(text, mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=True)