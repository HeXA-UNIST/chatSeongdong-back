import openai


def ask_model1(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "경증장애수당 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjHyCdt',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model2(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "고속도로 통행료 50%할인 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjO2VRx',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model3(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "공공시설 요금 감면 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjTQVnS',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer
def ask_model4(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "공영주차장 주차요금 감면 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjUSehM',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer
def ask_model5(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "관련사이트 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjWwS11',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer
def ask_model6(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "교통요금 할인 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjmJnNS',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer
def ask_model7(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "국민기초생활보장제도 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8Ojhd7Zy',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer



def ask_model8(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "긴급복지지원 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8Ok4cubc',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model9(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "노인맞춤돌봄서비스 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8Ok7fGWS',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model10(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "도시가스 요금 할인 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OjzkqrH',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model11(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "도시철도채권 구입의무 면제 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OkKuQc6',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model12(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "상속세 상속공제 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8OkOW0jL',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

def ask_model13(prompt):
    response = openai.ChatCompletion.create(
    messages=[
        {"role": "system", "content": "서울형 기초보장제도 정보 제공 쳇봇"},
        {"role": "user", "content": prompt}
    ],
    model='ft:gpt-3.5-turbo-0613:personal::8Oka0nQO',
    temperature=0.7,
    max_tokens=100,
    n=1,
    stop=None,
    frequency_penalty=0,
    presence_penalty=0
)

    answer = response['choices'][0]['message']['content']
    return answer

