import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from utils import *

#dataset iris
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
drawConvexHull(df,data.target_names,"scipy-iris",1)
drawConvexHull(df,data.target_names,"myConvexHull-iris",0)

data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
drawConvexHull(df[['petal length (cm)','petal width (cm)','Target']],data.target_names,"scipy-iris-petal",1)
drawConvexHull(df[['petal length (cm)','petal width (cm)','Target']],data.target_names,"myConvexHull-iris-petal",0)

#bonus : dataset lain
data = datasets.load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
drawConvexHull(df,data.target_names,"scipy-wine",1)
drawConvexHull(df,data.target_names,"myConvexHull-wine",0)



