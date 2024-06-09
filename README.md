# CS3243 Introduction to Artificial Intelligence
## Project 2: Constraint Satisfaction Problems and Local Search

### Project 2.1: Constraint Satisfaction Problems (CSP)

#### Overview
In this project, I implemented a solver for a general constraint satisfaction problem (CSP) using the backtracking algorithm, along with optimizations such as forward checking.

#### Task: Backtracking Algorithm
The task was to find a set of variable assignments that satisfy all given constraints using the backtracking algorithm.

##### Functionality
- **Input:** A dictionary with keys `domains` and `constraints`.
  - `domains`: A dictionary where keys are variable names (str) and values are lists of integers representing the domain of each variable.
  - `constraints`: A dictionary where keys are tuples of variable names and values are lambda functions representing binary constraints.
- **Output:** A dictionary with variable assignments that satisfy all constraints, or `None` if no solution exists.

##### Example
**Input:**
```python
input = {
    'domains': {
        'A': [1, 2, 3, 4, 5],
        'B': [2, 3, 4, 5, 6],
        'C': [3, 4, 5, 6, 7],
        'D': [5, 7, 9, 11, 13]
    },
    'constraints': {
        ('A', 'B'): lambda a, b: a + b == 8 and a >= b,
        ('B', 'C'): lambda b, c: b <= c / 2,
        ('C', 'D'): lambda c, d: (c + d) % 2 == 0
    }
}
```

**Output:**

```python
output = {'A': 5, 'B': 3, 'C': 7, 'D': 5}
```

### Project 2.2: Local Search and Constraint Satisfaction Problems
#### Overview
In this project, I implemented local search and CSP algorithms to solve various tasks.

#### Task 1: Local Search
#### Description
I was tasked with scheduling performances for a music festival in a balanced manner using local search. The goal was to partition a list of values into subsets of equal size and sum.

#### Functionality
**Input:** A dictionary with keys count, size, and values.
**count:** Number of subsets required (int).
**size:** Required size of each subset (int).
**values:** List of integers to be partitioned.
**Output:** A list of subsets where each subset has the same sum and size.

#### Example
**Input:**

```python
{
    'count': 5,
    'size': 4,
    'values': [7, 8, 4, 13, 12, 19, 9, 6, 6, 1, 3, 13, 10, 14, 3, 19, 8, 10, 32, 3]
}
```
**Output:**

```python
[
    [6, 9, 12, 13],
    [6, 7, 8, 19],
    [3, 10, 13, 14],
    [3, 8, 10, 19],
    [32, 1, 4, 3]
]
```
#### Task 2: CSP
#### Description
I was tasked with dividing a concert hall into square regions for ushers and security personnel using a CSP solver.

#### Functionality
**Input:** A dictionary with keys rows, cols, input_squares, and obstacles.
rows: Number of rows in the target rectangle (int).
cols: Number of columns in the target rectangle (int).
input_squares: Dictionary where keys are side lengths of squares and values are the number of squares available.
obstacles: List of obstacle coordinates (tuple[int, int]).
Output: A list of tuples representing the arrangement of squares. Each tuple contains the size of the square and its top-left corner coordinates.
Example
Input:

``` python
{
    'rows': 4,
    'cols': 8,
    'input_squares': {
        1: 5,
        2: 2,
        4: 1
    },
    
    'obstacles': [(3, 0), (1, 2), (3, 7)]
}
```

**Output:**

``` python
[
    (2, 0, 0),
    (1, 0, 2),
    (4, 0, 3),
    (1, 0, 7),
    (1, 1, 7),
    (1, 2, 0),
    (2, 2, 1),
    (1, 2, 7)
]
```
