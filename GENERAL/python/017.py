# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    new_list = list(set(arr))
    sorted_list = sorted(new_list)

    # find the index of runner-up
    runner_up = sorted_list[-2]
    print(runner_up)
    