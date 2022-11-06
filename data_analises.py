import json
import matplotlib

list_of_lists = []
for step in range(0, 250, 50):
    file_name = f'data/statistics_step_{step}.json'
    with open(file_name) as f:
        response_dict = json.load(f)
        response_list = response_dict["data"]["records"]
        list_of_lists.append(response_list)

print(len(list_of_lists))

dates, days, all_personnel_units, all_tanks, all_armoured_fighting_vehicles = [], [], [], [], []
all_artillery_systems, all_mlrs, all_aa_warfare_systems, all_planes, all_helicopters = [], [], [], [], []
all_vehicles_fuel_tanks, all_warships_cutters, all_cruise_missiles, all_uav_systems = [], [], [], []
all_special_military_equip, all_atgm_srbm_systems = [], []
for list_of_dict in list_of_lists:
    for data_dict in list_of_dict:
        date = data_dict["date"]
        day = data_dict["day"]
        personnel_units = data_dict["stats"]["personnel_units"]
        tanks = data_dict["stats"]["tanks"]
        armoured_fighting_vehicles = data_dict["stats"]["armoured_fighting_vehicles"]
        artillery_systems = data_dict["stats"]["artillery_systems"]
        mlrs = data_dict["stats"]["mlrs"]
        aa_warfare_systems = data_dict["stats"]["aa_warfare_systems"]
        planes = data_dict["stats"]["planes"]
        helicopters = data_dict["stats"]["helicopters"]
        vehicles_fuel_tanks = data_dict["stats"]["vehicles_fuel_tanks"]
        warships_cutters = data_dict["stats"]["warships_cutters"]
        cruise_missiles = data_dict["stats"]["cruise_missiles"]
        uav_systems = data_dict["stats"]["uav_systems"]
        special_military_equip = data_dict["stats"]["special_military_equip"]
        atgm_srbm_systems = data_dict["stats"]["atgm_srbm_systems"]
        dates.append(date)
        days.append(day)
        all_personnel_units.append(personnel_units)
        all_tanks.append(tanks)
        all_armoured_fighting_vehicles.append(armoured_fighting_vehicles)
        all_artillery_systems.append(artillery_systems)
        all_mlrs.append(mlrs)
        all_aa_warfare_systems.append(aa_warfare_systems)
        all_planes.append(planes)
        all_helicopters.append(helicopters)
        all_vehicles_fuel_tanks.append(vehicles_fuel_tanks)
        all_warships_cutters.append(warships_cutters)
        all_cruise_missiles.append(cruise_missiles)
        all_uav_systems.append(uav_systems)
        all_special_military_equip.append(special_military_equip)
        all_atgm_srbm_systems.append(atgm_srbm_systems)

print(days)
print(all_personnel_units)





