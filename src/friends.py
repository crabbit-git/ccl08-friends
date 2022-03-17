def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    return food in person["favourites"]["snacks"]
    # This is just shorthand for the following, which also works:
    # if food in person["favourites"]["snacks"]:
    #     return True
    # else:
    #     return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    bank_of_scoobland = 0
    for person in people:
        bank_of_scoobland += person["monies"]
    return bank_of_scoobland

def lend_money(lender, chancer, loan):
    lender["monies"] -= loan
    chancer["monies"] += loan

def all_favourite_foods(people):
    dream_menu = []
    for person in people:
        for snack in person["favourites"]["snacks"]:
            dream_menu.append(snack)
    return dream_menu

def find_no_friends(people):
    return [person for person in people if person["friends"] == []]

def find_mutual_friends(person1, person2):
    mutual_friends = []
    for friend in person1["friends"]:
        if friend in person2["friends"]:
            mutual_friends.append(friend)
    return mutual_friends

def find_people_who_like_tv_show(programme, people):
    programme_fans = []
    for person in people:
        if person["favourites"]["tv_show"] == programme:
            programme_fans.append(person)
    return programme_fans

def find_oldest_person(people):
    coffin_dodger = people[0]
    for person in people:
        if person["age"] > coffin_dodger["age"]:
            coffin_dodger = person
    return coffin_dodger

def all_favourite_tv_shows(people):
    tv_guide = []
    for person in people:
        if person["favourites"]["tv_show"] not in tv_guide:
            tv_guide.append(person["favourites"]["tv_show"])
    return tv_guide