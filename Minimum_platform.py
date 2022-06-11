"""
Minimum number of Railway platforms required: Greedy Techniques to find minimum number of platforms
List of arrival and departure time is given, Find the minimum number of platforms are required for the railway as no train waits
The arrival array is already sorted, we also sort the departure array.
Then we compare arrival times and departure times and according add or subtract platform required.
"""


def minimumNumberPlatform(arrival, departure, n):

    arrival.sort()
    departure.sort()

    plat_needed = 1
    minplatform = 1
    i = 1
    j = 0

    while (i < n and j < n):

        if (arrival[i] <= departure[j]):

            plat_needed += 1
            i += 1

            if (plat_needed > minplatform):
                minplatform = plat_needed

        elif (arrival[i] > departure[j]):

            plat_needed -= 1
            j += 1

    return minplatform

arrival = [100, 140, 150, 200, 215, 400]
departure = [110, 300, 220, 230, 315, 600]
n = len(arrival)

print("Minimum Number Platforms = ",
      minimumNumberPlatform(arrival, departure, n))

