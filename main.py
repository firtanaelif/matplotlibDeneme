import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 7
means_ay = (8, 12, 5, 10, 12, 11, 9)
means_puan = (9.5, 9.2, 9.2, 8.3, 9.8, 7.8, 6.6)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_ay, bar_width,
alpha=opacity,
color='b',
label='Y. Ayi')

rects2 = plt.bar(index + bar_width, means_puan, bar_width,
alpha=opacity,
color='g',
label='Puani')

plt.xlabel('Diziler')
plt.ylabel('Yayin Ayi / Puani')
plt.title('Dizilerin yayin ay ve puanlari grafigi')
plt.xticks(rotation=60)
plt.xticks(index + bar_width, ('Breaking Bad', 'Rick And Morty', 'Avatar', 'Sherlock', 'Peaky Blinders','Kara Ayna', 'Tuhaf Seyler'))
plt.legend()

plt.tight_layout()
plt.show()
