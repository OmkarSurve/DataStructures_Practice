"""
Linear time approach to solve Stock Buy Sell Problem

Problem Statement: An array is given as Input where ith element is the price of a given stock on day.
You were permitted to complete unlimited transaction. Derive an algorithm to find the maximum profit in O(n) Time complexity and O(n) Space Complexity
Asked in :Amazon Microsoft Flipkart DE-Shaw

Algo: As we traverse through the array, we need to find local minima and maxima. We buy at local minima and sell at maxima to get max profit.

Local minima is element which is less than element at next index, and local maxima is if next element is less.
"""


def stock_transaction(arr):

    buy_flag = True
    sell_flag = False
    sum_profit = 0
    profit = 0

    for i in range(1, len(arr) - 1):    # [98, 178, 250, 300, 40, 540, 690]

        if arr[i-1] < arr[i]:
            if buy_flag == True:
                buy_price = arr[i-1]
                buy_flag = False
                sell_flag = True  # We set the sell flag true as soon as we buy the stock

        if arr[i] > arr[i+1]:
            if sell_flag == True:
                sell_price = arr[i]
                buy_flag = True  # We set the buy flag true as soon as we sell the stock
                sell_flag = False
                profit = sell_price - buy_price
                sum_profit += profit

    if sell_flag == True:
        profit = arr[len(arr) - 1] - buy_price
        sum_profit += profit

    return sum_profit


ar = [30, 70, 100, 12, 45, 311, 60]
print (stock_transaction(ar))



