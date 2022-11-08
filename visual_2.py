import matplotlib.pyplot as plt

from data_analises import days, all_armoured_fighting_vehicles, all_vehicles_fuel_tanks


plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(days, all_armoured_fighting_vehicles, color='red', edgecolor='none', s=50,
           label="Броньовані бойові машини")
ax.scatter(days, all_vehicles_fuel_tanks, color='orange', edgecolor='none', s=50,
           label="Автотехніка та автоцистерни")

ax.set_title('Втрати техніки русорейху по дням війни.\nББМ та допоміжна техніка.', fontsize=24)
ax.set_xlabel('День війни', fontsize=24)
ax.set_ylabel('Втрати техніки, од.', fontsize=24)
ax.legend()
ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 260, 0, 6000])  # ax.axis([min_x, max_x, min_y, max_y])

plt.show()
