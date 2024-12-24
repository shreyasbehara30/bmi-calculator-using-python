def calculate_bmi(weight, height):
    
    return weight / (height ** 2)

def get_bmi_category(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


if __name__ == "__main__":
   
       
        weight = float(input("Enter your weight in kilograms (kg): ").strip())
        height = float(input("Enter your height in meters (m): ").strip())
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers. Please try again.")
        else:
           
            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)
            
           
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Based on your BMI, you are categorized as: {category}")
    
    