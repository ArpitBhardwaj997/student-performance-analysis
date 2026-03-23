import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="student",          
    user="postgres",
    password="@rpit",  
    host="localhost",
    port="5432"
)

# Fetch data from SQL
query = "SELECT * FROM students"
df = pd.read_sql(query, conn)

# Data cleaning
df.dropna(inplace=True)

# Create Average column
df["Average"] = ((df["math"] + df["science"] + df["english"]) / 3).round(2)

# Print data
print("\nFinal Data:\n")
print(df)

# Save output
df.to_csv("output.csv", index=False)

# Top performer
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Performer:\n", top_student)

# Visualization
df.plot(x="name", y=["math", "science", "english"], kind="bar")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Close connection
conn.close()