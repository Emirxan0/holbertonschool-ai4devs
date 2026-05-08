def process_user_data(data):
    """
    Bu funksiya istifadəçi ballarını emal etməli və ortalamanı tapmalıdır.
    Lakin boş siyahı gəldikdə və ya yanlış indeksləmədə səhv verir.
    """
    print("Məlumatlar emal olunur...")
    
    total_score = 0
    count = 0
    
    # Məntiqi xəta: Siyahını gəzərkən diapazonu səhv hesablayır
    for i in range(len(data) + 1): 
        current_val = data[i] # Burada IndexError baş verəcək (Off-by-one)
        total_score += current_val
        count += 1
        
    average = total_score / count # Siyahı boşdursa ZeroDivisionError verəcək
    
    print(f"Ümumi bal: {total_score}")
    return average

# Test nümunələri
test_list = [85, 90, 78, 92]
# Bu sətir xəta verəcək
result = process_user_data(test_list)
print(f"Nəticə: {result}")
