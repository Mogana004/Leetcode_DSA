# [problem- 1](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75)
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.


Example 

 candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 

## soluntion 
```java
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int maxCandies = 0;

        // Find the maximum number of candies any child currently has
        for (int candy : candies) {
            if (candy > maxCandies) {
                maxCandies = candy;
            }
        }

        // Determine if each child can have the greatest number of candies
        for (int candy : candies) {
            if (candy + extraCandies >= maxCandies) {
                result.add(true);
            } else {
                result.add(false);
            }
        }

        return result;
    }
}
```



# [Problem- 2](https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75)
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
## solution
```java
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int length = flowerbed.length;
        
        for (int i = 0; i < length; i++) {
            if (flowerbed[i] == 0) {
                // Check if the previous plot and the next plot are empty or out of bounds
                boolean emptyPrev = (i == 0) || (flowerbed[i - 1] == 0);
                boolean emptyNext = (i == length - 1) || (flowerbed[i + 1] == 0);
                
                if (emptyPrev && emptyNext) {
                    flowerbed[i] = 1; // Plant a flower here
                    count++;
                    if (count >= n) {
                        return true; // Early exit if we have planted enough flowers
                    }
                }
            }
        }
        
        return count >= n;
    }
}
```

# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.




 Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


```java
class Solution {
    public int maxProfit(int[] prices) {
        // Edge case: If the array is empty or has only one element
        if (prices == null || prices.length < 2) {
            return 0;
        }

        int maxProfit = 0; // Initialize maxProfit to 0
        int minPrice = prices[0]; // Start with the first price as the minimum price

        for (int i = 1; i < prices.length; i++) {
            // Calculate the current profit if we sell at prices[i]
            int currentProfit = prices[i] - minPrice;
            
            // Update maxProfit if the currentProfit is greater
            maxProfit = Math.max(maxProfit, currentProfit);
            
            // Update minPrice to be the lowest price seen so far
            minPrice = Math.min(minPrice, prices[i]);
        }

        return maxProfit;
    }
}
```
