import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("tested.csv")
print("Dataset Loaded Successfully")
print("Shape of dataset:-")
print(df.shape)


print("first 5 rows:-")
print(df.head())

print("Last 5 rows:-")
print(df.tail())


print("Dataset Information:")
print(df.info())

print("Statistical Summary:") 
print(df.describe())

print("Missing Values in Each Column:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
print("Missing Values After Filling Age:")
print(df.isnull().sum())

print("checking for the duplicate values")
print(df.nunique())

# 1.Overall Survival Count

plt.figure(figsize=(6,4))
sns.countplot(x='Survived', data=df, palette='viridis') 

plt.title("Overall Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()


# 2.Survival by Gender

plt.figure(figsize=(6,4))
sns.countplot(x='Sex', hue='Survived', data=df, palette='Set2') 

plt.title("Survival by Gender", fontsize=14)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)
plt.show()

# 3.Survival by Passenger Class

plt.figure(figsize=(6,4))
sns.countplot(x='Pclass', hue='Survived', data=df, palette="RdPu", edgecolor="0.2")

plt.title("Survival by Passenger Class", fontsize=14, fontweight='bold', color='#ad1457')
plt.xlabel("Passenger Class", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.legend(title='Survived', labels=['No', 'Yes'])

plt.show()

# 4.Age Distribution

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=30, kde=True, color='maroon') 
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 5.Age vs Survival
plt.figure(figsize=(6,4))
sns.boxplot(x='Survived', y='Age', data=df, color='darkslateblue')
plt.title("Age vs Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()


# 6.Fare Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Fare'], bins=40, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

#7. Fare vs Survival
plt.figure(figsize=(6,4)) 
sns.boxplot(x='Survived', y='Fare', data=df, color='slategray')
plt.title("Fare vs Survival") 
plt.xlabel("Survived") 
plt.ylabel("Fare") 
plt.show()

# 8.Correlation Heatmap
colors = ["#A0522D", "grey"] 
sns.catplot(x="Pclass", hue="Survived", col="Sex", data=df, kind="count", height=4, aspect=1, palette=colors)
plt.show()


# 9. Pair Plot
sns.pairplot(df[['Survived','Age','Fare','Pclass']], hue='Survived')
plt.show()

# 10.swarm plot

plt.figure(figsize=(7,5))
sns.swarmplot(x='Survived', y='Age', data=df)
plt.title("Individual Age Distribution vs Survival")
plt.show()

# 11.kernel density plot
plt.figure(figsize=(8,5))
sns.kdeplot(df[df['Survived']==1]['Fare'], label='Survived', shade=True)
sns.kdeplot(df[df['Survived']==0]['Fare'], label='Not Survived', shade=True)
plt.title("Fare Density by Survival")
plt.legend()
plt.show()

# 12.Violin Plot
plt.figure(figsize=(6,4))
sns.violinplot(x='Survived', y='Age', data=df)
plt.title("Age Distribution vs Survival")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Age")
plt.show()



