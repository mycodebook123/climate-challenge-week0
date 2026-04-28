African Climate Trend Analysis (2015–2026)
This repository contains an exploratory data analysis (EDA) of historical climate data for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria. The project aims to identify regional weather patterns and extreme events to support Ethiopia's strategic position for the COP32 climate conference.

📊 Key Analysis Insights
Across the five analyzed regions, several distinct patterns emerged:

Thermal Extremes: Sudan exhibited the highest thermal intensity, with temperatures peaking near 46°C, highlighting severe desertification risks.

Rainfall Drivers: Relative Humidity (RH2M) was identified as the primary driver for precipitation in Nigeria and Tanzania, showing strong positive correlations.

Climate Stability: Ethiopia and Kenya demonstrated consistent seasonal bimodal patterns, though extreme rainfall events (outliers) were preserved to model flash-flood risks.

Data Integrity: All datasets were cleaned of NASA sentinel values (-999) and validated using Z-score statistical analysis.

📂 Project Structure
notebooks/: Contains individual Jupyter notebooks for each country's analysis.

data/: Directory for raw and cleaned climate datasets (Note: Raw data is ignored via .gitignore).

requirements.txt: List of Python libraries required to run the analysis.

🚀 How to Reproduce the Environment
Clone the repository:

Bash
git clone https://github.com/mycodebook123/climate-challenge-week0.git
cd climate-challenge-week0
Set up a Virtual Environment:

Bash
python -m venv venv
Activate the environment:

Windows: .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install Dependencies:

Bash
pip install -r requirements.txt
🛠️ Tools Used
Pandas & Numpy: Data manipulation and cleaning.

Matplotlib & Seaborn: Statistical data visualization.

Scipy: Statistical Z-score calculations for outlier detection.