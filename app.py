from flask import Flask, jsonify, render_template, request
import openai
import model.py
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


def find_role():
    # find role in the croma DB
    role_str = ""
    return role_str
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
    





        
        

if __name__ == "__main__":
    app.run(debug=True)
