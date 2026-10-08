class Rectangle:
    def __init__(self, length, width):
        # Validasi: Nilai input tidak boleh 0 atau kurang dari 0 (menggunakan raise ValueError)
        if length <= 0 or width <= 0:
            raise ValueError("Panjang dan lebar harus lebih besar dari 0.")
        
        self.length = length
        self.width = width

    