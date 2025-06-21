import heapq

def merge_k_lists(lists):
    h = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(h, (lst[0], i, 0)) 

    while h:
        val, list_idx, element_idx = heapq.heappop(h)
        result.append(val)

        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(h, next_tuple)

    return result

def main():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)

if __name__ == "__main__":
    main()