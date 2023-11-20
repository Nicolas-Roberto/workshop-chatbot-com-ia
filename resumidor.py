import dotenv
import os
import openai

dotenv.load_dotenv()

openai.api_key = "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"

def resumidor_de_historico(historico):
    pass

def criando_resumo(historico):
    resposta = resumidor_de_historico(historico=historico)
    if resposta:
        if type(resposta) != str:
            resumo = resposta.choices[0].message.content
        else:            
            resumo = resposta
    else:
        print("resposta vazia")
        resumo = ""
    return resumo