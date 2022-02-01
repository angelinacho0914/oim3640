# 1.1
a = 3
a = a + 2
# Type: int. Value: a = 5

# 1.2
a = a + 1.0
a
# Type: float. Value: a = 6.0

# 1.3
a = 3
# b
# Type: undefined. Value: a = 3 b = undefined

# 1.4
a = 3
print(a == 5.0)
a
# Type: a = int. Value: a = 3

# 1.5
b = 10
c = b > 9
c
# Type: c = boolean. Value: c = True.

# 1.6
5 / 2 == 5 / 2.0
# Type: True. Python doesn't care about float and int same answer.

# 2.1
3.0 - 1.0 != 5.0 - 3.0
# Value returned: False

# 2.2
3 > 4 or (2 < 3 and 9 > 10)
# Value returned: False

# 2.3
4 > 5 or 3 < 4 and 9 > 8
# Valure returned: True

# 2.4
not (4 > 3 and 100 > 6)
# Valure returned: False

# 3.1
import time
SECONDS_IN_A_DAY = 86400

t = time.localtime()
days = time.time() / SECONDS_IN_A_DAY
hours = t.tm_hour
minutes = t.tm_min
seconds = t.tm_sec

print(
    f"The time is {hours}:{minutes}:{seconds}. It has been {days:.0f} days since the epoch."
)
