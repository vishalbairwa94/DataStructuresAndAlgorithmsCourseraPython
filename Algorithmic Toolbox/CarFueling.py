# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    can_run = tank
    stops.insert(0, 0)
    stops.append(distance)
    stops_needed = 0
    distance_covered = 0

    for i in range(0, len(stops)):
        if stops[i] == stops[-1]:
            break

        if can_run >= stops[i+1] - stops[i]:
            can_run = can_run - (stops[i+1] - stops[i])
            distance_covered = stops[i+1]
            if stops[i+1] - stops[i] > can_run:
                stops_needed = stops_needed + 1
                can_run = can_run + tank
        else:
            return -1

    return stops_needed

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))