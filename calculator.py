import streamlit as st
import math

# Set up the title for the calculator
st.title("Scientific Calculator")

# Display input fields
st.write("Enter your values below:")

# Input fields for the calculator
num1 = st.number_input("Enter first number:", value=0.0)
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Power", "Sin", "Cos", "Tan", "Log"])
num2 = None

# Conditionally render a second input field if the operation requires two numbers
if operation not in ["Square Root", "Sin", "Cos", "Tan", "Log"]:
    num2 = st.number_input("Enter second number (if applicable):", value=0.0)

# Calculate the result based on the operation selected
result = None

if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Power":
        result = math.pow(num1, num2)
    elif operation == "Sin":
        result = math.sin(math.radians(num1))  # Convert to radians
    elif operation == "Cos":
        result = math.cos(math.radians(num1))  # Convert to radians
    elif operation == "Tan":
        result = math.tan(math.radians(num1))  # Convert to radians
    elif operation == "Log":
        if num1 > 0:
            result = math.log(num1)
        else:
            result = "Error! Logarithm only defined for positive numbers."

    # Display the result
    st.write(f"Result: {result}")
