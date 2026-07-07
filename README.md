# Root Finder using Bisection Search

This Python script estimates the root of a number raised to a given power using the bisection search method.

## How to Use

1.  **Run the script**: Execute `main.py` using a Python interpreter.
    ```bash
    python main.py
    ```
2.  **Enter inputs**: The script will prompt you to enter three values:
    *   `enter number to find root of`: The number `x` for which you want to find the root.
    *   `enter power`: The power `p` such that you are looking for `x^(1/p)`.
    *   `epsilon`: The desired precision for the root estimation. The search stops when the absolute difference between `ans^p` and `x` is less than or equal to `epsilon`.

3.  **View the result**: The script will print the estimated root.

## How It Works

The script implements a `find_root` function that uses the bisection search algorithm to find the `p`-th root of a number `x`.

1.  **Initialization**:
    *   It first checks for invalid inputs (e.g., finding an even root of a negative number).
    *   It establishes an initial search interval `[low, high]` that is guaranteed to contain the root. This interval is set to `[-1, x]` or `[x, 1]` depending on the value of `x`.

2.  **Bisection Search**:
    *   The algorithm repeatedly halves the search interval.
    *   In each iteration, it calculates the midpoint `ans` of the current interval `[low, high]`.
    *   It then checks if `ans` raised to the `power` is less than or greater than `x`:
        *   If `ans^power < x`, the root must be in the upper half, so `low` is updated to `ans`.
        *   If `ans^power > x`, the root must be in the lower half, so `high` is updated to `ans`.
    *   This process continues until the absolute difference between `ans^power` and `x` is less than or equal to the specified `epsilon`.

3.  **Output**: The final `ans` value, which is the estimated root, is returned and printed.

## Example

If you run the script and provide the following inputs:

*   `enter number to find root of: 27`
*   `enter power: 3`
*   `epsilon: 0.001`

The script will output a value close to `3.0`.