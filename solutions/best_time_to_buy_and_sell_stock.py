# Best Time to Buy and Sell Stock (LeetCode 121)
def max_profit(prices):
    min_price = float('inf')
    max_p = 0
    for p in prices:
        min_price = min(min_price, p)
        max_p = max(max_p, p - min_price)
    return max_p

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))  # 5
