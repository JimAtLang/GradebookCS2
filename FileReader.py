def read_file(filename):
    lines = []
    gradelist  = []
    with open("data\\" + filename) as f:
        lines = f.readlines()
        for line in lines:
            gradelist.append(line.split(","))
    return gradelist