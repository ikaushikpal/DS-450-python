from math import sqrt

MAIN_COLOR = (244, 204, 74)
color_maps = {'golden yellow':(254, 198, 13),
              'lemon yellow':(252, 209, 9),
              'empire yellow':(254, 200, 46),
              'lemonade':(251, 234, 85),
}
dist_maps = {}

for color in color_maps:
    c1 = MAIN_COLOR
    c2 = color_maps[color]
    d = sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2)
    dist_maps[color] = d


# sort dist_maps based on values
sorted_dist_maps = sorted(dist_maps.items(), key=lambda x: x[1])

print(sorted_dist_maps)