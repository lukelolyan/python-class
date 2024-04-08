WEIGHT_WIDGET = 75  # grams
WEIGHT_GIZMO = 112  # grams

def main():
    # Input the number of widgets and gizmos
    num_widgets = int(input("Enter the number of widgets: "))
    num_gizmos = int(input("Enter the number of gizmos: "))

    # Calculate the total weight of the order
    total_weight = (num_widgets * WEIGHT_WIDGET) + (num_gizmos * WEIGHT_GIZMO)

    # Display the total weight of the order
    print("Total weight of the order:", total_weight, "grams")

if __name__ == "__main__":
    main()
