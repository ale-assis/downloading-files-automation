#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pyautogui as pg
import time

time.sleep(5)
pg.position()


# In[33]:


trigger = input('Deseja iniciar a automação? ')

while trigger == 'S':
    pg.PAUSE = 2

    pg.hotkey('ctrl', 'tab')
    pg.hotkey('ctrl', 'tab')
    pg.click(x=236, y=48)
    pg.hotkey('ctrl', 'c')
    pg.hotkey('ctrl','shift','tab')
    pg.click(x=244, y=272)
    pg.hotkey('ctrl', 'v')
    pg.press('enter')

    time.sleep(5) # esperando a verificação 
    pg.click(x=488, y=362)
    time.sleep(10) # esperando o arquivo ficar pronto
    pg.click(x=408, y=301) # clicou no link de download
    time.sleep(3)
    pg.press('enter')
    time.sleep(1.5)
    pg.click(x=116, y=124) # clicou para voltar para a HOME do site
    pg.hotkey('ctrl', 'tab')
    pg.hotkey('ctrl', 'w')
    pg.hotkey('ctrl', 'shift', 'tab')
    pg.hotkey('ctrl', 'shift', 'tab')
    trigger = input('Deseja continuar? S/N')
print('Automação finalizada com sucesso!')


# In[ ]:





# In[ ]:




