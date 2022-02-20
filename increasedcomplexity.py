angle = float(input("enter angle"))
minutes = int(2*angle) % 60
hours = int(angle/30)
print("minutes {0}, hours {1}".format(minutes, hours))