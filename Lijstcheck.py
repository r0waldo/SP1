# Opdracht 3.A
def count():
    lijst=[12,2,3,34,56,76,54,34,56,34,22,34]
    for x in lijst:
        count = lijst.count(x)
        print(x, count)
count()

#Opdracht 3.B
def verschil():
    lijst_positief=[]
    lijst = [12,2,3,34,56,76,54,34,56,34,22,34]
    verschil = [j - i for i, j in zip(lijst[: -1], lijst[1:])]
    for x in verschil:
        boykan = [abs(x)]
        lijst_positief.append(boykan)
    print(max(lijst_positief))
verschil()
# https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/

# Opdracht 3.C
def count():
    lijst=[12,2,3,34,56,76,54,34,56,34,22,34]
    for x in lijst:
        count = lijst.count(x)
        print(x, count)
count()
