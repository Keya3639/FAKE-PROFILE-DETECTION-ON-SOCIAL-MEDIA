# FAKE-PROFILE-DETECTION-ON-SOCIAL-MEDIA
The **Fake Profile Detection System** is a machine-learning based web application designed to identify whether a social media account is real or fake using profile attributes instead of manual verification.It analyzes important factors such as follower counts, posts, bio availability, links, and profile picture presence to detect suspicious user behavior patterns.

This tool helps users, researchers, educators, and cybersecurity teams automatically analyze profiles and reduce the risk of scams, spam, impersonation, and fake engagement.
## Overview

The system uses a trained **Machine Learning Classification Model (Random Forest)** to predict whether a profile is real or fake.
Instead of checking only one feature, the model evaluates multiple attributes together and recognizes hidden patterns commonly seen in fake accounts.

When a user enters details, the system:

- Takes profile information as input
- Converts data into model-readable format
- Converts data into model-readable format
- Converts data into model-readable format
- Predicts probability of fake vs real
- Displays confidence score and result

It runs as a Django web application, making it simple, structured, and user-friendly.

## Tools and Technologies Used

- **Python:** Core programming language
- **Django:** Web framework for building the application
- **Machine Learning (Random Forest Classifier):** Predicts fake vs real profiles
- **Pandas:** Handles dataset and feature processing
- **Joblib:** Loads saved ML model
- **HTML / CSS:** Front-end interface design
- **Bootstrap / Custom Styling:** For responsive UI
- **SQLite:** Default Django database

## Why These Tools Were Selected

- Django provides authentication, views, templates, routing, and scalability.
- Random Forest handles non-linear relationships and works well with mixed features.
- Pandas simplifies feature engineering and dataset handling.
- Joblib makes saving and loading ML models efficient.
- HTML + CSS help create clean, interactive UI screens.

Together, these tools make the project stable, modular, and production-ready.

## Features

- Detects whether a profile is real or fake
- Supports multiple platforms (Instagram, Twitter, Threads)
- Confidence score for prediction
- Clean and interactive UI
- Debug logs during analysis
- Secure CSRF-protected forms
- Model-driven predictions instead of manual rules

## How It Works

- User selects platform
- Enters profile details such as:

  - *Number of posts*
  - *Followers*
  - *Following*
  - *Bio present or not*
  - *Profile picture present or not*
  - *Private account*
  - *Link available or not*
- Data is processed and converted to numeric format
- Random Forest model predicts profile authenticity
- Result page displays:
  
  - *Profile status (Real / Fake)*
  - *Confidence percentage*
  - *Summary of inputs*
    
## Advantages

- Reduces time spent manually checking accounts
- Detects suspicious accounts early
- Handles multiple features at the same time
- Works even when some details are missing
- Highly interpretable with logs & confidence level
- Easy to deploy and integrate into portals
  
## Limitations

- Model accuracy depends on training dataset quality
- Cannot detect deep-fake identity verification
- Limited to provided features — full profile scraping not included
- Results are probabilistic (not guaranteed confirmation)
- Needs retraining for new platforms and behavior patterns

## Real-Time Applications

- **Social Media Research:** Identify bots and fake engagement
- **Cybersecurity:** Detect scam and impersonation profiles
- **Student Projects:** Demonstrates ML + Django integration
- **Content Moderation:** Filter out spam accounts
- **Business Marketing:** Validate influencer authenticity
  
## Future Enhancements

- Live scraping from platforms using APIs
- Advanced deep-learning model for improved accuracy
- Visualization dashboards
- Role-based login system (admin/user)
- Real-time prediction history storage
- Graph-based fraud analysis
- Deployment on cloud (Render / AWS / Railway / PythonAnywhere)
  
## Conclusion

The Fake Profile Detection System demonstrates how Machine Learning and Django can work together to solve real-world online safety problems.By analyzing profile patterns instead of relying on manual checks, this project provides a smart approach toward identifying suspicious accounts and improving digital security.
With further improvement and larger datasets, it can evolve into a powerful verification tool for social media platforms and research communities.
## OUTPUT:
<img width="643" height="637" alt="Image" src="https://github.com/user-attachments/assets/e222c1bb-68a3-4351-a8d5-770a32a0ed2d" />
<img width="507" height="830" alt="Image" src="https://github.com/user-attachments/assets/8c1916c8-8328-4372-85f6-6afc787d8e3b" />
<img width="565" height="792" alt="Image" src="https://github.com/user-attachments/assets/a2d915ba-726e-48cf-ac0a-f9e950e6bc43" />
<img width="563" height="515" alt="Image" src="https://github.com/user-attachments/assets/dd78bf26-108f-4b11-ba68-5f8d102a179f" />
