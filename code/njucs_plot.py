import matplotlib.pyplot as plt
x = [1,2,3,4,5,6, 7,8,9 , 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
y = [1,2,4,8,16,32,33,34,35,36,37,38,39,40,41,42,23,24,25,26,27,28,1,2,4,9]

for a,b in zip(x,y):
    if a==6:
        plt.text(a,b+1,'%.0f' %b,ha='center',va='bottom',fontsize=10)

plt.scatter(x,y,s=20)
# 设置图表标题，并给坐标轴添加标签
#plt.title("square of 'x'", fontsize=22)
plt.xlabel("Transmission round", fontsize=10)
plt.ylabel("Congestion window size (segments)", fontsize=10)
plt.plot(x,y)

#plt.xticks([1,2,3,4,5,6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26])
plt.xticks([2,4,6, 8,10,12,14,16,18,20,22,24,26])
plt.yticks([5,10,15,20,25,30,35,40,45,50])
# 设置坐标轴刻度标记的大小
plt.tick_params(axis='both',which='major', labelsize=10)
plt.axis('tight')
plt.legend()
plt.show()