from flask import Flask, jsonify, render_template, request
import openai
from apikey import OPEN_AI_KEY

default_response = "This information is not available at the moment.For more queries can contact our executive"

app = Flask(__name__)

openai.api_key = OPEN_AI_KEY

def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        messages=[
            {"role": "system", "content": "role"},
            {"role": "user", "content": prompt}
        ],
        model='model_name',
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response['choices'][0]['message']['content']
    return answer


# this renders a html template for the user
@app.route("/")
def index():
    return render_template("index.html")


# post method to request the gpt model to answer the question asked by user
@app.route("/ask", methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = ask_gpt3(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
