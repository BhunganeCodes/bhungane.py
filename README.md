# final-500 - Python Comprehensive Assessment (All Concepts)

# Learning Outcomes assessed:

- **Data Structures:** Lists, dictionaries, tuples, sets, nested structures
- **Loops & Iteration:** for loops, while loops, list comprehensions
- **Functions:** Parameters, return values, validation
- **Conditionals:** if/elif/else, boolean logic, comparisons
- **String Manipulation:** Methods, formatting, validation
- **Mathematical Operations:** Calculations, aggregations, averages
- **Recursion:** Base cases, recursive calls
- **Error Handling:** try/except, raising exceptions
- **Input/Output:** print statements, input validation
- **Algorithms:** Sorting, filtering, batching, caching (LRU)
- **Object-Oriented Concepts:** Class-based cache implementation

---

# Assessment Structure

This is a comprehensive coding assessment with 10 challenging questions that integrate multiple concepts.

## Scoring & Weighting

Your coding score is determined by the number of tests you pass.

Let:
- T = total number of coding tests
- P = number of tests you pass

```bash
Coding Score = (P / T) × 100%
```

### Pass Mark

To pass the overall assessment, your score must be **60% (Minimum Pass Mark) or higher**.

---

## How to run your tests

To run all your tests:

```bash
python3 -m pytest test_final_assessment.py -v
```

To run your tests individually:

```bash
python3 -m pytest test_final_assessment.py::test_sales_report_generator_logic -v
```

---

# Final Comprehensive Assessment

This assessment combines concepts from all previous units into real-world, integrated challenges.

## Project Structure

```
final-assessment/
├── final_assessment.py          # <-- This is where you write your solutions
├── test_final_assessment.py     # <-- These are the tests you must make pass
└── README.md                     # <-- Assessment instructions (this file) 
```

---

## Question 1 - `sales_report_generator(sales_data)` 
**Concepts:** Dictionaries, Lists, Aggregation, Validation

**User Story:**
*As an e-commerce analytics manager, I need to generate sales reports that aggregate revenue and unit sales by product, combining data from multiple transactions throughout the day to understand which products are performing best.*

**Requirements:**
- Accept a list of sale dictionaries with keys: `product`, `price`, `quantity`
- Return a dictionary where:
  - Keys are product names
  - Values are dicts with `total_revenue` (price × quantity summed) and `units_sold` (quantity summed)
- Handle multiple sales of the same product by aggregating
- Raise `KeyError` if required keys are missing
- Raise `ValueError` if price or quantity is negative

**Example:**
```python
sales_report_generator([
    {"product": "Laptop", "price": 1000, "quantity": 2},
    {"product": "Mouse", "price": 25, "quantity": 5},
    {"product": "Laptop", "price": 1000, "quantity": 1}
])
# Returns: {
#     "Laptop": {"total_revenue": 3000, "units_sold": 3},
#     "Mouse": {"total_revenue": 125, "units_sold": 5}
# }
```

---

## Question 2 - `temperature_analyzer(temperatures, threshold)`
**Concepts:** Lists, Conditionals, Math, Print Statements, Loops

**User Story:**
*As a climate researcher monitoring weather station data, I need to analyze temperature readings, identify how many fall below a critical threshold, and calculate the average temperature for my daily report.*

**Requirements:**
- Accept a list of temperature readings and a threshold value
- Print different messages based on conditions:
  - If empty list: "No temperature data"
  - If all temps ≥ threshold: "All temperatures above threshold"
  - Otherwise: "Warning: X readings below Y" (X = count, Y = threshold)
- Always print the average temperature: "Average: X" (formatted to 2 decimals)
- Handle empty lists gracefully

**Example:**
```python
temperature_analyzer([15, 25, 18, 30], 20)
# Output:
# Warning: 2 readings below 20
# Average: 22.00

temperature_analyzer([25, 30, 28], 20)
# Output:
# All temperatures above threshold
# Average: 27.67
```

---

## Question 3 - `password_validator_with_retry(max_attempts)`
**Concepts:** While Loops, Input Validation, String Methods, Counters

**User Story:**
*As a security engineer building an account creation system, I need to enforce strong password requirements with a limited number of attempts, prompting users until they create a valid password or exhaust their attempts.*

**Requirements:**
- Accept maximum number of attempts
- Continuously prompt "Enter password:" until valid password or max attempts reached
- Valid password must have:
  - At least 8 characters
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least one special character from: `!@#$%^&*`
- Print "Invalid password. Try again." for invalid attempts
- Print "Password accepted!" when valid
- Print "Maximum attempts reached. Account locked." if attempts exhausted

**Example:**
```python
password_validator_with_retry(3)
# User: weak
# Output: Invalid password. Try again.
# User: Better123
# Output: Invalid password. Try again.
# User: Secure@123
# Output: Password accepted!
```

---

## Question 4 - `student_grade_processor(students)`
**Concepts:** Nested Dictionaries, Lists, Math, Conditionals, Validation

**User Story:**
*As an academic coordinator processing end-of-term results, I need to categorize students into passing (≥60% average) and failing (<60% average) groups with their calculated averages for intervention planning.*

**Requirements:**
- Accept a list of student dicts with keys: `name`, `grades` (list of scores)
- Return a dictionary with two keys:
  - `passing`: list of dicts with `name` and `average` (≥60)
  - `failing`: list of dicts with `name` and `average` (<60)
- Calculate average to 2 decimal places
- Raise `KeyError` if required keys missing
- Raise `ValueError` if grades list is empty

**Example:**
```python
student_grade_processor([
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [55, 60, 58]}
])
# Returns: {
#     "passing": [{"name": "Alice", "average": 87.67}],
#     "failing": [{"name": "Bob", "average": 57.67}]
# }
```

---

## Question 5 - `transaction_batcher(transactions, batch_size)`
**Concepts:** List Slicing, Pagination, Validation

**User Story:**
*As a payment gateway engineer processing bulk transactions, I need to split large transaction lists into smaller batches for API rate limiting, ensuring no transaction is lost and batches don't exceed size limits.*

**Requirements:**
- Accept a list of transactions and batch size
- Return a list of batches (each batch is a list)
- Last batch may have fewer items than batch_size
- Preserve order of transactions
- Raise `ValueError` if batch_size < 1
- Return empty list for empty input

**Example:**
```python
transaction_batcher(["T1", "T2", "T3", "T4", "T5"], 2)
# Returns: [["T1", "T2"], ["T3", "T4"], ["T5"]]
```

---

## Question 6 - `network_graph_analyzer(network)`
**Concepts:** Dictionaries, Graph Theory, Aggregation, Max Finding

**User Story:**
*As a network administrator analyzing server connectivity, I need to identify the total number of connections, which server has the most connections, and which servers are isolated (no outgoing connections) for infrastructure optimization.*

**Requirements:**
- Accept a dictionary representing a network (adjacency list)
- Return a dictionary with three keys:
  - `total_connections`: sum of all outgoing connections
  - `most_connected`: name of node with most connections (or None if empty)
  - `isolated_nodes`: list of nodes with zero connections
- Handle ties by returning any node with max connections

**Example:**
```python
network_graph_analyzer({"A": ["B", "C"], "B": ["A"], "C": []})
# Returns: {
#     "total_connections": 3,
#     "most_connected": "A",
#     "isolated_nodes": ["C"]
# }
```

---

## Question 7 - `sum_of_digits(n)` **[MUST USE RECURSION]**
**Concepts:** Recursion, Mathematical Operations, Validation

**User Story:**
*As a mathematics education app developer teaching number theory, I need to recursively calculate the sum of digits in a number to demonstrate the elegance of recursive problem decomposition to students.*

**Requirements:**
- Accept a non-negative integer
- Return the sum of all digits
- **MUST use recursion** (tests verify this)
- Base case: single digit returns itself
- Recursive case: last digit + sum_of_digits(remaining digits)
- Raise `ValueError` for negative numbers or non-integers

**Example:**
```python
sum_of_digits(123)   # Returns: 6 (1 + 2 + 3)
sum_of_digits(9)     # Returns: 9
sum_of_digits(1234)  # Returns: 10 (1 + 2 + 3 + 4)
```

**Algorithm:**
```
sum_of_digits(123):
  = 3 + sum_of_digits(12)
  = 3 + (2 + sum_of_digits(1))
  = 3 + (2 + 1)
  = 6
```

---

## Question 8 - `data_pipeline_processor(raw_data, transformations)`
**Concepts:** Lists, Functions, Conditionals, Filtering, Mapping

**User Story:**
*As a data engineer building an ETL pipeline, I need to apply a sequence of transformations to raw data (doubling values, filtering, adding constants) to prepare datasets for machine learning models.*

**Requirements:**
- Accept a list of numbers and a list of transformation names
- Apply transformations in order
- Available transformations:
  - `"double"`: multiply each number by 2
  - `"add_ten"`: add 10 to each number
  - `"filter_even"`: keep only even numbers
  - `"square"`: square each number
- Raise `ValueError` for unknown transformations
- Return transformed list

**Example:**
```python
data_pipeline_processor([1, 2, 3, 4], ["double", "filter_even"])
# [1, 2, 3, 4] -> [2, 4, 6, 8] -> [2, 4, 6, 8]
# Returns: [2, 4, 6, 8]

data_pipeline_processor([1, 2, 3], ["double", "add_ten"])
# [1, 2, 3] -> [2, 4, 6] -> [12, 14, 16]
# Returns: [12, 14, 16]
```

---

## Question 9 - `leaderboard_ranker(scores)`
**Concepts:** Tuples, Sorting, Lists, Ranking Algorithm

**User Story:**
*As a competitive gaming platform developer, I need to rank players by score (highest first) and assign ranks, handling tied scores correctly where tied players share the same rank.*

**Requirements:**
- Accept a list of tuples: `(player_name, score)`
- Return a list of tuples: `(player_name, score, rank)`
- Sort by score descending (highest first)
- Handle ties: tied players get same rank, next rank skips
  - Example: scores [100, 100, 90] → ranks [1, 1, 3] (not [1, 1, 2])
- Raise `ValueError` if tuple doesn't have exactly 2 elements

**Example:**
```python
leaderboard_ranker([("Alice", 100), ("Bob", 150), ("Charlie", 120)])
# Returns: [("Bob", 150, 1), ("Charlie", 120, 2), ("Alice", 100, 3)]

leaderboard_ranker([("A", 100), ("B", 100), ("C", 90)])
# Returns: [("A", 100, 1), ("B", 100, 1), ("C", 90, 3)]
```

---

## Question 10 - `smart_cache_system(capacity)` **[CLASS-BASED]**
**Concepts:** Classes, Objects, LRU Algorithm, Dictionaries

**User Story:**
*As a backend developer optimizing API response times, I need to implement an LRU (Least Recently Used) cache that stores frequently accessed data and automatically evicts the least recently used items when capacity is reached.*

**Requirements:**
- Return a cache object with methods: `put(key, value)` and `get(key)`
- Maximum capacity (number of items)
- When capacity is full and new item added, evict least recently used item
- `get(key)` marks key as recently used
- `put(key, value)` updates existing keys without affecting capacity
- `get(key)` returns `None` if key not found
- Raise `ValueError` if capacity < 1

**Example:**
```python
cache = smart_cache_system(2)
cache.put("a", 1)
cache.put("b", 2)
cache.get("a")      # Returns: 1 (marks "a" as recently used)
cache.put("c", 3)   # Evicts "b" (least recently used)
cache.get("b")      # Returns: None
cache.get("c")      # Returns: 3
```

**LRU Logic:**
- Items are ordered by access time
- `get()` and `put()` update access time
- When full, remove item with oldest access time

---

# Your Goal

Complete all functions in `final_assessment.py` so that:
- The code is valid Python
- Each function behaves according to requirements
- All unit tests pass successfully
- Question 7 **MUST** use recursion
- Question 10 **MUST** use a class

## Tips for Success

1. **Read user stories** - understand the business context
2. **Plan before coding** - think through the algorithm
3. **Test incrementally** - one function at a time
4. **Validate inputs** - check types, ranges, required keys
5. **Handle edge cases** - empty lists, ties, boundary values
6. **Use appropriate data structures** - dicts for grouping, lists for ordering
7. **For recursion (Q7)** - define base case first, then recursive case
8. **For LRU cache (Q10)** - consider using OrderedDict or track access order

## Common Pitfalls to Avoid

- ❌ Not aggregating duplicate products (Q1)
- ❌ Forgetting to format averages to 2 decimals (Q2, Q4)
- ❌ Not counting attempts correctly (Q3)
- ❌ Not handling tied scores properly in ranking (Q9)
- ❌ Using loops instead of recursion (Q7)
- ❌ Not implementing LRU eviction correctly (Q10)

## Concept Integration Map

| Question | Data Structures | Loops | Math | Validation | Recursion | Classes |
|----------|----------------|-------|------|------------|-----------|---------|
| Q1 | ✅ Nested dicts | ✅ | ✅ | ✅ | | |
| Q2 | ✅ Lists | ✅ | ✅ | | | |
| Q3 | | ✅ While | | ✅ | | |
| Q4 | ✅ Nested | ✅ | ✅ | ✅ | | |
| Q5 | ✅ Lists | ✅ | | ✅ | | |
| Q6 | ✅ Dicts | ✅ | | | | |
| Q7 | | | ✅ | ✅ | ✅ | |
| Q8 | ✅ Lists | ✅ | | ✅ | | |
| Q9 | ✅ Tuples/Lists | ✅ | | ✅ | | |
| Q10 | ✅ Dicts | | | ✅ | | ✅ |

Good luck! 🚀