
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
    res = {}

    for item in inventory_data:
        category = item["category"]
        cost = item["unit_cost"]
        stock = item["stock_count"]

        if stock < 0 or cost < 0:
            raise ValueError

        if category not in res:
            res[category] = {"total_value": cost * stock, "total_stock": stock}
        else:
            res[category]["total_value"] += cost * stock
            res[category]["total_stock"] += stock
    
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
    count = 0

    if not readings:
        print("No rainfall data")

    if len(readings) > 0:
        average = (sum(readings) / len(readings))

        for data in readings:
            if data > threshold:
                count += 1
        
        if count == 0:
            print("All readings within threshold")
            print(f"Average: {average:.02f}")

        if count > 0:
            print(f"Warning: {count} readings above {threshold}")
            print(f"Average: {average:.02f}")


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

        if letters and digits and underscore:
            print("Username accepted!")
            break
        else:
            print("Invalid username. Try again.")
            attempts += 1
    
    if attempts == max_attempts:
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

    for item in employees:
        if len(item) != 2:
            raise KeyError
        
        name = item["name"]
        scores = item["scores"]

        if len(scores) == 0:
            raise ValueError
        
        average = round(sum(scores)/ len(scores), 2)

        if average >= 80:
            res["high_performers"].append({"name": name, "average": average})
        else:
            res["needs_improvement"].append({"name": name, "average": average})

    return res


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
    if batch_size < 1:
        raise ValueError
    
    res = []

    for i in range(0, len(orders), batch_size):
        res.append(orders[i:i+batch_size])
    
    return res


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
    
    res = {
        "total_follows": 0,
        "most_followed": None,
        "no_followers": []
    }

    follow_tracker = {}

    for key, value in network.items():
        print(f"Key: {key}")
        print(f"Value: {value}")
        res["total_follows"] += len(value)

        for item in value:
            if item not in follow_tracker:
                follow_tracker[item] = 1
            else:
                follow_tracker[item] += 1
    
    if follow_tracker:
        res["most_followed"] = max(follow_tracker, key=lambda k: follow_tracker[k])
    
    res["no_followers"] = [user for user in network if user not in follow_tracker]
        
    return res
    

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
    vowels = "aeiouAEIOU"

    if not isinstance(s, str):
        raise TypeError
    
    if not s:
        return 0
    
    if s[0] in vowels:
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])
    

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
    allowed_trans = ["uppercase", "strip", "remove_empty", "reverse"]

    for t in transformations:
        if t not in allowed_trans:
            raise ValueError
        
        for idx, text in enumerate(raw_texts):
            if t == "uppercase":
                raw_texts[idx] = raw_texts[idx].upper()
            if t == "strip":
                raw_texts[idx] = raw_texts[idx].strip()
            if t == "remove_empty":
                raw_texts[idx] = raw_texts[idx].replace(" ", "")
            if t == "reverse":
                raw_texts[idx] = raw_texts[idx][::-1]

    for text in raw_texts:
        if text == "":           
            raw_texts.remove(text)

    return raw_texts


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
    res = []
    
    for score in scores:
        if len(score) != 2:
            raise ValueError
    
    ranked = sorted(scores, key=lambda s: s[1], reverse=True)
    
    rank = 1

    for idx, (name, score) in enumerate(ranked):
        
        if idx > 0 and score == ranked[idx - 1][1]:
            res.append((name, score, res[-1][2]))
        else:
            rank = idx + 1 
            res.append((name, score, rank))
    
    return res


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
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)