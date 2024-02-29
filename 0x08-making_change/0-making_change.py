#!/usr/bin/python3

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet a given amount total.
    """
    # If total is 0 or less, return 0
    if total <= 0:
        return 0

    # Initialize an array to store the fewest number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp[i] if using the current coin results in fewer coins needed
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, total cannot be met by any number of coins
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]


if __name__ == "__main__":
    # Test cases
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

