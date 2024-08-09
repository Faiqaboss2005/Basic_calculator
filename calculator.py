import streamlit as st
from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

def main():
    st.title("Simple Calculator")

    # Taking user input using Streamlit's widgets
    num1 = st.number_input("Enter the first number:", format="%.2f")
    num2 = st.number_input("Enter the second number:", format="%.2f")
    operator = st.selectbox("Choose an operator:", ('+', '-', '*', '/'))

    # Perform the calculation based on the selected operator
    if st.button("Calculate"):
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            st.error("Invalid operator selected!")
            return

        st.success(f"The result is: {result}")

if __name__ == "__main__":
    main()
