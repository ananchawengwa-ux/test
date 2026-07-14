def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 1) + 1):
        if n % i == 0:
            return False
    return True

for num in range(1, 21):
    if is_prime(num):
        print(num, "เป็นจำนวนเฉพาะ")
  
