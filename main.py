from rectangle import Rectangle

# Menguji program
try:
    # Membuat objek Rectangle dengan panjang 3 cm dan lebar 2 cm
    rect = Rectangle(3, 2)

    # 1. Memanggil fungsi __str__ secara implisit melalui print
    print("Representasi Objek:", rect)

    # 2. Memanggil fungsi keliling (circumference)
    print("Keliling (Circumference):", rect.circumference(), "cm")

    # 3. Memanggil fungsi luas (area)
    print("Luas (Area):", rect.area(), "cm²")

    # Pengujian validasi input <= 0
    print("\n--- Pengujian Validasi Input 0 ---")
    rect_invalid = Rectangle(0, 5)

except ValueError as e:
    print("Error Handling Active:", e)