import qrcode

# Data to encode in the QR code
data = input("Paste the link here: ")

# Creates a QR code instance
qr = qrcode.QRCode(
    version=1,  # Size of the QR code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box
    border=4,  # Thickness of the border
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("qrcode_output.png")

print("QR code generated successfully!")
