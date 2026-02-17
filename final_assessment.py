# final_assessment.py
# Complete the following functions to make all tests pass


def sales_report_generator(sales_data):
    """
    Generate sales report aggregating revenue and units by product.
    
    Args:
        sales_data: List of dicts with keys: product, price, quantity
        
    Returns:
        dict: Keys are products, values are dicts with total_revenue and units_sold
        
    Raises:
        KeyError: If required keys are missing
        ValueError: If price or quantity is negative
    """
    res = {}
    
    for data in sales_data:
        if list(data.keys()) != ["product", "price", "quantity"]:
            raise KeyError
        
        prod = data["product"]
        price = data["price"]
        quantity = data["quantity"]

        if price < 0 or quantity < 0:
            raise ValueError

        if prod not in res:
            res[prod] = {"total_revenue": 0,
                         "units_sold": 0}
            
        res[prod]["total_revenue"] += price * quantity
        res[prod]["units_sold"] += quantity
    
    return res


def temperature_analyzer(temperatures, threshold):
    """
    Analyze temperature readings against a threshold.
    
    Args:
        temperatures: List of temperature readings
        threshold: Minimum acceptable temperature
        
    Prints:
        - "No temperature data" if empty
        - "All temperatures above threshold" if all >= threshold
        - "Warning: X readings below Y" otherwise
        - "Average: X" (always, formatted to 2 decimals)
    """
    count = 0

    for temp in temperatures:
        if temp < threshold:
            count += 1
    
    if not temperatures:
        print("No temperature data")
    
    if len(temperatures) == 0:
        pass
    elif count > 0:
        print(f"Warning: {count} readings below {threshold}")
        print(f"Average: {sum(temperatures) / len(temperatures):.2f}")
    elif count == 0:
        print(f"All temperatures above threshold")
        print(f"Average: {sum(temperatures) / len(temperatures):.2f}")


def password_validator_with_retry(max_attempts):
    """
    Validate password with limited retry attempts.
    
    Args:
        max_attempts: Maximum number of attempts allowed
        
    Behavior:
        - Prompt "Enter password:" for each attempt
        - Valid password requires: 8+ chars, upper, lower, digit, special (!@#$%^&*)
        - Print "Invalid password. Try again." for invalid
        - Print "Password accepted!" when valid
        - Print "Maximum attempts reached. Account locked." if exhausted
    """
    import re
    attempts = 1

    while attempts <= max_attempts:
        password = input("Enter password:")

        if re.search(r"^[a-zA-Z0-9!@#$%\^&*]{8,}$", password):
            print("Password accepted!")
            break
        else:
            print("Invalid password. Try again.")
            attempts += 1
    
    if attempts > max_attempts:
        print("Maximum attempts reached. Account locked.")


def student_grade_processor(students):
    """
    Categorize students by passing/failing status with averages.
    
    Args:
        students: List of dicts with keys: name, grades (list)
        
    Returns:
        dict: Keys "passing" and "failing", values are lists of dicts with name and average
        
    Raises:
        KeyError: If required keys missing
        ValueError: If grades list is empty
    """
    res = {"passing": [], "failing": []}

    for s in students:
        if set(s.keys()) != {"name", "grades"}:
            raise KeyError
        
        grades = s["grades"]
        name = s["name"]

        if not grades:
            raise ValueError
        
        average = float(sum(grades) / len(grades))
        average = round(average, 2)

        if average < 60:
            res["failing"].append({"name": name, "average": average})

        else:
            res["passing"].append({"name": name, "average": average})

    return res


def transaction_batcher(transactions, batch_size):
    """
    Split transactions into batches of specified size.
    
    Args:
        transactions: List of transactions
        batch_size: Number of transactions per batch
        
    Returns:
        list: List of batches (each batch is a list)
        
    Raises:
        ValueError: If batch_size < 1
    """
    res = []

    if batch_size < 1:
        raise ValueError

    for t in range(0, len(transactions), batch_size):
        res.append(transactions[t:t+batch_size])
    
    return res


def network_graph_analyzer(network: dict[str, list[str]]):
    """
    Analyze network connectivity statistics.
    
    Args:
        network: Dict where keys are nodes, values are lists of connected nodes
        
    Returns:
        dict: Keys are total_connections, most_connected, isolated_nodes
    """
    count = 0
    longest_len = 0
    isolated = []

    res = {
    "total_connections": 0,
    "most_connected": None,
    "isolated_nodes": []
}
    count_dict = {}


    for k, v in network.items():
        if len(v) > longest_len:
            longest_len = len(v)
        
        if len(v) == 0:
            res["isolated_nodes"].append(k)

        if k in count_dict:
            count_dict[k] += len(v)
        else:
            count_dict[k] = len(v)

    for k, v in count_dict.items():
        count += v
        if v == longest_len:
            res["most_connected"] = k

    res["total_connections"] = count
    res["isolated_nodes"].extend(isolated)

    return res
    


def sum_of_digits(n):
    """
    Calculate sum of digits using RECURSION.
    
    IMPORTANT: You MUST use recursion. Iterative solutions will fail tests.
    
    Args:
        n: A non-negative integer
        
    Returns:
        int: Sum of all digits
        
    Raises:
        ValueError: If n is negative or not an integer
    """
    
    if n < 0 or not isinstance(n, int):
        raise ValueError
    if n < 10:
        return n
    else:
        return (n % 10) + sum_of_digits(n // 10) 


def data_pipeline_processor(raw_data, transformations):
    """
    Apply sequence of transformations to data.
    
    Args:
        raw_data: List of numbers
        transformations: List of transformation names
        
    Available transformations:
        - "double": multiply by 2
        - "add_ten": add 10
        - "filter_even": keep only even numbers
        - "square": square each number
        
    Returns:
        list: Transformed data
        
    Raises:
        ValueError: For unknown transformations
    """

    trans = ["double", "add_ten", "filter_even", "square"]

    for t in transformations:
        if t not in trans:
            raise ValueError
        
    for t in transformations:
        if t == "double":
            raw_data = [data * 2 for data in raw_data]
        if t == "filter_even":
            raw_data = [data for data in raw_data if data % 2 == 0]
        if t == "add_ten":
            raw_data = [data + 10 for data in raw_data]
        if t == "square":
            raw_data = [data ** 2 for data in raw_data]
    
    return raw_data


def leaderboard_ranker(scores):
    """
    Rank players by score with proper tie handling.
    
    Args:
        scores: List of tuples (player_name, score)
        
    Returns:
        list: List of tuples (player_name, score, rank) sorted by score descending
        
    Raises:
        ValueError: If tuple doesn't have exactly 2 elements
    """
    # TODO: Implement this function
    # Sort by score descending
    # Handle ties: same score = same rank, next rank skips
    pass


def smart_cache_system(capacity):
    """
    Create an LRU (Least Recently Used) cache system.
    
    IMPORTANT: You MUST implement this using a class.
    
    Args:
        capacity: Maximum number of items in cache
        
    Returns:
        Cache object with methods:
            - put(key, value): Add/update item
            - get(key): Retrieve item (returns None if not found)
        
    Raises:
        ValueError: If capacity < 1
        
    LRU Behavior:
        - When full, evict least recently used item
        - get() and put() mark items as recently used
    """
    # TODO: Implement this using a class
    # Hint: Use OrderedDict or track access order manually
    
    class LRUCache:
        def __init__(self, capacity):
            # TODO: Initialize cache
            pass
        
        def get(self, key):
            # TODO: Get value and mark as recently used
            pass
        
        def put(self, key, value):
            # TODO: Add/update value, evict if necessary
            pass
    
    # Validate capacity
    if capacity < 1:
        raise ValueError("Capacity must be at least 1")
    
    return LRUCache(capacity)