def suggest_cross_sell(purchase_history):
    # Dummy cross-selling logic for demonstration purposes
    # In a real-world scenario, this could be based on machine learning models or rules.
    cross_sell_products = {
        1: [2],  # If customer buys A, recommend B
        2: [],  # If customer buys B, recommend nothing
        3: [2],  # If customer buys C, recommend B
    }

    recommendations = []
    for product in purchase_history:
        if product in cross_sell_products:
            recommendations.extend(cross_sell_products[product])

    return list(set(recommendations))  # Remove duplicates
