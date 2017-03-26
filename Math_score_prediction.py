import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean
Hours_spent = [4,9,10,14,4,7,12,22,1,3,8,11,5,6,10,11,16,13,13,10]
Math_score = [390,580,650,730,410,530,600,790,350,400,590,640,450,520,690,690,770,700,730,640]
DataSet = list(zip(Hours_spent,Math_score))

df = pd.DataFrame(data = DataSet, columns = ['Hours_spent','Math_score'])

df.to_csv('Math-score.csv',index = False, header = False)
Location = r'C:\Python34\Math-score.csv'
df = pd.read_csv(Location, names = ['Hours_spent','Math_score'])

x = df['Hours_spent']
y = df['Math_score']

plt.scatter(x, y, color = 'r', label = 'Data Points')

def best_fit(x, y):
    slope_m = (((mean(x)*mean(y)) - mean(x*y)) /
               ((mean(x)*mean(x)) - mean(x*x)) )
    b = mean(y) - slope_m * mean(x)
    return slope_m, b

slope_m, b = best_fit(x, y)

regression_line = [ (slope_m*i) + b for i in x ]

plt.plot(x, regression_line, color = 'b', label = 'Best Fit Line')

predict_x = 15
predict_y = slope_m * predict_x + b

plt.scatter(predict_x, predict_y, color = 'g',s=100, label = 'Predicted Point')

plt.xlabel('Hours Spent')
plt.ylabel('Maths Score')
plt.legend()
plt.show()
