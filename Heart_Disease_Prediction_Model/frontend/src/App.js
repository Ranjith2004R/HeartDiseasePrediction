import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    age: "",
    gender: "",
    heart_rate: "",
    systolic_bp: "",
    diastolic_bp: "",
    blood_sugar: "",
    ck_mb: "",
    troponin: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const response = await axios.post("http://localhost:8000/api/predict/", formData);
      setPrediction(response.data.prediction);
    } catch (err) {
      setError("Error making prediction. Please try again.");
      console.error("Prediction Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="diabetes-form-container">
      <h1 className="form-title">Heart Disease Prediction</h1>
      <form className="diabetes-form" onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div className="form-field" key={key}>
            <label className="field-label">{key.replace(/_/g, " ")}:</label>
            <input
              className="field-input"
              type={key === "gender" ? "text" : "number"}  // Gender as text, others as numbers
              name={key}
              value={formData[key]}
              onChange={handleChange}
              required
            />
          </div>
        ))}
        <button className="submit-button" type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict"}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}
      {prediction && (
        <div className="result-container">
          <h2 className="result-title">Prediction:</h2>
          <p className="result">{prediction}</p>
          <button className="recheck-button" onClick={() => setPrediction(null)}>
            Recheck
          </button>
        </div>
      )}
    </div>
  );
}

export default App;
