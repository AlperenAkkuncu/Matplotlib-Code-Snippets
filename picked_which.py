import matplotlib.pyplot as plt
import numpy as np

def on_pick(event):
    if(event.artist == sine_0):
        text.set_text("sine_0 picked!")
        sine_0.set_linewidth(5)
        sine_1.set_linewidth(2)
        sine_0.set_zorder(1)
        sine_1.set_zorder(0)
        plt.draw()
    elif(event.artist == sine_1):
        text.set_text("sine_1 picked!")
        sine_0.set_linewidth(2)
        sine_1.set_linewidth(5)
        sine_0.set_zorder(0)
        sine_1.set_zorder(1)
        plt.draw()

# make data
x = np.linspace(0, 10, 1000)
y0 = 4 + 2 * np.sin(2 * x) #sine_0 data
y1 = 4 + 2.8 * np.sin(4 * x) #sine_1 data

# plot
fig, ax = plt.subplots()

sine_0, = ax.plot(x, y0, linewidth=2.0, #get Line2D object, VITAL!
                    picker=True, pickradius=5) 
sine_1, = ax.plot(x,y1, linewidth=2.0,  #get Line2D object, VITAL!
                    picker=True, pickradius=5)

pickevent_ID = plt.connect('pick_event', on_pick)

#text for showing which line is picked
text = plt.text(0.5,7.4, "no pick", fontweight='bold', fontsize='large')
text.set_bbox(dict(facecolor='red', alpha=0.5, boxstyle="Round"))

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))
plt.tight_layout()
plt.show()
