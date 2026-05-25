import qrcode

# Ask user for input
data = input("Enter text or URL: ")

# Create QR code
qr = qrcode.make(data)

# Save image
qr.save("qr_code.png")

print("QR Code generated successfully!")
