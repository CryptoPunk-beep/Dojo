# Este código implementa um "Dead Man Switch" simples. Ele verifica periodicamente se um check-in foi realizado. 
# Se o check-in falhar após um certo tempo, uma ação de emergência é executada. 
# Para simular o check-in, usamos um temporizador. 
# O código usa a biblioteca `time`, que já vem instalada com Python.

import time
import threading

def check_in():
    global last_check_in
    while True:
        time.sleep(5)  # Simula um check-in a cada 5 segundos
        last_check_in = time.time()
        print("Check-in realizado.")

def dead_man_switch():
    while True:
        time.sleep(10)  # Tempo limite para o check-in
        if time.time() - last_check_in > 10:
            print("Ação de emergência: Check-in falhou!")

last_check_in = time.time()
threading.Thread(target=check_in, daemon=True).start()
dead_man_switch()