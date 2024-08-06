# problem 1 -1431. Kids With the Greatest Number of Candies
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
![image](https://github.com/user-attachments/assets/8249884d-af5d-42a3-8e58-bee6d97f785b)

# problem 2 ) lower case 
```java
class Solution {
    public String toLowerCase(String s) {
      return  s.toLowerCase();
    }
}
```
![image](https://github.com/user-attachments/assets/5208178f-f20c-4c72-8a6d-4d84668158d5)

