
def getMaxRequests(capacity,traffic, k):

    total_requests = 0
    gains_list = []

    for i in range(len(capacity)):

        curr_capacity = capacity[i]
        curr_traffic = traffic[i]

        capacity_handled = min(curr_capacity,curr_traffic)

        potential_handled = min(curr_capacity * 2, curr_traffic)

        total_requests += capacity_handled

        curr_gain = potential_handled - capacity_handled

        gains_list.append(curr_gain)

    
    gains_list.sort(reverse=True)

    for r in range(min(k, len(capacity))):

        total_requests += gains_list[r]

    return total_requests


if __name__ == "__main__":
    cap = [5, 3, 7, 10, 12]
    traffic = [3, 2, 5, 8, 10]
    k = 2
    print(f"Result: {getMaxRequests(cap, traffic, k)}")