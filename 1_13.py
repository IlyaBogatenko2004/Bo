# задача M
children = int(input())
candies = int(input())
candies_per_child = candies // children
remaining_candies = candies % children
print(candies_per_child)
print(remaining_candies)