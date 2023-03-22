with open("data/journal.0006.txt", encoding="windows-1252") as f:
    lines = f.readlines()

nb_stairs_created = 0
nb_ceilings_created = 0
nb_windows_created = 0
nb_floors_created = 0
nb_doors_created = 0


for line in lines:
    stripped_line = line.strip()
    if stripped_line.startswith("'"):  # comment
        continue
    if stripped_line.startswith('Jrn.Command "Ribbon"'):
        splitted_line = stripped_line.split(",")
        if "ID_OBJECTS_STAIRS" in splitted_line[2]:
            nb_stairs_created += 1
        elif "ID_OBJECTS_CEILING" in splitted_line[2]:
            nb_ceilings_created += 1
        elif "ID_OBJECTS_WINDOW" in splitted_line[2]: 
            nb_windows_created += 1
        elif "ID_OBJECTS_FLOOR" in splitted_line[2]:
            nb_floors_created += 1
        elif "ID_OBJECTS_DOOR" in splitted_line[2]:
            nb_doors_created += 1

print("nb_stairs_created: ", nb_stairs_created)
print("nb_ceilings_created: ", nb_ceilings_created)
print("nb_windows_created: ", nb_windows_created)
print("nb_floors_created: ", nb_floors_created)
print("nb_doors_created: ", nb_doors_created)
