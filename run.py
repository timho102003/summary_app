import openai


def call(**input):
    openai.api_key = input["api_key"]
    messages = [
        {"role": "system", "content": "You are a very professional news artlce summization and analysis agent."},
        {"role": "user", "content": input["article"]},
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        answer = response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        answer = e
    # print(answer)
    return {"response": answer}


if __name__ == "__main__":
    article = """
        A number of countries -- including the United States, the United Kingdom, Sweden, Spain, the Netherlands, Japan, Italy, Germany, France and Canada -- airlifted and evacuated diplomats, embassy staff and others from Sudan's war-torn capital over the weekend. Both the U.S. and Canadian governments also announced temporary suspensions of operations at their embassies in Khartoum. Summarize the above article. 
    """
    api_key = input("openai api-key: ")
    answer = call(api_key=api_key, article=article)
    print(answer)
