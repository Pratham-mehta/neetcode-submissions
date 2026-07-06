from typing import List


def create_list_of_odds(n: int) -> List[int]:
    list1 = []
    if n%2!=0:
        list1.append(n)
    
    return list1



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
