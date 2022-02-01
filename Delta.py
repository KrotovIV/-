def delta_fync(toponym):
    upper_corner = list(map(lambda x: float(x), toponym["boundedBy"]["Envelope"]["upperCorner"].split()))
    lower_corner = list(map(lambda x: float(x), toponym["boundedBy"]["Envelope"]["lowerCorner"].split()))
    delta_x = str((upper_corner[0] - lower_corner[0]))
    delta_y = str((upper_corner[1] - lower_corner[1]))
    return ",".join([delta_x, delta_y])
