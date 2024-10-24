import datetime
import time
from matplotlib import pyplot as plt # type: ignore
import streamlit as st
import pandas as pd
import numpy as np
import subprocess


def contaProcesso():
    result = subprocess.run(['bash', '-c', 'ps aux | wc -l'], stdout=subprocess.PIPE)
    processosStr = result.stdout.decode('utf-8').strip()
    numero = int(processosStr)
    return int(numero)


processos = []
tempo = []
st.title('Processamento da máquina:')

chart_placeholder = st.empty()
while True:
    numero_processos = contaProcesso()
    processos.append(numero_processos)
    horaAtual = datetime.time.strftime
    if len(processos) > 6:
        processos.pop(0)
    plt.figure(figsize=(10, 5))
    plt.plot(processos, marker='o')
    plt.title('Gráfico que mostra o total de processos ativos na máquina')
    plt.xlabel('Tempo de execução')
    plt.ylabel('Total de processos ativos')
    plt.grid()

    chart_placeholder.pyplot(plt)

    time.sleep(10)

