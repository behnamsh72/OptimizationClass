def get_data(aTouple):
    nums = ()
    words = ()
    for t in aTouple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)


test = ((1, "a"), (2, "b"), (1, "a"), (7, "b"))

(a, b, c) = get_data(test)
print('a:', a, ' b: ', b, ' c:', c)

f = [1, 2, 3]
my_set = {1, 2, 3, 4, 5, 6}
l = [1, 23, 5, 7, 9, 10]
print(len(l))
l.append(11)


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return "<" + str(self.x) + " , " + str(self.y) + ">"

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y


c = Coordinate(3, 4)
print(c.x)
origin = Coordinate(6, 9)
print(origin.y)
print(c.distance(origin))
print(c)
print(type(c))
c.__add__(origin)
print(c)

print(c.__eq__(c))