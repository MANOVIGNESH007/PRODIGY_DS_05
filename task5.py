import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset with specified encoding
df = pd.read_csv('AviationData.csv', encoding='latin1')

# Display the first few rows and column names
print(df.head())
print(df.columns)

# Check for missing values
print(df.isnull().sum())

# Handling missing or irrelevant columns
df_cleaned = df.drop(['Accident.Number', 'Airport.Code', 'Publication.Date'], axis=1)
df_cleaned['Weather.Condition'].fillna('Unknown', inplace=True)
df_cleaned.dropna(subset=['Broad.phase.of.flight'], inplace=True)

# Confirming the changes
print(df_cleaned.info())

# Save cleaned dataset to a new CSV file
df_cleaned.to_csv('AviationData_cleaned.csv', index=False)
print("Cleaned dataset saved to AviationData_cleaned.csv")

# Example: Visualizing accident counts by weather condition
plt.figure(figsize=(10, 6))
sns.countplot(x='Weather.Condition', data=df_cleaned)
plt.title('Accident Counts by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Accident Count')
plt.xticks(rotation=45)
plt.savefig("Accident Counts by Weather Condition")
plt.show()

# Example: Visualizing accident locations on a map
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=df_cleaned, hue='Weather.Condition', palette='viridis', s=50)
plt.title('Accident Locations by Latitude and Longitude')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(title='Weather Condition')
plt.savefig("Accident Locations by Latitude and Longitude")
plt.show()
