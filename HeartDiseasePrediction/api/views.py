from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MedicalDataSerializer
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Load and train model
df = pd.read_csv('E:\Heart_Disease_Prediction_model\HeartDiseasePrediction\heart_data.csv')  # Replace with actual path
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

model = DecisionTreeClassifier()
model.fit(X, y)

@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        serializer = MedicalDataSerializer(data=request.data)
        if serializer.is_valid():
            input_data = np.array(list(serializer.validated_data.values())).reshape(1, -1)
            prediction = model.predict(input_data)[0]
            return Response({'prediction': 'Positive' if prediction == 1 else 'Negative'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
