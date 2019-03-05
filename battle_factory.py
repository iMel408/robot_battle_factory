from datetime import datetime
from random import sample

file = open('robot_names.txt')
lines = file.read().splitlines()
names = sample(lines, len(lines))
teams = ['Good', 'Evil']

class Robot(object):

    def __init__(self,team):

        self.unit_id = id(self)
        self.unit_name = names.pop(0)
        self.status = 'active'
        self.team = team
        self.date_built = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.health_level = 100
        self.charge_level = 100


class Battle(object):

    def __init__(self,battle_name,user_name,team_size):

        self.robots = []
        self.team_size = team_size
        self.id = id(self)
        self.name = battle_name
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.owner_id = user_name


    def add_robot(self,team):

        new_robot = Robot(team)
        self.robots.append(new_robot)


def battle_factory(team_size):

    instance = Battle('Mordor','Melissa',team_size)


    for team in teams:
        for i in range(instance.team_size):
           instance.add_robot(team)

    return instance


new_battle = battle_factory(10)

print("[Battle Name]:", new_battle.name)
for robot in new_battle.robots:
    print("[Team]:",robot.team, "[Unit Name]:",robot.unit_name)



# print(names)

# print("unit_id:", battle.robots[0].unit_id)
# print("unit_name:", battle.robots[0].unit_name)
# print("date_built:", battle.robots[0].date_built)