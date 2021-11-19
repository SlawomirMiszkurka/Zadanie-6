lines = ["Niebieski", "Żółty","Czerwony"]
with open("readme.txt", "w") as f:
    for line in lines:
        f.write(line)
        f.write('\n')