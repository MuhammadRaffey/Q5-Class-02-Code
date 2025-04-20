Recursion in programming is a technique where a function calls itself directly or indirectly to solve a problem. It's often used to solve problems that can be broken down into smaller, similar subproblems. A classic example of recursion is computing the factorial of a number.

Here's a simple Python code example that demonstrates recursion by calculating the factorial of a number:

```python
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
print(f"The factorial of {number} is {factorial(number)}")
```

In this example, the `factorial` function calls itself with the argument `n-1` until it reaches the base case of `n` being 0 or 1. The base case is essential to prevent infinite recursion and to provide a stopping condition for the recursive calls.