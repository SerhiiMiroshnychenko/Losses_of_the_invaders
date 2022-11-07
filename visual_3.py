import matplotlib.pyplot as plt

from data_analises import days, all_tanks, all_artillery_systems, all_uav_systems


plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(days, all_tanks, color='red', edgecolor='none', s=50,
           label="Танки")
ax.scatter(days, all_artillery_systems, color='orange', edgecolor='none', s=50,
           label="Атр.системи")
ax.scatter(days, all_uav_systems, color='grey', edgecolor='none', s=50,
           label="БПЛА")

ax.set_title('Втрати техніки русорейху по дням війни.\nТанки, артсистеми, безпілотники.', fontsize=24)
ax.set_xlabel('День війни', fontsize=24)
ax.set_ylabel('Втрати техніки, од.', fontsize=24)
ax.legend()
ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 260, 0, 3000])  # ax.axis([min_x, max_x, min_y, max_y])

plt.show()