import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class StudentSalesAnalyze:

    def __init__(self):
        self.df = None
        self.last_plot = None

    def __del__(self):
        pass

    # --------LOAD dataset ----------
    def load_dataset(self):
        print("\n--- Dataset Loading ---")
        file_path = input("Enter CSV file path: ")
        try:
            self.df = pd.read_csv(file_path)
            print("CSV loaded successfully.")
        except Exception as e:
            print("Failed to load file:", e)

    # ---------- explore DATA ----------
    def explore_data(self):
        if self.df is None:
            print("Dataset not loaded.")
            return

        while True:
            print("\n======= Explore Data ===========")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Go Back")

            ch = input("Enter your choice: ")

            if ch == "1":
                print(self.df.head())
            elif ch == "2":
                print(self.df.tail())
            elif ch == "3":
                print(list(self.df.columns))
            elif ch == "4":
                print(list(self.df.dtypes))
            elif ch == "5":
                 self.df.info()
            elif ch =="6":
                break
            else:
                print("Invalid Option")                

    # ---------- MISSING VALUES ----------
    def handle_missing_data(self):
        if self.df is None:
            print("Load data first.")
            return

        while True:
            print("\n======== Handle missing data ==========")
            print("1. Display rows with missing values")
            print("2. Fill Missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back")

            ch = input("Enter your choice: ")

            if ch == "1":
                rows = self.df[self.df.isnull().any(axis=1)]
                if rows.empty:
                    print("No missing values found.")
                else:
                    print(rows)

            elif ch == "2":
                self.df.fillna(self.df.mean(numeric_only=True), inplace=True)
                print("Filled using mean.")

            elif ch == "3":
                self.df.dropna(inplace=True)
                print("Rows deleted.")

            elif ch == "4":
                value = input("Enter value to replace missing values: ")
                try:    
                    value = float(value)
                except:
                  pass
                self.df.fillna(value, inplace=True)
                print("Missing values replaced.")

            elif ch == "5":
                break
            else:
                print("Invalid Option")

    
         # ---------- NUMPY CALCULATIONS ----------
    def numeric_analysis(self):
        if self.df is None:
            print("Dataset not loaded.")
            return

        col = input("Enter numeric column: ")

        if col in self.df.columns and np.issubdtype(self.df[col].dtype, np.number):
            arr = self.df[col].to_numpy()
            print("Array:", arr)
            print("Total:", np.sum(arr))
            print("Average:", np.mean(arr))
            print("Highest:", np.max(arr))
            print("Lowest:", np.min(arr))
        else:
            print("Invalid numeric column.")

    # ---------- DATA SPLIT / MERGE ----------
    def dataframe_operations(self):
        if self.df is None:
            print("Load dataset first.")
            return

        while True:
            print("\n--- DataFrame Tools ---")
            print("1. Merge another dataset")
            print("2. Split dataset")
            print("3. Back")

            ch = input("Choice: ")

            if ch == "1":
                path = input("Enter second CSV path: ")
                try:
                    df2 = pd.read_csv(path)
                    merged = pd.concat([self.df, df2], ignore_index=True)
                    print("Merged Data Preview:")
                    print(merged.head())
                except:
                    print("Merge failed.")

            elif ch == "2":
                try:
                    mid = len(self.df) // 2
                    part1 = self.df.iloc[:mid]
                    part2 = self.df.iloc[mid:]
                    print("Part 1:")
                    print(part1.head())
                    print("\nPart 2:")
                    print(part2.head())
                except:
                    print("Split error.")

            elif ch == "3":
                break
            else:
                print("Invalid option")

    # ---------- STATISTICS ----------
    def descriptive_stats(self):
        if self.df is None:
            print("Load data first.")
            return

        print("\n--- Statistical Report ---")
        print(self.df.describe())
        print("\nStd Deviation:\n", self.df.std(numeric_only=True))
        print("\nVariance:\n", self.df.var(numeric_only=True))

    # ---------- VISUALS ----------
    def visualize_data(self):
        if self.df is None:
            print("Dataset missing.")
            return

        while True:
            print("\n--- Chart Menu ---")
            print("1. Column Bar Chart")
            print("2. Trend Line")
            print("3. Scatter Diagram")
            print("4. Sales Distribution")
            print("5. Correlation Heatmap")
            print("6. Histogram")
            print("7. Stack plot")
            print("8. Back")

            ch = input("Choice: ")
            plt.figure(figsize=(6, 4))

            if ch == "1":
                plt.bar(self.df.iloc[:, 1], self.df.iloc[:, 3])
                plt.title("Bar Chart")

            elif ch == "2":
                plt.plot(self.df.iloc[:, 3])
                plt.title("Line Chart")

            elif ch == "3":
                x = input("X column: ")
                y = input("Y column: ")

                if x in self.df.columns and y in self.df.columns:
            
                 plt.scatter(self.df[x], self.df[y])
                 plt.title("Scatter Plot")
                else:
                    print("Invalid colimn name")
                    plt.close()
                    continue

            elif ch == "4":
                self.df.groupby(self.df.columns[2])[self.df.columns[3]].sum().plot.pie(
                 autopct="%1.1f%%")
    
                plt.title("Sales Distribution")

            elif ch == "5":
                sns.heatmap(self.df.corr(numeric_only=True), annot=True)
                plt.title("Heatmap")

            elif ch == "6":
                plt.hist(self.df.iloc[:, 3], bins=6)
                plt.title("Histogram")

            elif ch == "7":
                plt.stackplot(self.df.index, self.df.iloc[:,3])
                plt.title("Stack Plot")

            elif ch == "8":
                plt.close()
                break

            else:
                print("Wrong Option")
                plt.close()
                continue

            self.last_plot = plt.gcf()
            plt.show()

    # ---------- SAVE IMAGE ----------
    def save_visualization(self):
        if self.last_plot is None:
            print("No chart to save.")
            return

        name = input("Enter image filename: ")
        self.last_plot.savefig(name)
        print("Image saved successfully.")


# ================= MAIN =================
analyzer = StudentSalesAnalyze()

while True:
    print("\n========== Data Analysis & Visualization Program ==========")
    print("Please select an option:")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("===========================================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        analyzer.load_dataset()
    elif choice == "2":
        analyzer.explore_data()
    elif choice == "3":
        analyzer.dataframe_operations()
    elif choice == "4":
        analyzer.handle_missing_data()
    elif choice == "5":
        analyzer.descriptive_stats()
    elif choice == "6":
        analyzer.visualize_data()
    elif choice == "7":
        analyzer.save_visualization()
    elif choice == "8":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")