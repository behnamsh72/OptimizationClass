###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from aoptimization.ps1.ps1_partition import get_partitions
import time
from collections import OrderedDict


# ================================
# Part A: Transporting Space Cows
# ================================

# Problem first
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cows = {}
    file = open(filename, 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        count += 1
        data = line.split(',')
        cows[data[0]] = int(data[1])

    file.close()
    return cows


# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    first. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    result = []

    sortedCows = dict(sorted(cows.items(), key=lambda item: item[1], reverse=True))
    print(sortedCows)
    numTransport = 0
    while len(sortedCows) != 0:
        transport = []
        totalWeight = 0
        for item in sortedCows:
            if totalWeight + sortedCows[item] <= limit:
                transport.append(item)
                totalWeight += sortedCows[item]
        numTransport += 1
        for cowNames in transport:
            sortedCows.pop(cowNames)
        # print(numTransport)
        # print(transport)
        result.append(transport)

    return result


# Problem 3
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    first. Enumerate all possible ways that the cows can be divided into separate trips
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    trips = []
    cows_copy = cows.copy()
    cows_sorted = OrderedDict(sorted(cows_copy.items(), reverse=True, key=lambda x: x[1]))

    cow_partitions = get_partitions(cows_sorted)
    successful_score = 0
    allowable_trip = 0
    current_min_trips = None

    for trip_combo in cow_partitions:
        # print(trip_combo)
        allowable_trip = 0
        found_cows = []
        for item in trip_combo:
            trip_weight = 0
            successful_score = 0
            for cow in item:
                if trip_weight + cows_sorted[cow] <= limit and cow not in found_cows:
                    trip_weight = trip_weight + cows_sorted[cow]
                    successful_score += 1
                    found_cows.append(cow)
                else:
                    break
            if successful_score == len(item):
                allowable_trip += 1

        if allowable_trip == len(trip_combo):
            if trip_combo not in trips:
                trips.append(trip_combo)

    minLength = len(trips[0])
    minTrip = trips[0]

    for trip in trips:
        if len(trip) < minLength:
            minLength = len(trip)
            minTrip = trip

    return list(minTrip)


# Problem 4


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")

    print("\n---Greedy algorithm\n")

    start = time.time()
    print(greedy_cow_transport(cows))
    end = time.time()
    print(end - start, " seconds")
    print("\n---Brute force algorithm\n")
    print()
    start = time.time()
    print(brute_force_cow_transport(cows))
    end = time.time()
    print(end - start, "seconds")


if __name__ == "__main__":
    cows = load_cows('ps1_cow_data_2.txt')
    print(greedy_cow_transport(cows, 10))
    print(brute_force_cow_transport(cows, 10))
    print("\n\nCompare two methods:\n")
    compare_cow_transport_algorithms()
