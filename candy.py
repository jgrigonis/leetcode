class Solution:
    def candy(self, ratings: list[int]) -> int:
        candies = [1] * len(ratings)
        for index, rating in enumerate(ratings):
            
            if index > 0 and rating > ratings[index - 1]:
                candies[index] = candies[index - 1] + 1

        for index, rating in reversed(list(enumerate(ratings))):
            
            if index + 1 < len(ratings):
                if rating > ratings[index + 1]:
                    if candies[index + 1] + 1 > candies[index]:
                        candies[index] = candies[index + 1] + 1

        print(candies)

        return sum(candies)
    
x = Solution()
print(x.candy([1, 2, 3]))
print(x.candy([1, 2, 2]))
print(x.candy([1, 0, 2]))
print(x.candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]))

print(x.candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]))
print(x.candy([20000, 20000, 16001, 16001, 16002, 16002, 16003, 16004, 16005, 16005, 16006, 16006, 16007, 16007, 16008, 16008, 16009, 16009, 16010, 16010, 16011, 16011, 16012, 16012, 16013, 16013, 16014, 16014, 16015, 16015, 16016, 16016, 16017, 16017, 16018, 16018, 16019, 16019, 16020, 16020, 16021, 16021, 16022, 16022, 16023, 16023, 16024, 16024]))

print(x.candy([3, 2, 2, 1, 3, 2, 1]))

print(x.candy([1, 2, 3, 4, 1, 2, 3, 4]))
print(x.candy([1, 3, 4, 5, 2]))


assert(x.candy([1, 2, 3]) == 6)
assert(x.candy([1, 0, 2]) == 5)
assert(x.candy([3, 2, 1]) == 6)
assert(x.candy([3, 2, 2, 1, 3, 2, 1]) == 12)
assert(x.candy([6, 7, 6, 5, 4, 3, 2, 1, 0, 0, 0, 1, 0]) == 42)
assert(x.candy([100, 80, 70, 60, 70, 80, 90, 100, 90, 80, 70, 60, 60]) == 35)
assert(x.candy([1,3,4,5,2]) == 11)
