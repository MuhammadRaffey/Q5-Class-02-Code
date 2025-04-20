Recursion in programming is a technique where a function calls itself directly or indirectly to solve a problem. It's often used to solve problems that can be broken down into smaller, similar subproblems.

Here's a simple example of recursion in Python: calculating the factorial of a number. The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It's denoted by n!.

```python
def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)
```

In this example, `factorial` is a recursive function. When you call `factorial(n)`, it calls itself with the argument `n-1`, and this process repeats until it reaches the base case, which is when `n` is 0. Then it starts to return the results up the call chain, calculating the final result.

For example, if you call `factorial(5)`, the function calls will look like this:

- `factorial(5)` calls `factorial(4)`
- `factorial(4)` calls `factorial(3)`
- `factorial(3)` calls `factorial(2)`
- `factorial(2)` calls `factorial(1)`
- `factorial(1)` calls `factorial(0)`

Then, `factorial(0)` returns 1 (base case), and each function call returns the result of `n * factorial(n-1)` up the chain, eventually returning `5! = 120`.