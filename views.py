from django.shortcuts import render, redirect
import joblib
import pandas as pd
import os

def home(request):
    if request.method == 'POST':
        platform = request.POST.get('platform')
        return redirect('input_details', platform=platform)
    return render(request, 'home.html')

def input_details(request, platform):
    if request.method == 'POST':
        try:
            # Debug: Print received POST data
            print("\n=== RAW POST DATA ===")
            for key, value in request.POST.items():
                print(f"{key}: {value}")
            
            # Load model
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            model_path = os.path.join(BASE_DIR, 'fake_account_model.pkl')
            model = joblib.load(model_path)
            print("\nModel features expected:", model.feature_names_in_)

            # Prepare input data EXACTLY as model expects
            input_data = {
                'Number of posts': [float(request.POST.get('posts'))],
                'Number of followers': [float(request.POST.get('followers'))],
                'Number of following': [float(request.POST.get('following'))],
                'Bio': [1 if request.POST.get('BIO') == 'present' else 0],
                'Profile Pic': [1 if request.POST.get('profile_pic') == 'present' else 0],
                'Private Account': [1 if request.POST.get('private_account') == 'yes' else 0],
                'Link Present': [1 if request.POST.get('link_present') == 'yes' else 0]            
            }

            print("\nProcessed input data:", input_data)
            
            # Create DataFrame
            features = pd.DataFrame(input_data)
            
            # Make prediction and get confidence
            prediction_proba = model.predict_proba(features)[0]  # Get probability for both classes
            prediction = model.predict(features)[0]  # Get predicted class
            confidence = round(max(prediction_proba) * 100, 2)  # Confidence is max probability * 100
            is_fake = bool(prediction)  # 1 is fake, 0 is real

            print(f"\nPrediction result: {'FAKE' if is_fake else 'REAL'}")
            print(f"Confidence: {confidence}%")

            # Model accuracy (static example, update if you have a proper accuracy metric)
            model_accuracy = 100.0  # You can replace this with actual accuracy from testing

            return render(request, 'result.html', {
                'is_fake': is_fake,
                'username': request.POST.get('username'),
                'platform': platform,
                'confidence': confidence,
                'accuracy': model_accuracy,  # Add model accuracy
                'input_data': input_data  # For debugging
            })
            
        except Exception as e:
            print(f"\nERROR: {str(e)}")
            return render(request, 'input_details.html', {
                'platform': platform,
                'error': f"Analysis failed. Please check console for details."
            })
    
    return render(request, 'input_details.html', {'platform': platform})
