def get_minimum_coins_recursive(denominations, total):
    # Memoization dictionary to store results of subproblems
    memo = {}

    def helper(remaining):
        # Base case: If the remaining amount is 0, no coins are needed
        if remaining == 0:
            return []

        # Base case: If the remaining amount is negative, it's not possible
        if remaining < 0:
            return None

        # If the result is already computed, return it
        if remaining in memo:
            return memo[remaining]

        # Try using each coin and find the combination with the minimum coins
        best_solution = None
        for coin in denominations:
            result = helper(remaining - coin)
            if result is not None:
                current_solution = result + [coin]
                if best_solution is None or len(current_solution) < len(best_solution):
                    best_solution = current_solution

        # Store the result in the memoization dictionary
        memo[remaining] = best_solution
        return best_solution

    # Call the helper function
    solution = helper(total)

    # If no solution exists
    if solution is None:
        return "Change not possible"

    return solution
