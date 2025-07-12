# shoppingbill.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def calculate_total(items, tax_percent):
    subtotal = sum(item['price'] * item['quantity'] for item in items)
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

def generate_pdf(items, subtotal, tax_amount, total, tax_percent):
    filename = "Shopping_Bill.pdf"
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 750, "Shopping Bill")

    c.setFont("Helvetica", 12)
    c.drawString(50, 710, "Item")
    c.drawString(200, 710, "Quantity")
    c.drawString(300, 710, "Price")
    c.drawString(400, 710, "Total")

    y = 690
    for item in items:
        item_total = item['price'] * item['quantity']
        c.drawString(50, y, item['name'])
        c.drawString(200, y, str(item['quantity']))
        c.drawString(300, y, f"₹{item['price']:.2f}")
        c.drawString(400, y, f"₹{item_total:.2f}")
        y -= 20

    c.line(50, y, 500, y)
    y -= 20

    c.drawString(300, y, "Subtotal:")
    c.drawString(400, y, f"₹{subtotal:.2f}")
    y -= 20

    c.drawString(300, y, f"Tax ({tax_percent}%):")
    c.drawString(400, y, f"₹{tax_amount:.2f}")
    y -= 20

    c.setFont("Helvetica-Bold", 12)
    c.drawString(300, y, "Total:")
    c.drawString(400, y, f"₹{total:.2f}")

    c.save()
    print(f"\nPDF generated: {filename}")

def main():
    print("Enter details for 3 items:\n")
    items = []
    for i in range(3):
        name = input(f"Item {i+1} Name: ")
        price = float(input(f"Item {i+1} Price (₹): "))
        quantity = int(input(f"Item {i+1} Quantity: "))
        items.append({"name": name, "price": price, "quantity": quantity})

    tax_percent = float(input("\nEnter Tax Percentage: "))

    subtotal, tax_amount, total = calculate_total(items, tax_percent)
    print(f"\nSubtotal: ₹{subtotal:.2f}")
    print(f"Tax: ₹{tax_amount:.2f}")
    print(f"Total: ₹{total:.2f}")

    generate_pdf(items, subtotal, tax_amount, total, tax_percent)

if __name__ == "__main__":
    main()
