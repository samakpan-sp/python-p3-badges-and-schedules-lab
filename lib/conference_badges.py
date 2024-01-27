def badge_maker(name):
    message = f"Hello, my name is {name}."
    print(message)
    return message
badge_maker("Ariel")

def batch_badge_creator(names):
    badges = []    
    for name in names:
        badges.append(f"Hello, my name is {name}.")   
    return badges

badegs = batch_badge_creator(["bam", "jik","yui","nmik"])
print(badegs)
print("***********")

# bady = batch_badge_creator(badegs)
# for bad in bady:
#     print(bad)

def assign_rooms(names):
    assigned_rooms = []
    available_rooms = [1, 2, 3, 4, 5, 6, 7, 8]

    for index, name in enumerate(names):
        if index < len(available_rooms):
            room = available_rooms[index]
            assigned_rooms.append(f"Hello, {name}! You'll be assigned to room {room}!")
        else:
            assigned_rooms.append(f"Hello, {name}! All rooms are filled!")

    return assigned_rooms

# Test the function
result = assign_rooms(["Arel", "Carol","jim"])
print(result)
print("***********")



def printer(names):
    big_badges = batch_badge_creator(names)
    for badge in big_badges:
        print(badge)

    newlist = assign_rooms(names)
    for list in newlist:
        print(list)
printer(["Samuel", "Money"])



