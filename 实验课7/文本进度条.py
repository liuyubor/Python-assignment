import time
scale = 50
for i in range(scale + 1):
    a = (i/scale)*100
    print("\rString{} {:^3.0f}%".format('.'*3,a),end = '')
    time.sleep(0.1)
print("\rString{} Done!".format('.'*3,))