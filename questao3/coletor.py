import requests
import random
import time
from datetime import datetime

def get_temperatura_motor():
        temp_motor = random.uniform(90, 104)
        return temp_motor

def get_pressao_pneus():
        pressao = random.uniform(28, 32)
        return pressao
               
def get_nivel_oleo():
        oleo = random.randint(0, 2)
        if(oleo == 0):
                return ("Muito baixo")
        elif(oleo==1):
                return ("Baixo")
        elif(oleo==2):
                return ("Bom")

def get_nivel_gasolina():
        gasolina = random.randint(0, 3)
        if(gasolina == 0):
                return ("Muito baixo")
        elif(gasolina==1):
                return ("Baixo")
        elif(gasolina==2):
                return ("Metade")
        elif(gasolina==3):
                return ("Alto")                

def get_cintos():
        cintos = random.randint(0, 1)
        if(cintos == 0):
                return ("False")
        elif(cintos==1):
                return ("True")
       

def get_temperatura_externa():
        temp_externa = random.uniform(20, 35)
        return temp_externa
                        
def get_modo_conducao():
        conducao = random.randint(0, 2)
        if(conducao == 0):
              return "ECO"
        elif(conducao==1):
              return "Esportivo"
        elif(conducao==2):
              return "Conforto"        

def get_velocidade():
        velocidade = random.randint(0, 110)
        return velocidade

def get_date_time():
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string

def get_farois():
        farois = random.randint(0, 2)
        if(farois == 0):
                return ("Desligado")
        elif(farois==1):
                return ("Baixo")
        elif(farois==2):
                return ("Alto")


while True:

        dados = dict()
        dados['date time']=get_date_time()
        dados['velocidade']= get_velocidade()
        dados['temperatura motor']=get_temperatura_motor()
        dados['pressao pneus']=get_pressao_pneus()
        dados['nivel oleo']=get_nivel_oleo()
        dados['nivel gasolina']=get_nivel_gasolina()
        dados['cintos de seguranca']=get_cintos()
        dados['temperatura externa']=get_temperatura_externa()
        dados['modo de conducao']=get_modo_conducao()
        dados['status farois']=get_farois()

        r = requests.post('http://127.0.0.1:8000', data=dados)
        time.sleep(0.2)


