"""
 import matplotlib.pyplot as plt
%matplotlib inline

plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 2))

axes[0].plot(x, y, color="green", lw=3)
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')

axes[1].plot(x, z, color="blue", lw=2, ls='--')
axes[1].set_xlabel('x')
 axes[1].set_ylabel('z')
 """
"""
import seaborn as sns
iris = sns.load_dataset('iris')
sns.pairplot (iris, hue = 'species', palette = 'pastel')
"""
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=9381243783,phoneno=9*8*7)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)