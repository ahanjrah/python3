import pandas
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")
df1 = pandas.read_csv("sample.csv")

time = list(df1.iloc[0:95, 0])
data = list(df1.iloc[0:95, 1])
# print(time)
# print(data)

plt.plot(time, data)

plt.title("license usage")

plt.show()
