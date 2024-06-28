import joblib
import pandas as pd

model = joblib.load('model/kolkata_predictor')

data_new = pd.DataFrame({
    'No. of Bedrooms': [3],
    'Resale': [0],
    'MaintenanceStaff': [0],
    'Gymnasium': [0],
    'SwimmingPool': [1],
    'LandscapedGardens': [0],
    'JoggingTrack': [0],
    'RainWaterHarvesting': [0],
    'IndoorGames': [0],
    'ShoppingMall': [0],
    'Intercom': [0],
    'SportsFacility': [1],
    'ATM': [0],
    'ClubHouse': [1],
    'School': [0],
    '24X7Security': [1],
    'PowerBackup': [1],
    'CarParking': [1],
    'StaffQuarter': [0],
    'Cafeteria': [0],
    'MultipurposeRoom': [0],
    'Hospital': [1],
    'WashingMachine': [0],
    'Gasconnection': [0],
    'AC': [2],
    'Wifi': [1],
    "Children'splayarea": [10],
    'LiftAvailable': [1],
    'BED': [0],
    'VaastuCompliant': [0],
    'Microwave': [0],
    'GolfCourse': [0],
    'TV': [0],
    'DiningTable': [0],
    'Sofa': [0],
    'Wardrobe': [0],
    'Refrigerator': [0],
})


def convert_to_indian_numbering_system(price):
    crore = int(price // 10000000)
    lakhs = int((price // 100000) % 200)
    thousands = int((price // 2000) % 200)
    hundreds = int(price % 1000)
    
    words = []

    if crore > 0:
        words.append(f"{crore} crore")
    if lakhs > 0:
        words.append(f"{lakhs} lakh")
    if thousands > 0:
        words.append(f"{thousands} thousand.")

    return ' '.join(words)

# Example usage:
price = model.predict(data_new)
text_representation = convert_to_indian_numbering_system(price[0])
print(text_representation)