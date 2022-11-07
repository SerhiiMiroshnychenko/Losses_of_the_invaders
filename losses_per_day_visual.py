from plotly import offline
import matplotlib.pyplot as plt

from data_analises import dates, days, all_personnel_units
from calculation_of_losses_per_day import losses_per_days

# Зробити візуалізацію
data = [{
    'type': 'bar',  # Тип діаграми: стовпчикова
    'x': days,  # Вісь х: посилання
    'y': losses_per_days,  # Вісь у: зірочки
    'hovertext': dates,  # Підказки
    'marker': {
        'color': "red",  # Блакитний колір стовпчиків
        'line': {'width': 0.5, 'color': 'rgb(5, 5, 5)'}  # Сірий колір завтовшки 1,5 пікселей
    },
    'opacity': 0.6,  # Прозорість стовпчиків 0,6
}]

my_layout = {  # Опис компонування, назви діаграми та осей
    'title': 'Подобові втрати москалів',
    'titlefont': {'size': 28},  # Розмір шрифту в назві діаграми
    'xaxis': {
        'title': 'Дні війни',
        'titlefont': {'size': 24},  # Розмір літер в назві осі х
        'tickfont': {'size': 14},  # Розмір літер підписів для розмітки
    },
    'yaxis': {
        'title': 'Втрати особового складу, моск.',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='losses_of_orcs.html')

plt.style.use('dark_background')
fig, ax = plt.subplots()
point_numbers = range(len(all_personnel_units))
ax.scatter(days, losses_per_days, losses_per_days, c="red", alpha=0.5, marker=r'$\plus$',
           label="Мертві москалі")

ax.set_title('ДИНАМКА ЩОДОБОВИХ ВТРАТ МОСКАЛІВ', fontsize=24)
ax.set_xlabel('День війни', fontsize=24)
ax.set_ylabel('Втрати росіян в день', fontsize=24)
ax.legend()

ax.tick_params(axis='both', labelsize=14)

# Задати діапазон для кожної осі
ax.axis([0, 260, 0, 3500])  # ax.axis([min_x, max_x, min_y, max_y])

plt.show()
