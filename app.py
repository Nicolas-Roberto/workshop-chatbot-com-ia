from flask import Flask
import os
import openai
import dotenv
from time import sleep
from helpers import *

app = Flask(__name__)
app.secret_key = 'workshop'
    
dotenv.load_dotenv()

openai.api_key = "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"

from views import *

def bot(prompt,historico):
    maxima_repeticao = 1
    repeticao = 0
    while True:
        try:
            model='gpt-3.5-turbo'
            prompt_do_sistema = f"""            
            ## Historico:
            {historico}
            """
            response = openai.ChatCompletion.create(
                messages=[
                    {
                        "role": "system",
                        "content": prompt_do_sistema
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream = True,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model = model)
            return response
        except Exception as erro:
            repeticao += 1
            if repeticao >= maxima_repeticao:
                return "Erro no GPT3: %s" % erro
            print('Erro de comunicação com OpenAI:', erro)
            sleep(1)

if __name__ == "__main__":
    app.run(debug = True)
