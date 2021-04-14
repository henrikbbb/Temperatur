import numpy as np
import pandas as pd
import math
data = pd.read_csv("temperature.csv") # https://www.kaggle.com/selfishgene/historical-hourly-weather-data?select=temperature.csv
data2 = data[['datetime', 'Portland']].to_numpy()
days = np.empty([math.floor(len(data)/24), 24])

# gruppiere Tage mit jew. 24 Werten (0-23 Uhr)
for i in range(len(days)):
    day = np.empty(24)
    for j in range(24):
        day[j] = data2[i*24 + j][1]
    days[i] = day

# erstelle falsche Werte
import random
size = len(days)
fakes = np.empty([size, 24])
for i in range(len(fakes)):
    fake = np.empty(24)

    x1 = random.uniform(0, 10)
    x2 = 2*x1 + 270
    y1 = x1 + 5
    y2 = x2/2 + 155

    span = random.uniform(x1, y1)
    center = random.uniform(x2, y2)
    t = 24

    for j in range(len(fake)):
        if j > 0 and 0.15 > random.uniform(0, 1):
            fake[j] = fake[j-1]
        else:
            temperature = center + math.cos(2*math.pi*j/t)*span*random.uniform(0.9, 1.1)
            r = 1
            error = random.uniform(-r, r)
            fake[j] = temperature + error
    fakes[i] = fake

x = np.concatenate((days, fakes), axis=0)
y = np.concatenate((np.zeros(len(days)), np.ones(len(fakes))), axis=0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, shuffle=True)

from sklearn import svm
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test)
print('accuracy: ' + str(accuracy_score(y_test, y_pred)))

from sklearn import metrics
disp = metrics.plot_confusion_matrix(clf, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
import matplotlib.pyplot as plt
plt.show()

newData = np.empty([len(x), 25])
for i in range(len(x)):
    newData[i] = np.append(x[i], [y[i]])
np.savetxt("newData.csv", newData, fmt='%.2f', delimiter=",")

import matplotlib.pyplot as plt
# fig, axs = plt.subplots(2)
for i in range(20):
    n = random.randint(0, len(days)-1)
    # axs[0].plot(days[n])
    # axs[1].plot(fakes[n])
    plt.plot(fakes[n])
plt.title('falsche Werte')
plt.show()
