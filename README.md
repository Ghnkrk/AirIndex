# 🌍 **Breathe Better: Air Quality Prediction App**  
Welcome to the **Air Quality Prediction App** – a seamless, AI-powered tool to assess air quality levels based on pollutant data like **CO**, **Ozone**, **NO₂**, and **PM₂.5**. Take a deep breath and explore smarter predictions! 🌬️✨  

---

## 🌟 **Why Choose This App?**  
🔮 **Accurate Predictions**: Predicts air quality categories instantly using cutting-edge machine learning models.  
🎨 **Stylish Interface**: Experience a sleek, modern UI with smooth transitions and gradient visuals.  
⚡ **Fast & Interactive**: Powered by **Streamlit** for blazing-fast performance and responsive design.  

---

## 🔧 **Tech Behind the Magic**  
🔹 **Frontend**: Built with Streamlit for simplicity and elegance.  
🔹 **Machine Learning**: Models powered by Scikit-learn and xgboost with robust preprocessing pipelines.  
🔹 **Backend**: Python-based architecture for flexibility and power.  

---

## 📥 **How to Get Started**  
Follow these simple steps to set up and run the app on your machine:  

1️⃣ **Clone this Repository**:  
```bash  
git clone https://github.com/Ghnkrk/AirIndex.git  
cd AirIndex
```  

2️⃣ **Install Required Packages**:  
```bash  
pip install -r Requirements.txt  
```  

3️⃣ **Run the App**:  
```bash  
streamlit run app.py  
```  

✨ And voilà! The app is up and running.  

---

## 🎯 **How Does It Work?**  
📝 **Input Your Data**: Enter AQI values for pollutants like CO, Ozone, NO₂, and PM₂.5.  
🛠️ **Preprocessing**: Data is scaled using a pre-trained scaler for consistency.  
🤖 **Prediction**: The ML model predicts the air quality category in real-time.  
🎉 **Output**: A visually appealing result is displayed instantly.  

---

## 📂 **Project Directory**  
```
📁 air-quality-prediction/
├── app.py                                # Core application logic  
├── model.pkl                             # Pre-trained machine learning model  
├── requirements.txt                      # List of dependencies  
├── AirQualityIndex.ipynb                 # Notebook where the data is processed and model is trained
├── global air pollution dataset.csv      # The dataset the model is trained on
├── README.md                             # This very document
```  

---

## 💡 **Workflow Explained**  
1️⃣ **Preprocessing**  
   - Inputs are scaled with `PowerTransformer`.  
   - Encoded labels ensure accurate predictions.  

2️⃣ **Model Training**  
   - **RandomSearchCV** is used to determine the best estimator and its best hyperparameters among **Linear Regression , Support Vector Regression and XGBRegressor**.  
   - The best estimator **XGBRegressor** is saved as `model.pkl` using Pickle.  

3️⃣ **Deployment**  
   - Streamlit provides an intuitive user interface for data input and results.  

---

## 🚀 **Running the Training Pipeline**  
Want to train your own model? No problem!  

```bash
jupyter nbconvert --to script model.ipynb
python model.py
```  

The script:  
- Loads and preprocesses the dataset.  
- Trains the best estimator **XGBRegressor**.  
- Exports the trained model to `model.pkl`.

---

## 📊 **Features You'll Love**  
🌈 **Responsive Layout**: Works beautifully on all screen sizes.  
📈 **Dynamic Results**: Instant prediction of AQI categories like "Good," "Moderate," etc.  
🎨 **Engaging Visuals**: Smooth animations and intuitive design elements.  

---

## 🚧 **Future Roadmap**  
🔄 **Real-Time Data**: Integrate live AQI updates via APIs.  
📊 **Visualization**: Show historical trends and future forecasts.  
📋 **Comparison Tools**: Side-by-side AQI comparisons based on global standards.  

---

## 📜 **License**  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  

---

## 🙏 **Acknowledgments**  
💖 Thanks to:  
- **Streamlit**: For providing an amazing app framework.  
- **Scikit-learn**: For enabling easy and efficient ML development.  
- Everyone who contributed to making this project a reality!  

---

🌟 **Start Predicting Now**  
Unleash the power of machine learning to create a cleaner, healthier environment. 🌱  

---
