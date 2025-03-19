import joblib
import numpy as np
from flask import Flask, render_template, request
from config.paths_config import MODEL_OUTPUT_PATH  # Ensure this file exists

app = Flask(__name__)

# Load the model (ensure MODEL_OUTPUT_PATH is correct)
try:
    loaded_model = joblib.load(MODEL_OUTPUT_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    loaded_model = None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Extract form data with error handling
            lead_time = int(request.form.get("lead_time", 0))
            no_of_special_request = int(request.form.get("no_of_special_request", 0))
            avg_price_per_room = float(request.form.get("avg_price_per_room", 0.0))
            arrival_month = int(request.form.get("arrival_month", 1))
            arrival_date = int(request.form.get("arrival_date", 1))
            market_segment_type = int(request.form.get("market_segment_type", 0))
            no_of_week_nights = int(request.form.get("no_of_week_nights", 0))
            no_of_weekend_nights = int(request.form.get("no_of_weekend_nights", 0))
            type_of_meal_plan = int(request.form.get("type_of_meal_plan", 0))
            room_type_reserved = int(request.form.get("room_type_reserved", 0))

            # Prepare features for prediction
            features = np.array([[lead_time, no_of_special_request, avg_price_per_room,
                                  arrival_month, arrival_date, market_segment_type,
                                  no_of_week_nights, no_of_weekend_nights,
                                  type_of_meal_plan, room_type_reserved]])

            # Make prediction
            if loaded_model is not None:
                prediction = loaded_model.predict(features)[0]
            else:
                prediction = None  # Handle case where model failed to load

            return render_template('index.html', prediction=prediction)
        except ValueError as e:
            return render_template('index.html', prediction=None, error=f"Invalid input: {e}")
        except Exception as e:
            return render_template('index.html', prediction=None, error=f"Error: {e}")

    return render_template("index.html", prediction=None, error=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)  # Enable debug mode