from aoptimization.AGreedyAlgorithm import Food
import random


def dynamicMaxVal(toConsider, avail, memo={}):
    """Assumes toConsider a list of items, avail a weight
    and memo a dictionary with a tuple as key aoptimization value is the ramining items
    and second value is the ramining weight or avail weight
       Returns a tuple of the total value of a solution to the
         0/a knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = dynamicMaxVal(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        try:
            result = memo[(len(toConsider[1:]), avail - nextItem.getCost())]
        except KeyError:
            withVal, withToTake = dynamicMaxVal(toConsider[1:],
                                                avail - nextItem.getCost(), memo)
            withVal += nextItem.getValue()
            # Explore right branch
            withoutVal, withoutToTake = dynamicMaxVal(toConsider[1:], avail, memo)
            # Choose better branch
            if withVal > withoutVal:
                result = (withVal, withToTake + (nextItem,))
                memo[(len(toConsider[1:]), avail - nextItem.getCost())] = result
            else:
                result = (withoutVal, withoutToTake)
                memo[(len(toConsider[1:]), avail)] = result

    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = dynamicMaxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        sum = 0
        for item in taken:
            sum += item.getCost()
            print('   ', item)
        print("sum colories=", sum)


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))

    return items


# def buildMenu(names, values, calories):
#     """names, values, calories lists of same length
#         name  a list of strings
#         values and calories list of numbers
#         :returns list of Foods
#     """
#     menu = []
#     for i in range(len(values)):
#         menu.append(Food(names[i], values[i], calories[i]))
#
#     return menu


if __name__ == "__main__":
    # simple test
    ####for previous example in greedy algorithm
    # names = ['wine', 'beer', 'pizza', 'burger', 'fries',
    #          'cola', 'apple', 'donut', 'cake']
    # values = [89, 90, 95, 100, 90, 79, 50, 10]
    # calories = [123, 154, 258, 354, 365, 150, 95, 195]
    # foods = buildMenu(names, values, calories)
    # testMaxVal(foods, 750)

    for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
        items = buildLargeMenu(numItems, 90, 250)
        print("For numItems:", numItems)
        testMaxVal(items, 750, True)
