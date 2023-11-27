from flask import Flask, jsonify, render_template, request
import openai
from apikey import OPEN_AI_KEY
import chromadb
import jsonlines
import model
import os
from flask_cors import CORS
default_response = "This information is not available at the moment.For more queries can contact our executive"

app = Flask(__name__)
CORS(app)
openai.api_key = OPEN_AI_KEY

client = chromadb.PersistentClient()
posts = client.get_or_create_collection(
    name = "posts"
)
ids_input=[str(i+1) for i in range(761)]


print(os.getcwd())
hn_dataset = []
with jsonlines.open("./chatSeongdong-back/mo.jsonl") as f:
    for line in f.iter():
        hn_dataset.append(line["messages"][1]["content"])


posts.add(
    documents=hn_dataset,
    ids = ids_input
)




# this renders a html template for the user
@app.route("/")
def index():
    return render_template("index.html")


# post method to request the gpt model to answer the question asked by user
@app.route("/ask", methods=['POST'])
def ask():
    user_input = request.form['user_input']
    result =posts.query(
        query_texts=[user_input],
        n_results=1
    )

    result_query = result["documents"][0][0]
    chat_bot = None
    with jsonlines.open("./chatSeongdong-back/mo.jsonl") as f:
        for line in f.iter():
            if line["messages"][1]["content"] == result_query:
                chat_bot = line["messages"][0]["content"]

    responsed = find_model(chat_bot, user_input)

    return jsonify({"response": responsed})


def find_model(role, prompt):
    if role == "경증장애수당 정보 제공 쳇봇":
        response = model.ask_model1(prompt)
    elif role == "고속도로 통행료 50%할인 정보 제공 쳇봇":
        response = model.ask_model2(prompt)
    elif role == "공공시설 요금 감면 정보 제공 쳇봇":
        response = model.ask_model3(prompt)
    elif role == "공영주차장 주차요금 감면 정보 제공 쳇봇":
        response = model.ask_model4(prompt)
    elif role == "관련사이트 정보 제공 쳇봇":
        response = model.ask_model5(prompt)
    elif role == "교통요금 할인 정보 제공 쳇봇":
        response = model.ask_model6(prompt)
    elif role == "국민기초생활보장제도 정보 제공 쳇봇":
        response = model.ask_model7(prompt)
    elif role == "긴급복지지원 정보 제공 쳇봇":
        response = model.ask_model8(prompt)
    elif role == "노인맞춤돌봄서비스 정보 제공 쳇봇":
        response = model.ask_model9(prompt)
    elif role == "도시가스 요금 할인 정보 제공 쳇봇":
        response = model.ask_model10(prompt)
    elif role == "도시철도채권 구입의무 면제 정보 제공 쳇봇":
        response = model.ask_model11(prompt)
    elif role == "상속세 상속공제 정보 제공 쳇봇":
        response = model.ask_model12(prompt)
    elif role == "서울형 기초보장제도 정보 제공 쳇봇":
        response = model.ask_model13(prompt)

    return response


if __name__ == "__main__":
    app.run(debug=True, port=8080)
