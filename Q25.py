import matplotlib.pyplot as plt

def visualize_sales():
    # Data definition
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sales = [45000, 52000, 48000, 61000, 58000, 65000, 62000, 70000, 68000, 75000, 72000, 80000]

    # Identify highest and lowest sales months
    max_sales = max(sales)
    min_sales = min(sales)
    max_month = months[sales.index(max_sales)]
    min_month = months[sales.index(min_sales)]

    print(f"Highest Sales: {max_month} (₹{max_sales})")
    print(f"Lowest Sales: {min_month} (₹{min_sales})")

    # Create a figure with two subplots (1 row, 2 columns)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # 1. Line Chart
    ax1.plot(months, sales, marker='o', linestyle='-', color='b', linewidth=2, markersize=6)
    ax1.set_title('Monthly Sales Revenue (Line Chart)')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Sales (₹)')
    ax1.grid(True, linestyle='--', alpha=0.7)

    # 2. Bar Chart
    bars = ax2.bar(months, sales, color='skyblue', edgecolor='black')
    ax2.set_title('Monthly Sales Revenue (Bar Chart)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Sales (₹)')
    
    # Highlight highest and lowest on the bar chart
    bars[sales.index(max_sales)].set_color('green')
    bars[sales.index(min_sales)].set_color('red')

    # Add data labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 1000, f"{yval}", ha='center', va='bottom', fontsize=9)

    # Adjust layout and display
    plt.tight_layout()
    plt.show()

# Execute the visualization function
visualize_sales()
