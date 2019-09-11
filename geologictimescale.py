year = float(input('Year'))

time_periods = {
    "Holocene": (0,.008),
    "Pleistocene": (.008,1.8),
    "Pliocene": (1.8,5.3),
    "Miocene": (5.3,23.8),
    "Oligocene": (23.8,33.7),
    "Eocene": (33.7,55.5),
    "Paleocene": (55.5,65),
    "Cretaceous": (65,145),
    "Jurassic": (145,213),
    "Triassic": (213,248),
    "Permian": (248,286),
    "Pennsylvanian": (286,325),
    "Mississippian": (325,360),
    "Devonian": (360,410),
    "Silurian": (410,440),
    "Ordovician": (440,505),
    "Cambrian": (505,544)
}

for name,(begin,end) in time_periods.items():
    if begin <= year <= end:
        tail = '{} million years ago was the geologic period known as {} according to USGS,2001.'.format(year, name)
        print(tail)
        break
