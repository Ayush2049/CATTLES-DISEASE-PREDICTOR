from predict import predict_disease, get_available_info

def main():
    print("🐄🐑 Veterinary Disease Predictor 🐐🐃")
    print("=" * 60)
    
    # Get available options
    info = get_available_info()
    
    print(f"📋 Available Animals: {', '.join(info['animals'])}")
    print(f"🏥 Can Predict: {', '.join(info['diseases'])}")
    print("\n💊 Available Symptoms:")
    
    # Display symptoms in a nice format
    symptoms = info['symptoms']
    for i, symptom in enumerate(symptoms, 1):
        print(f"   {i:2d}. {symptom}")
    
    print("=" * 60)
    
    try:
        # Get user input
        animal = input("\n🐄 Enter animal type (cow/buffalo/sheep/goat): ").strip().lower()
        
        if animal not in info['animals']:
            print(f"⚠️ Warning: '{animal}' not in training data, but continuing...")
        
        age = int(input("📅 Enter age of animal (years): "))
        temperature = float(input("🌡️ Enter temperature (°F): "))
        
        print(f"\n💊 Enter symptoms from the list above (separated by commas):")
        print(f"   💡 Example: loss of appetite, fatigue, difficulty walking")
        symptoms_input = input("🔍 Your symptoms: ")
        symptoms = [s.strip().lower() for s in symptoms_input.split(",") if s.strip()]
        
        if not symptoms:
            print("❌ No symptoms provided! Using only animal data...")
        
        print("\n🔄 Analyzing...")
        
        # Make prediction
        disease, confidence, valid_symptoms = predict_disease(animal, age, temperature, symptoms)
        
        # Display results
        print("\n" + "="*60)
        print("📊 PREDICTION RESULTS")
        print("="*60)
        print(f"🐄 Animal: {animal.title()}")
        print(f"📅 Age: {age} years")
        print(f"🌡️ Temperature: {temperature}°F")
        print(f"💊 Symptoms entered: {', '.join(symptoms) if symptoms else 'None'}")
        print(f"✅ Valid symptoms recognized: {', '.join(valid_symptoms) if valid_symptoms else 'None'}")
        print("-"*60)
        print(f"🏥 Predicted Disease: {disease.upper()}")
        print(f"📈 Confidence Level: {confidence:.1%}")
        print("="*60)
        
        # Confidence interpretation
        if confidence < 0.4:
            print("🔴 LOW confidence - Very uncertain prediction")
        elif confidence < 0.7:
            print("🟡 MODERATE confidence - Reasonable prediction")
        else:
            print("🟢 HIGH confidence - Strong prediction")
            
        if not valid_symptoms:
            print("⚠️  Note: Prediction based only on animal type, age, and temperature")
            print("   Try using symptoms from the available list for better accuracy")
            
        print("\n📞 IMPORTANT: Always consult a qualified veterinarian for proper diagnosis and treatment!")
        print("   This tool is for educational purposes and preliminary assessment only.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye! Take care of your animals!")
    except ValueError as e:
        print(f"❌ Input error: Please enter valid numbers for age and temperature.")
        print(f"   Error details: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        print("   Please check that all model files exist and try again.")

if __name__ == "__main__":
    main()