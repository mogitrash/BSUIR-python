import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-55,55,100)
y=np.linspace(-55,55,100)
x,y=np.meshgrid(x,y)
z1 = np.power(x, 0.25) + np.power(y, 0.25)
z2 = x**2 - y**2
z3 = 2*x + 3*y
z4 = x**2 + y**2
z5 = 2 + 2*x + 2*y - x**2 - y**2
plt.figure(figsize=(15,12))

# plt.subplot(321)
plt.plot(x[0,:],z1[0,:],label='z = x^0.25 + y^0.25')
plt.xlabel('X')
plt.ylabel('Z')
plt.title('z = x^0.25 + y^0.25')
plt.legend()

# plt.subplot(322)
plt.plot(x[0,:],z2[0,:],label='z = x^2 - y^2')
plt.xlabel('X')
plt.ylabel('Z')
plt.title('z = x^2 - y^2')
plt.legend()

# plt.subplot(323)
plt.plot(x[0,:],z3[0,:],label='z = 2x + 3y')
plt.xlabel('X')
plt.ylabel('Z')
plt.title('z = 2x + 3y')
plt.legend()

# plt.subplot(324)
plt.plot(x[0,:],z4[0,:],label='z = x^2 + y^2')
plt.xlabel('X')
plt.ylabel('Z')
plt.title('z = x^2 + y^2')
plt.legend()

# plt.subplot(325)
plt.plot(x[0,:],z4[0,:],label='z = 2 + 2x + 2y - x^2 - y^2')
plt.xlabel('X')
plt.ylabel('Z')
plt.title('z = 2 + 2x + 2y - x^2 - y^2')
plt.legend()
plt.tight_layout()
plt.show()