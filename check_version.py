import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
import matplotlib.pyplot as plt
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
from pandas.plotting import scatter_matrix
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))


# Load CSV using Pandas from URL
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
print(data.shape)

description = data.describe()
print(description)

data = pandas.read_csv(url, names=names)
scatter_matrix(data)
plt.show()