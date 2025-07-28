a1 = [1,2,4,1]

print("a1", a1)

a1_set = list(set(a1))

print("a1_set", a1_set)

class_data = {
    "students": ["Ali", "Sara"],
    "grades": [90, 85],
    "roll_no": [1,2]
}


print()
print("grades:", class_data["grades"])
print("roll_no:", class_data.get("roll_no", [0,0]))


def add(*args):
    return sum(args)
    count = 0
    for i in args:
        count += i

    return count

result = add(3, 5, 1)
print(result)

def info(name="anon"):
    print(f"My name is {name}")
    
info("farzam")
