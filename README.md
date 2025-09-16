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

### 2. Dev Container Setup (Recommended)
   1. Open the project in Visual Studio Code.
   1. Install the Dev Containers extension.
   1. Reopen the project in the Dev Container:
      - Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS).
      - Select Dev Containers: Reopen in Container.
   1. The container will automatically install all dependencies from requirements.txt.  
     
### 3. Docker Setup
   1. Build the Docker image:   
   ```bash
   docker build -t gold-price-analysis .
   ```

   2. Run the container:
   ```bash
   docker run --rm -it gold-price-analysis
   ```

### 4. Manual Setup (Without Dev Container or Docker)
a. Set Up a Virtual Environment  
```bash
python3 -m venv .venv
source .venv/bin/activate
```  
b. Install Dependencies  
```bash
make install
```  

### 5. Run the Main Script  
```bash
make run
```  
### 6. Run Unit Tests   
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
