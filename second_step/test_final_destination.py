import pytest
from final_destination import *
from unittest.mock import patch
from io import StringIO
import sys


# ──────────────────────────────────────────────────────────────────────────────
# Question 1 – Inventory Report Generator
# ──────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("inventory_data, expected", [
    (
        [
            {"category": "Electronics", "unit_cost": 200, "stock_count": 5},
            {"category": "Books",       "unit_cost": 15,  "stock_count": 10},
            {"category": "Electronics", "unit_cost": 200, "stock_count": 3},
        ],
        {
            "Electronics": {"total_value": 1600, "total_stock": 8},
            "Books":        {"total_value": 150,  "total_stock": 10},
        },
    ),
    ([], {}),
    (
        [{"category": "Furniture", "unit_cost": 500, "stock_count": 4}],
        {"Furniture": {"total_value": 2000, "total_stock": 4}},
    ),
])
def test_inventory_report_generator_logic(inventory_data, expected):
    assert inventory_report_generator(inventory_data) == expected


def test_inventory_report_generator_missing_keys():
    with pytest.raises(KeyError):
        inventory_report_generator([{"category": "Test", "unit_cost": 10}])


def test_inventory_report_generator_negative_unit_cost():
    with pytest.raises(ValueError):
        inventory_report_generator([{"category": "Test", "unit_cost": -5, "stock_count": 3}])


def test_inventory_report_generator_negative_stock():
    with pytest.raises(ValueError):
        inventory_report_generator([{"category": "Test", "unit_cost": 10, "stock_count": -1}])


def test_inventory_report_generator_large_dataset():
    data = [{"category": f"Cat_{i % 50}", "unit_cost": 10, "stock_count": 1} for i in range(5000)]
    result = inventory_report_generator(data)
    assert len(result) == 50
    assert result["Cat_0"]["total_stock"] == 100


def test_inventory_report_generator_duplicate_categories():
    data = [
        {"category": "Gadget", "unit_cost": 100, "stock_count": 2},
        {"category": "Gadget", "unit_cost": 100, "stock_count": 4},
    ]
    assert inventory_report_generator(data) == {
        "Gadget": {"total_value": 600, "total_stock": 6}
    }


# ──────────────────────────────────────────────────────────────────────────────
# Question 2 – Rainfall Analyzer
# ──────────────────────────────────────────────────────────────────────────────

def _capture(fn, *args):
    buf = StringIO()
    sys.stdout = buf
    fn(*args)
    sys.stdout = sys.__stdout__
    return buf.getvalue()


def test_rainfall_analyzer_all_within_threshold():
    out = _capture(rainfall_analyzer, [10, 15, 8, 12], 20)
    assert "All readings within threshold" in out
    assert "Average: 11.25" in out


def test_rainfall_analyzer_some_above_threshold():
    out = _capture(rainfall_analyzer, [5, 25, 8, 30], 20)
    assert "Warning: 2 readings above 20" in out
    assert "Average: 17.00" in out


def test_rainfall_analyzer_all_above_threshold():
    out = _capture(rainfall_analyzer, [50, 60, 70], 20)
    assert "Warning: 3 readings above 20" in out


def test_rainfall_analyzer_empty_list():
    out = _capture(rainfall_analyzer, [], 20)
    assert "No rainfall data" in out


def test_rainfall_analyzer_exact_threshold():
    out = _capture(rainfall_analyzer, [20, 20, 20], 20)
    assert "All readings within threshold" in out


def test_rainfall_analyzer_negative_readings():
    # Negative readings are below threshold — all within
    out = _capture(rainfall_analyzer, [-5, 0, 5], 10)
    assert "All readings within threshold" in out


# ──────────────────────────────────────────────────────────────────────────────
# Question 3 – Username Validator with Retry
# ──────────────────────────────────────────────────────────────────────────────

def test_username_validator_valid_first_try(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("valid_user1\n"))
    out = _capture(username_validator_with_retry, 3)
    assert "Username accepted!" in out


def test_username_validator_max_attempts_exceeded(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("ab\nab\nab\n"))
    out = _capture(username_validator_with_retry, 3)
    assert "Maximum attempts reached" in out
    assert out.count("Enter username:") == 3


def test_username_validator_valid_on_last_attempt(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("ab\n123bad\nGood_user9\n"))
    out = _capture(username_validator_with_retry, 3)
    assert "Username accepted!" in out
    assert out.count("Enter username:") == 3


def test_username_validator_too_long(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("a" * 16 + "\nValid_1\n"))
    out = _capture(username_validator_with_retry, 2)
    assert "Username accepted!" in out


def test_username_validator_must_start_with_letter(monkeypatch):
    monkeypatch.setattr("sys.stdin", StringIO("1invalid\nValid_1\n"))
    out = _capture(username_validator_with_retry, 3)
    assert "Username accepted!" in out


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 4 – Employee Performance Processor
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("employees, expected", [
#     (
#         [
#             {"name": "Alice", "scores": [90, 85, 88]},
#             {"name": "Bob",   "scores": [70, 65, 75]},
#         ],
#         {
#             "high_performers":    [{"name": "Alice", "average": 87.67}],
#             "needs_improvement":  [{"name": "Bob",   "average": 70.0}],
#         },
#     ),
#     ([], {"high_performers": [], "needs_improvement": []}),
# ])
# def test_employee_performance_processor_logic(employees, expected):
#     result = employee_performance_processor(employees)
#     for key in ("high_performers", "needs_improvement"):
#         for emp in result[key]:
#             emp["average"] = round(emp["average"], 2)
#         for emp in expected[key]:
#             emp["average"] = round(emp["average"], 2)
#     assert result == expected


# def test_employee_performance_processor_exact_boundary():
#     employees = [{"name": "Edge", "scores": [80, 80, 80]}]
#     result = employee_performance_processor(employees)
#     assert len(result["high_performers"]) == 1
#     assert result["high_performers"][0]["name"] == "Edge"


# def test_employee_performance_processor_empty_scores():
#     with pytest.raises(ValueError):
#         employee_performance_processor([{"name": "Test", "scores": []}])


# def test_employee_performance_processor_missing_keys():
#     with pytest.raises(KeyError):
#         employee_performance_processor([{"name": "Test"}])


# def test_employee_performance_processor_mixed():
#     employees = [
#         {"name": "Top",  "scores": [95, 90]},
#         {"name": "Low",  "scores": [55, 60]},
#         {"name": "Mid",  "scores": [82, 78]},
#     ]
#     result = employee_performance_processor(employees)
#     assert len(result["high_performers"]) == 2
#     assert len(result["needs_improvement"]) == 1


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 5 – Order Batcher
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("orders, batch_size, expected", [
#     (
#         ["O1", "O2", "O3", "O4", "O5"],
#         2,
#         [["O1", "O2"], ["O3", "O4"], ["O5"]],
#     ),
#     (["A", "B", "C"], 3, [["A", "B", "C"]]),
#     ([], 4, []),
# ])
# def test_order_batcher_logic(orders, batch_size, expected):
#     assert order_batcher(orders, batch_size) == expected


# def test_order_batcher_invalid_batch_size():
#     with pytest.raises(ValueError):
#         order_batcher(["A", "B"], 0)


# def test_order_batcher_batch_size_one():
#     assert order_batcher(["X", "Y", "Z"], 1) == [["X"], ["Y"], ["Z"]]


# def test_order_batcher_large_dataset():
#     orders = [f"ORD{i}" for i in range(1000)]
#     result = order_batcher(orders, 50)
#     assert len(result) == 20
#     assert all(len(b) == 50 for b in result)


# def test_order_batcher_preserves_order():
#     orders = ["first", "second", "third", "fourth"]
#     result = order_batcher(orders, 2)
#     assert result[0][0] == "first"
#     assert result[-1][-1] == "fourth"


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 6 – Social Network Analyzer
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("network, expected", [
#     (
#         {"Alice": ["Bob", "Carol"], "Bob": ["Carol"], "Carol": []},
#         {"total_follows": 3, "most_followed": "Carol", "no_followers": ["Alice"]},
#     ),
#     (
#         {"X": [], "Y": [], "Z": []},
#         {"total_follows": 0, "most_followed": None, "no_followers": ["X", "Y", "Z"]},
#     ),
#     ({}, {"total_follows": 0, "most_followed": None, "no_followers": []}),
# ])
# def test_social_network_analyzer_logic(network, expected):
#     result = social_network_analyzer(network)
#     assert result["total_follows"] == expected["total_follows"]
#     assert set(result["no_followers"]) == set(expected["no_followers"])
#     if expected["most_followed"] is None:
#         assert result["most_followed"] is None
#     else:
#         # Accept any user with the maximum in-degree
#         all_followed = [f for follows in network.values() for f in follows]
#         max_count = max(all_followed.count(u) for u in network) if all_followed else 0
#         top_users = [u for u in network if all_followed.count(u) == max_count]
#         assert result["most_followed"] in top_users


# def test_social_network_analyzer_single_user():
#     result = social_network_analyzer({"Solo": []})
#     assert result["total_follows"] == 0
#     assert result["no_followers"] == ["Solo"]


# def test_social_network_analyzer_no_isolates():
#     network = {"A": ["B"], "B": ["A"]}
#     result = social_network_analyzer(network)
#     assert result["no_followers"] == []
#     assert result["total_follows"] == 2


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 7 – Count Vowels (Recursive)
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("s, expected", [
#     ("hello", 2),
#     ("",      0),
#     ("AEIOU", 5),
#     ("rhythm", 0),
#     ("Python programming", 5),
# ])
# def test_count_vowels_logic(s, expected):
#     assert count_vowels(s) == expected


# def test_count_vowels_non_string():
#     with pytest.raises(TypeError):
#         count_vowels(123)


# def test_count_vowels_is_recursive():
#     with patch("new_assessment.count_vowels", wraps=count_vowels) as mocked:
#         mocked("hello")
#         assert mocked.call_count > 1, "Recursion not detected"


# def test_count_vowels_base_case():
#     assert count_vowels("") == 0
#     assert count_vowels("b") == 0
#     assert count_vowels("a") == 1


# def test_count_vowels_recursive_params():
#     with patch("new_assessment.count_vowels", wraps=count_vowels) as mocked:
#         mocked("aeiou")
#         for call in mocked.call_args_list:
#             args, _ = call
#             assert isinstance(args[0], str)


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 8 – Text Pipeline Processor
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("raw_texts, transformations, expected", [
#     (["hello", "world"], ["uppercase"], ["HELLO", "WORLD"]),
#     (["  hi  ", " there "], ["strip"], ["hi", "there"]),
#     (["keep", "", "me", ""], ["remove_empty"], ["keep", "me"]),
#     (["abc", "xyz"], ["reverse"], ["cba", "zyx"]),
#     ([], ["uppercase"], []),
# ])
# def test_text_pipeline_processor_logic(raw_texts, transformations, expected):
#     assert text_pipeline_processor(raw_texts, transformations) == expected


# def test_text_pipeline_processor_unknown_transformation():
#     with pytest.raises(ValueError):
#         text_pipeline_processor(["hello"], ["shout"])


# def test_text_pipeline_processor_chained():
#     result = text_pipeline_processor(["  hello  ", "  "], ["strip", "remove_empty", "uppercase"])
#     assert result == ["HELLO"]


# def test_text_pipeline_processor_no_transformations():
#     assert text_pipeline_processor(["a", "b"], []) == ["a", "b"]


# def test_text_pipeline_processor_reverse_then_uppercase():
#     result = text_pipeline_processor(["abc"], ["reverse", "uppercase"])
#     assert result == ["CBA"]


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 9 – Score Ranker
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("scores, expected", [
#     (
#         [("Alice", 100), ("Bob", 150), ("Charlie", 120)],
#         [("Bob", 150, 1), ("Charlie", 120, 2), ("Alice", 100, 3)],
#     ),
#     ([("Solo", 42)], [("Solo", 42, 1)]),
#     ([], []),
# ])
# def test_score_ranker_logic(scores, expected):
#     assert score_ranker(scores) == expected


# def test_score_ranker_tied_scores():
#     result = score_ranker([("A", 100), ("B", 100), ("C", 90)])
#     assert result[0][2] == 1
#     assert result[1][2] == 1
#     assert result[2][2] == 3   # rank skips to 3


# def test_score_ranker_all_tied():
#     result = score_ranker([("X", 50), ("Y", 50), ("Z", 50)])
#     assert all(r[2] == 1 for r in result)


# def test_score_ranker_invalid_tuple():
#     with pytest.raises(ValueError):
#         score_ranker([("Player", 100, "extra")])


# def test_score_ranker_large_dataset():
#     scores = [(f"P{i}", i) for i in range(500, 0, -1)]
#     result = score_ranker(scores)
#     assert result[0][1] == 500
#     assert result[-1][1] == 1
#     assert result[0][2] == 1
#     assert result[-1][2] == 500


# # ──────────────────────────────────────────────────────────────────────────────
# # Question 10 – Fibonacci (Recursive)
# # ──────────────────────────────────────────────────────────────────────────────

# @pytest.mark.parametrize("n, expected", [
#     (0,  0),
#     (1,  1),
#     (2,  1),
#     (5,  5),
#     (10, 55),
# ])
# def test_fibonacci_logic(n, expected):
#     assert fibonacci(n) == expected


# def test_fibonacci_negative():
#     with pytest.raises(ValueError):
#         fibonacci(-1)


# def test_fibonacci_non_integer():
#     with pytest.raises(ValueError):
#         fibonacci(3.5)


# def test_fibonacci_is_recursive():
#     with patch("new_assessment.fibonacci", wraps=fibonacci) as mocked:
#         mocked(6)
#         assert mocked.call_count > 1, "Recursion not detected"


# def test_fibonacci_base_cases():
#     assert fibonacci(0) == 0
#     assert fibonacci(1) == 1


# def test_fibonacci_recursive_params():
#     with patch("new_assessment.fibonacci", wraps=fibonacci) as mocked:
#         mocked(5)
#         for call in mocked.call_args_list:
#             args, _ = call
#             assert isinstance(args[0], int)