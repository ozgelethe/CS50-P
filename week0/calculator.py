# x = input("whats x? ")
# y = input("whats y? ")

# z = int(x) + int(y)

# print(z)

# x = int(input("whats x? "))
# y = int(input("whats y? "))

# virgülden sonnrasını yazabilmesi için float kullanıyoruz

#x = float(input("whats x? "))
#y = float(input("whats y? "))

#print(x + y)

# eğer float sonucumuzu integera yuvarlamak istiyorsak;
# z = round(x + y)
# print(z)

# sonucu, z'yi üçerli basamaklara virgülle ayırmak istiyorsak;
# print(f"{z:,}")

# sonuçta virgülden sonra kaç birim olacağını belirlemek istiyorsak;
# z = round(x / y, 2)
# print(z)

# ya da, daha az kullanılır
# z = x / y
# print (f"{:.2f}")

def main():
    x = int(input("whats x? "))
    print("x squared is,", square(x))

def square(n):
    return n * n
    # ya da n'in 2. kuvvetini almak için
    # return pow(n, 2)

main()