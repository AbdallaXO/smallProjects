import inflect
def get_names():
    names = []
    while True:
        try:
            name=input("Name: ").capitalize()
            names.append(name)    
        except KeyboardInterrupt:
            return names
            
        
def adieu_format(names="world"):
    p = inflect.engine()
    adieu = "Adieu, adieu, to"
    return f"{adieu} {p.join(names)}"
    
if __name__ == "__main__":
    names = get_names()
    print(adieu_format(names))