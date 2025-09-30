import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file
df = pd.read_csv('City-State-Condo-Price.csv')

# Convert date column to datetime if not already
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for California and New York
ca_data = df[(df['State'] == 'CA') & (df['RegionName'] == 'San Jose')]
ny_data = df[(df['State'] == 'NY') & (df['RegionName'] == 'New York')]

# Create the scatterplot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot California data
ax.scatter(ca_data['Date'], ca_data['Price'], 
           alpha=0.6, s=30, color='#FF6B6B', label='California', edgecolors='darkred', linewidth=0.5)

# Plot New York data
ax.scatter(ny_data['Date'], ny_data['Price'], 
           alpha=0.6, s=30, color='#4ECDC4', label='New York', edgecolors='darkblue', linewidth=0.5)

# Formatting
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Price ($)', fontsize=12, fontweight='bold')
ax.set_title('Condo Prices: San Jose, California vs. New York, New York', fontsize=14, fontweight='bold', pad=20)

# Format y-axis to show prices with commas
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:,.0f}'))

# Format x-axis dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
plt.xticks(rotation=45, ha='right')

# Add legend
ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

# Add grid for better readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5)

# Tight layout to prevent label cutoff
plt.tight_layout()

# Display the plot
plt.show()

