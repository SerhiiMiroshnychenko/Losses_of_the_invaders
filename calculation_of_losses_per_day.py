from data_analises import all_personnel_units

losses_per_days = [all_personnel_units[0]]
print(losses_per_days)
for i in range(1, len(all_personnel_units)):
    losses_per_day = all_personnel_units[i] - all_personnel_units[i-1]
    losses_per_days.append(losses_per_day)
print(losses_per_days)
print(len(losses_per_days))
print(len(all_personnel_units))
print(losses_per_days[16])
losses_per_days[16] = 226
