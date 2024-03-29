import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data_to_encode = input("Enter the data for the QR code: ")
    output_file_name = input("Enter the output file name (e.g., qrcode.png): ")

    generate_qr_code(data_to_encode, output_file_name)
    print(f"QR code saved as {output_file_name}")
