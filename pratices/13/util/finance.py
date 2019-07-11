

def calculate_with_vat(num):
    with_vat = [a * 1.21 for a in num]
    return sum(with_vat)
