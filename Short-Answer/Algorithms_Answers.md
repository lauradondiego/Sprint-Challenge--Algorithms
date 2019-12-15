#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)O(n) => you are only running one while loop, which makes this O(n). "a" will always be less than "n"

b)O(n) XXX
line 17 = O(n) (order of)
no matter what n is, line 18 will always run
line 18 = O(1)
line 19 = log(n) j ran half as many times as n

- Correct Answer: O(n)log(n)

* you can ignore the lowest orders like O(1)

c)O(n)

## Exercise II

I would first create a variable called "stories" and set it to "n".
stories = n
I would create an if statement to check if f less than n, then return "not broken" and if f is greater than n, return "broken" and find the highest floor you can drop eggs at where they won't break.

- correct answer
- go to the middle floor and see if the egg breaks. if it does, eliminate everything above that floor. (split the array and only look at the left half 0-midpoint) then cut that new array in half and see if the egg breaks there. if so, repeat. split and test again. (Look up binary sort) (divide & conquer approach)
