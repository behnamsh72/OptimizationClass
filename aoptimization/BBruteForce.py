from aoptimization.AGreedyAlgorithm import Food
import random


def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weight
       Returns a tuple of the total value of a solution to the
         0/first knapsack problem and the items of that solution"""
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getCost() > avail:
        # Explore right branch only
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withVal, withToTake = maxVal(toConsider[1:],
                                     avail - nextItem.getCost())
        withVal += nextItem.getValue()
        # Explore right branch
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def testMaxVal(foods, maxUnits, printItems=True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(foods, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)


def buildMenu(names, values, calories):
    """names, values, calories lists of same length
        name  a list of strings
        values and calories list of numbers
        :returns list of Foods
    """
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu


def buildLargeMenu(numItems, maxVal, maxCost):
    items = []
    for i in range(numItems):
        items.append(Food(str(i), random.randint(1, maxVal), random.randint(1, maxCost)))

    return items


if __name__ == "__main__":
    ####for previous example in greedy algorithm
    # names = ['wine', 'beer', 'pizza', 'burger', 'fries',
    #          'cola', 'apple', 'donut', 'cake']
    # values = [89, 90, 95, 100, 90, 79, 50, 10]
    # calories = [123, 154, 258, 354, 365, 150, 95, 195]
    # foods = buildMenu(names, values, calories)
    # testMaxVal(foods, 750)

    # example with more items 
    for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60):
        items = buildLargeMenu(numItems, 90, 250)
        print("For numItems:", numItems)
        testMaxVal(items, 750, False)
