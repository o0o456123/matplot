
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests 
import matplotlib.pyplot as plt
import numpy as np


# In[37]:


x1 = np.arange(0,360,5)
y1 = np.sin(x1 * np.pi / 180.0)

x2 = x1
y2 = np.cos(x2 * np.pi / 180.0)

x3 = x1
y3 = np.tan(x3 * np.pi / 180.0)
plt.subplot(231)
plt.plot(x1,y1,lw=3)
plt.subplot(232)
plt.plot(x2,y2,"ro")
plt.subplot(236)
plt.plot(x3,y3,"y--",lw=1)

plt.ylabel("y_label")
plt.xlabel("x_label")
plt.title("Title")

plt.xlim(-30,390)
plt.ylim(-5,5)

plt.show()
