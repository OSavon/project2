def evaluate_polynomial(coeffs, x):
    """
    Evaluate a 5th order polynomial at x.
    coeffs should be a list or tuple of 6 values:
    [a5, a4, a3, a2, a1, a0]
    """
    if len(coeffs) != 6:
        raise ValueError("Expected 6 coefficients for a 5th order polynomial")
    return sum(coef * x**exp for exp, coef in enumerate(reversed(coeffs)))

if __name__ == "__main__":
    # Example coefficients for: 2x^5 - x^4 + 3x^3 - 4x^2 + x - 7
    coeffs = [2, -1, 3, -4, 1, -7]
    x = 1.5
    result = evaluate_polynomial(coeffs, x)
    print(y"Polynomial value at x={x}: {result}")