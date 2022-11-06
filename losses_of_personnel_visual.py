import matplotlib.pyplot as plt
from data_analises import days, all_personnel_units


plt.style.use('dark_background')
fig, ax = plt.subplots()
point_numbers = range(len(all_personnel_units))
ax.scatter(days, all_personnel_units, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=1000)

ax.set_title('ВТРАТИ ОСОБОВОГО СКЛАДУ росіян ПО ДНЯМ ВІЙНИ', fontsize=24)
ax.set_xlabel('День війни', fontsize=24)
ax.set_ylabel('Втрати росіян', fontsize=24)

ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 260, 0, 80000])  # ax.axis([min_x, max_x, min_y, max_y])

plt.show()
