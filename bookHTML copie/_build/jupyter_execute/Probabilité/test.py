#!/usr/bin/env python
# coding: utf-8

# # Test live code

# In[1]:


import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

z =   [[2, 4, 7, 12, 13, 14, 15, 16],
       [3, 1, 6, 11, 12, 13, 16, 17],
       [4, 2, 7, 7, 11, 14, 17, 18],
       [5, 3, 8, 8, 13, 15, 18, 19],
       [7, 4, 10, 9, 16, 18, 20, 19],
       [9, 10, 5, 27, 23, 21, 21, 21],
       [11, 14, 17, 26, 25, 24, 23, 22]]

fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Without Smoothing', 'With Smoothing'))

fig.add_trace(go.Contour(z=z, line_smoothing=0), 1, 1)
fig.add_trace(go.Contour(z=z, line_smoothing=0.85), 1, 2)

fig.show()


# In[2]:


get_ipython().run_line_magic('load_ext', 'tikz_magic')


# In[3]:


get_ipython().run_cell_magic('tikz', '', '\\begin{tikzpicture}\n\\begin{axis}[xmax=9,ymax=9, samples=50]\n  \\addplot[blue, ultra thick] (x,x*x);\n  \\addplot[red,  ultra thick] (x*x,x);\n\\end{axis}\n\\end{tikzpicture}')


# In[ ]:




