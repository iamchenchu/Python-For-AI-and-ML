from enum import Enum

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print("The enum member associated with value 2 is : ", Season(2).name)
print("The enum member associated with name AUTUMN is : ", Season['AUTUMN'].value)

for season in (Season):
    print(season.value, "-", season)

