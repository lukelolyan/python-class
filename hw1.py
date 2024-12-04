def fractional_knapsack(capacity, items):
    total_value = 0  
    while capacity > 0 and items:
  
        best_item_index = -1
        best_ratio = 0
        for i, (weight, value) in enumerate(items):
            ratio = value / weight
            if ratio > best_ratio:
                best_ratio = ratio
                best_item_index = i

        if best_item_index == -1:
            break  

 
        weight, value = items.pop(best_item_index)
        if weight <= capacity:
         
            total_value += value
            capacity -= weight
        else:
         
            total_value += value * (capacity / weight)
            capacity = 0  
    return total_value

# Example usage
capacity = 50
items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
result = fractional_knapsack(capacity, items)
print(f"Maximum value: {result}")
