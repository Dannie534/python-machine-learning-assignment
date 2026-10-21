# importing libraries
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#features
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
#target variables
y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]
# creating a linear regression model
model = LinearRegression()
# fitting the model
model.fit(X, y)
#  Allow the user to enter the number of hours studied using input()
user_input = input("Enter hours studied: ")
# Convert the user input to a float
hours_studied = float(user_input)
# Predicting the score based on user input
predicted_score = model.predict([[hours_studied]])
# Displaying the predicted score
print(f"Predicted score for {hours_studied} hours studied: {predicted_score[0]:.2f}")

# visualizing the results
print("\nGenerating relationship graph...")
study_hours = [row[0] for row in X]
# plotting the data points
plt.scatter(study_hours, y, color='blue', label='Actual Scores')
# plotting the regression line
plt.plot(study_hours, model.predict(X), color='red', label='Regression Line')
# adding labels and title
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Hours Studied vs. Exam Scores')
plt.legend()
plt.grid(True)
plt.show()
