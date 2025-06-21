import heapq


def get_total_cost(nums):
    heapq.heapify(nums)
    total_cost = 0

    while len(nums) > 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        cost = a+b
        total_cost += cost
        heapq.heappush(nums, cost)

    return total_cost;


def main():
    nums = [4, 3, 5, 1, 7, 6, 2]
    result = get_total_cost(nums)
    print(result)


if __name__ == "__main__":
    main()