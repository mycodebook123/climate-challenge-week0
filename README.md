# African Climate Trend Analysis (2015–2026)

This repository contains an exploratory data analysis (EDA) and an interactive dashboard of historical climate data for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria. The project aims to identify regional weather patterns and extreme events to support Ethiopia's strategic position for the COP32 climate conference.

## 📊 Key Analysis Insights
Across the five analyzed regions, several distinct patterns emerged:
* **Thermal Extremes:** Sudan exhibited the highest thermal intensity, with mean temperatures of 28.76°C, highlighting severe desertification risks.
* **Rainfall Drivers:** Relative Humidity (RH2M) was identified as the primary driver for precipitation in Nigeria and Tanzania, showing strong positive correlations.
* **Precipitation Instability:** Tanzania showed the highest rainfall variability (Std Dev: 8.00), suggesting highly unpredictable seasons.
* **Data Integrity:** All datasets were cleaned of NASA sentinel values (-999) and validated using Z-score statistical analysis.

## 🖥️ Interactive Dashboard
A Streamlit-based dashboard is included to allow stakeholders to explore the data dynamically.
* **Features:** Multi-country selection, year range filtering, and real-time visualization of temperature and rainfall trends.
* **To run locally:** `streamlit run app/main.py`

## 📂 Project Structure
* `notebooks/`: Individual Jupyter notebooks for each country and the cross-country comparison.
* `app/`: Streamlit application files (`main.py` and `utils.py`).
* `data/`: Directory for raw and cleaned climate datasets (Note: Raw data is ignored via .gitignore).
* `requirements.txt`: List of Python libraries required to run the analysis.

## 🚀 How to Reproduce the Environment
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/mycodebook123/climate-challenge-week0.git](https://github.com/mycodebook123/climate-challenge-week0.git)
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

Streamlit: Interactive dashboard development.

Scipy: Statistical Z-score calculations for outlier detection.