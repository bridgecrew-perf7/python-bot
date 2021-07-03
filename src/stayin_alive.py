'''
Whether you're a brother or whether you're a mother
You're stayin' alive, stayin' alive
Feel the city breakin' and everybody shakin'
And we're stayin' alive, stayin' alive
Ah, ha, ha, ha, stayin' alive, stayin' alive

Ahora en serio, este código va a mantener vivo al bot por
y para siempre, a no ser que se acabe la existencia
'''

#!/usr/bin/env python

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()