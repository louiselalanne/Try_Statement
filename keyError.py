#keyError
dictionary ={"fruit" : "mango",
            "color":"pink",
            "bird":"parrot"}

try:
    print(dictionary["animal"])
except(KeyError):
    print("key animal is not present in dictionary")

#indexError
mylist=[0,1,2,3]

try:
    print(mylist[5])
except IndexError:
    print("Matheus feio")