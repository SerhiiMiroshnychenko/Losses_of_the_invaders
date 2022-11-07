import matplotlib.pyplot as plt

from data_analises import days, all_mlrs, all_aa_warfare_systems, all_planes, all_helicopters, \
    all_cruise_missiles, all_special_military_equip


plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(days, all_mlrs, color='red', edgecolor='none', s=50,
           label="РСЗВ")
ax.scatter(days, all_aa_warfare_systems, color='orange', edgecolor='none', s=50,
           label="Засоби ППО")
ax.scatter(days, all_planes, color='blue', edgecolor='none', s=50,
           label="Літаки")
ax.scatter(days, all_helicopters, color='green', edgecolor='none', s=50,
           label="Гвинтокрили")
ax.scatter(days, all_cruise_missiles, color='purple', edgecolor='none', s=50,
           label="Крилаті ракети")
ax.scatter(days, all_special_military_equip, color='grey', edgecolor='none', s=50,
           label="Спец.техніка")

ax.set_title('Втрати техніки русорейху по дням війни.\nЛітаки, гвинтокрили, крилаті ракети, РСЗВ та ін.', fontsize=20)
ax.set_xlabel('День війни', fontsize=24)
ax.set_ylabel('Втрати техніки, од.', fontsize=24)
ax.legend()
ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 260, 0, 400])  # ax.axis([min_x, max_x, min_y, max_y])

plt.show()