
def inventory_report_generator(inventory_data):
    """
    Generate inventory report aggregating stock and value by category.

    Args:
        inventory_data: List of dicts with keys: category, unit_cost, stock_count

    Returns:
        dict: Keys are categories, values are dicts with total_value and total_stock

    Raises:
        KeyError: If required keys are missing
        ValueError: If unit_cost or stock_count is negative
    """
    valid_keys = ["category", "unit_cost", "stock_count"]
    res = {}
    
    for data in inventory_data:
        if len(data) != 3:
            raise KeyError
        
        category = data["category"]
        cost = data["unit_cost"]
        stock_count = data["stock_count"]

        if cost < 0 or stock_count < 0:
            raise ValueError

        if category not in res:
            res[category] = {"total_value": cost * stock_count, "total_stock": stock_count}
        else:
            res[category]["total_value"] += cost * stock_count
            res[category]["total_stock"] += stock_count
    
    return res


def rainfall_analyzer(readings, threshold):
    """
    Analyze rainfall readings against a threshold.

    Args:
        readings: List of rainfall readings (mm)
        threshold: Maximum acceptable rainfall (mm)

    Prints:
        - "No rainfall data" if empty
        - "All readings within threshold" if all <= threshold
        - "Warning: X readings above Y" otherwise
        - "Average: X" (always when data exists, formatted to 2 decimals)
    """
    if not readings:
        print("No rainfall data")
    
    count = 0
    
    for reading in readings:
        if reading > threshold:
            count += 1
    
    if count > 0:
        print(f"Warning: {count} readings above {threshold}")
        print(f"Average: {(sum(readings) / len(readings)):.02f}")
    elif len(readings) != 0:
        print("All readings within threshold")
        print(f"Average: {(sum(readings) / len(readings)):.02f}")


def username_validator_with_retry(max_attempts):
    """
    Validate a username with limited retry attempts.

    Args:
        max_attempts: Maximum number of attempts allowed

    Behavior:
        - Prompt "Enter username:" for each attempt
        - Valid username requires: 5-15 chars, only letters, digits, or underscores,
          must start with a letter
        - Print "Invalid username. Try again." for invalid
        - Print "Username accepted!" when valid
        - Print "Maximum attempts reached. Access denied." if exhausted
    """
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username:")

        letters = any(char.isalpha() for char in username)
        digits = any(char.isdigit() for char in username)
        underscore = True if "_" in username else False
        length = 5 <= len(username) <= 15

        if letters and digits and username and length and underscore:
            print("Username accepted!")
            break
        else:
            print("Invalid username. Try again.")
            attempts += 1
    
    if attempts >= max_attempts:
        print("Maximum attempts reached. Access denied.")



def employee_performance_processor(employees):
    """
    Categorize employees by performance rating.

    Args:
        employees: List of dicts with keys: name, scores (list of ints 0-100)

    Returns:
        dict: Keys "high_performers" (avg >= 80) and "needs_improvement" (avg < 80),
              values are lists of dicts with name and average

    Raises:
        KeyError: If required keys are missing
        ValueError: If scores list is empty
    """
    res = {
        "high_performers": [],
        "needs_improvement": []
    }

    for employee in employees:
        if len(employee) != 2:
            raise KeyError
        
        name = employee["name"]
        scores = employee["scores"]

        if len(scores) > 0: 
            average = round(sum(scores) / len(scores), 2) 

        if len(scores) == 0:
            raise ValueError
        
        if average >= 80:
            res["high_performers"].append({"name": name, "average": average})
        else:
            res["needs_improvement"].append({"name": name, "average": average})
    
    return res

employee_performance_processor([
    {"name": "Alice", "scores": [90, 85, 88]},
    {"name": "Bob",   "scores": [70, 65, 75]},
])


def order_batcher(orders, batch_size):
    """
    Split orders into batches of specified size.

    Args:
        orders: List of orders
        batch_size: Number of orders per batch

    Returns:
        list: List of batches (each batch is a list)

    Raises:
        ValueError: If batch_size < 1
    """
    pass


def social_network_analyzer(network: dict[str, list[str]]):
    """
    Analyze a social network's follow relationships.

    Args:
        network: Dict where keys are users, values are lists of users they follow

    Returns:
        dict with keys:
            - total_follows (int): sum of all follow relationships
            - most_followed (str | None): user who appears most in others' follow lists
            - no_followers (list[str]): users that nobody follows
    """
    pass


def count_vowels(s):
    """
    Count vowels in a string using RECURSION.

    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.

    Args:
        s: A string

    Returns:
        int: Number of vowels (a, e, i, o, u — case-insensitive)

    Raises:
        TypeError: If s is not a string
    """
    pass


def text_pipeline_processor(raw_texts, transformations):
    """
    Apply a sequence of transformations to a list of strings.

    Args:
        raw_texts: List of strings
        transformations: List of transformation names

    Available transformations:
        - "uppercase": convert to uppercase
        - "strip": remove leading/trailing whitespace
        - "remove_empty": remove empty strings
        - "reverse": reverse each string

    Returns:
        list: Transformed data

    Raises:
        ValueError: For unknown transformations
    """
    pass


def score_ranker(scores):
    """
    Rank competitors by score with proper tie handling.

    Args:
        scores: List of tuples (competitor_name, score)

    Returns:
        list: List of tuples (competitor_name, score, rank) sorted by score descending.
              Tied competitors share the same rank; the next rank skips accordingly.

    Raises:
        ValueError: If any tuple doesn't have exactly 2 elements
    """
    pass


def fibonacci(n):
    """
    Return the nth Fibonacci number using RECURSION.

    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.

    Args:
        n: A non-negative integer

    Returns:
        int: The nth Fibonacci number

    Raises:
        ValueError: If n is negative or not an integer
    """
    pass