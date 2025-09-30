# Condo Price Scatterplot: San Jose vs. New York

## Overview
This Python script creates a scatterplot visualization comparing condo prices between San Jose, California and New York, New York over time using data from Zillow's publicly available condo market datasets.

## Requirements
- Python 3.x
- pandas
- matplotlib

Install dependencies:
```bash
pip install pandas matplotlib
```

## Data Format
The script expects a CSV file named `City-State-Condo-Price.csv` with the following columns:
- `RegionName`: City name (e.g., "San Jose", "New York")
- `State`: State abbreviation (e.g., "CA", "NY")
- `Date`: Date values (converted to datetime objects)
- `Price`: Condo price values in dollars

## How It Works

### 1. Loading and Preparing Data
```python
df = pd.read_csv('City-State-Condo-Price.csv')
df['Date'] = pd.to_datetime(df['Date'])
```
The script loads the CSV file into a pandas DataFrame and converts the Date column to datetime objects for proper time-series handling.

### 2. Filtering Data by Region and State
```python
ca_data = df[(df['State'] == 'CA') & (df['RegionName'] == 'San Jose')]
ny_data = df[(df['State'] == 'NY') & (df['RegionName'] == 'New York')]
```

This uses **boolean indexing** with multiple conditions:
- `df['State'] == 'CA'` creates a True/False mask for California rows
- `df['RegionName'] == 'San Jose'` creates a True/False mask for San Jose rows
- The `&` operator combines both conditions (both must be True)
- Parentheses are required due to operator precedence
- The result is a filtered DataFrame containing only San Jose, CA data

The same logic applies for New York data.

### 3. Creating the Scatterplot
```python
fig, ax = plt.subplots(figsize=(12, 7))
ax.scatter(ca_data['Date'], ca_data['Price'], ...)
ax.scatter(ny_data['Date'], ny_data['Price'], ...)
```

The script creates two scatter series:
- **X-axis**: Date values from the filtered data
- **Y-axis**: Price values from the filtered data
- **San Jose**: Red points (#FF6B6B)
- **New York**: Teal points (#4ECDC4)

### 4. Formatting Features
- **Price formatting**: Y-axis displays prices with dollar signs and commas (e.g., $500,000)
- **Date formatting**: X-axis shows dates in MM-YYYY format
- **Rotated labels**: X-axis labels rotated 45° for readability
- **Grid lines**: Semi-transparent grid for easier value reading
- **Legend**: Distinguishes between the two cities

## Usage
1. Ensure your CSV file is named `City-State-Condo-Price.csv` and is in the same directory as the script
2. Run the script:
```bash
python your_script_name.py
```
3. The scatterplot will display in a new window

## Customization
To compare different cities, modify the filtering conditions:
```python
ca_data = df[(df['State'] == 'CA') & (df['RegionName'] == 'San Francisco')]
tx_data = df[(df['State'] == 'TX') & (df['RegionName'] == 'Austin')]
```

Update the legend labels and title accordingly.

## Output
The visualization shows:
- How condo prices evolved over time for each city
- Price disparities between markets
- Trends such as market crashes, recoveries, and boom periods
- The 2008 financial crisis impact and differential recovery speeds
