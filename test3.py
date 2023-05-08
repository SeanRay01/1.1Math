import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()  # 建立單一圖表
ax.set_xlim(0,10)         # 設定 x 軸範圍 0～10
ax.set_ylim(0,10)         # 設定 y 軸範圍 0～10

def init():
    ax.scatter(2, 8)      # 一開始要執行的韓式，在 (2,8) 的位置畫點

def run(data):
    if data>0:
        ax.scatter(data, data)    # 如果資料大於 0，就在圖表上畫點
    else:
        pass

ani = animation.FuncAnimation(fig, run, frames=10, interval=10, init_func=init)  # 製作動畫
ani.save('animation.gif', fps=10)   # 儲存為 gif
plt.show()