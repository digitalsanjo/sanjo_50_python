# AreaCalculator.py
"""
Streamlit App: Area Calculator for Circle, Rectangle, and Triangle
Author: [Your Name]
"""

import streamlit as st
import math

# ----------- Area Calculation Functions -----------

def area_circle(radius: float) -> float:
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return math.pi * radius ** 2

def area_rectangle(width: float, height: float) -> float:
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive numbers.")
    return width * height

def area_triangle(base: float, height: float) -> float:
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

# ----------- Streamlit UI -----------

st.set_page_config(page_title="📐 Area Calculator", layout="centered")
st.title("📐 Area Calculator")
st.write("Select a shape and enter dimensions to calculate the area.")

# Shape Selection
shape = st.selectbox("Choose a shape:", ["Circle", "Rectangle", "Triangle"])

# Dynamic Inputs
if shape == "Circle":
    radius = st.number_input("Enter radius:", min_value=0.0, format="%.2f")
elif shape == "Rectangle":
    width = st.number_input("Enter width:", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height:", min_value=0.0, format="%.2f")
elif shape == "Triangle":
    base = st.number_input("Enter base:", min_value=0.0, format="%.2f")
    height = st.number_input("Enter height:", min_value=0.0, format="%.2f")

# Calculate Button
if st.button("Calculate Area"):
    try:
        if shape == "Circle":
            area = area_circle(radius)
        elif shape == "Rectangle":
            area = area_rectangle(width, height)
        elif shape == "Triangle":
            area = area_triangle(base, height)
        
        st.success(f"✅ The area of the {shape.lower()} is: {area:.2f}")
    except ValueError as e:
        st.error(f"❌ {str(e)}")

# Optional Console Test Cases
if __name__ == "__main__":
    print("\n📐 Area Calculation Test Cases:")
    print(f"Circle (r=5): {area_circle(5):.2f}")
    print(f"Rectangle (4x6): {area_rectangle(4, 6):.2f}")
    print(f"Triangle (8x5): {area_triangle(8, 5):.2f}")
