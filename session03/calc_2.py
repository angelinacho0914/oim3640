from cmath import sqrt

# ex02-01
r = 5
pi = 3.1415926
volume = (4 / 3) * pi * sqrt(r)
print(f"The volume of a sphere with radius 5 is {volume:.2f} cubic cm.")

# ex02-02
total = 24.95 * 0.6 + 3 + 0.75 * 59
print(f"The wholesale cost for 60 copies is ${total}.")

# ex02-03
# leaves at 6:52am and run 1 mile at an easy pace (8:15 per mile),  then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?
breakfast = "7:29"
print(f"I would get home at {breakfast} am for breakfast.")

# ex02-04
# If my average grade rises from 82 to 89. What is the percentage of the increase?
# Format the result as xx.x%. Keep one figure after decimal point.
percentage = (89 - 82) / 82
print(f"The perventage of the increase is {percentage:.1f}%.")
