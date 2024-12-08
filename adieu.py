import inflect
p = inflect.engine()
names = []
adieu = "Adieu, adieu, to"
while True:
    try:
        name=input("Name: ").capitalize()
        names.append(name)    
    except eof:
        print(f"{adieu} {p.join(names)}")
        break
        ## to break
        
