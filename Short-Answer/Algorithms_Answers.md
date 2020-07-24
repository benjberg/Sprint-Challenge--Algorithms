#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)   a = 0
    while (a < n * n * n):
      a = a + n * n

O(n) We have 1 loop that will execute until the condition (a = n) The means the runtime for this psuedocode will grow at the same rate as N. so while we have N=1 the loop runs once, n=2 loop runs twice ect.


b) sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

i believe its O(n). While i almost think it could be O(n^2), the first for loop doesnt actually do anything to the inputs, and instead just creates a variable while all the actual work is done in the while loop, making it so sum is only counted once for each input value making what i believe to be a 1:1 growth ratio.



c) def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

The runtime complexity of this code is again O(n). In recursion the function is called within itself. in this function we call the original input and then after running it calls iteself again minus 1 until it will reach 0. That means that this is invoked an equal number of times to the input put into the function giving it a 1:1 growth rate.


## Exercise II


Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


A binary search looks like it fits best for this type of issue as the number of cracked eggs is minimized since finding something by increment in the worst case senario requires guesses equal to the number of floors while using a biary search only takes a logrithmic amount of time and is much quicker. Since we do not know what floor the eggs break on we will need an exertnal function that I will call break that takes the floor into account, if the egg is broken it reaturns true else it returns false. 

first we would take the number of floors 'f' setting the min, max and mid. lets say we have 20 floors or f=20. we'd loop through the floors starting at mid (10) and checking the status of the egg. if the egg breaks then we move down half as many floors to 5 and drop the egg. if the egg is broken we go down again. if its not then we go up half as many floors and check the egg again. we repeat this process till we get to the floor that it wont break on. if as stated above that we dropped the egg at floor 10 and it didnt break then we'd go up half as many floors to 15 and repeat. each pass eliminates half as many possibilites as if we just started on the bottom or top and worked up/down 1 floor at a time.



runtime complexity is O(log n) as explained above