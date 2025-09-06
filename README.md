# Gold Price Analysis

This project analyzes gold price data from 2015 to 2025, exploring trends, relationships with other financial instruments, and applying machine learning techniques to predict gold prices. The project also includes data visualization and cumulative return analysis.


---

## Features

1. **Data Inspection**:
   - Loads and inspects the dataset for missing values and data types.

2. **Data Filtering and Grouping**:
   - Filters data by date range.
   - Calculates yearly means for selected financial instruments.

3. **Machine Learning**:
   - Uses linear regression to predict gold prices based on other financial indicators.

4. **Visualization**:
   - Creates cumulative return plots for selected financial instruments.

5. **Unit Testing**:
   - Comprehensive tests for all major functionalities using the `unittest` framework.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/im-Tree/simple_data_analysis.git
cd simple_data_analysis
```

### 2. Set Up a Virtual Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate
```  

### 3. Install Dependencies  
```bash
make install
```  

### n4. Run the Main Script  
```bash
make run
```  
### 5. Run Unit Tests   
```bash
make test
```   
  
## Findings  
1. Gold Price Trends:  
    Gold prices showed a steady increase from 2015 to 2025, with occasional fluctuations. 
       
1. Correlation with Other Instruments:   
    Gold return are positively correlated with silver (SLV) return.   
   
1. Machine Learning Results:    
    The linear regression model achieved an R-squared value of ~0.61, indicating a strong relationship between the selected features(SPX return, EUR/USD return, SLV return) and gold return.
