# Project: Prompting Debug Assistant - Bug Descriptions

## Bug 1 – bug1.py (Python)
**Intended Behavior**: Funksiya sensor məlumatlarını qəbul etməli, mənfi yükləri kənarlaşdırmalı və qalan temperaturların ortalamasını hesablamalıdır.
**Issue Type**: Logical Error, Off-by-one, Runtime Exception.
**Notes**: 
- `if readings[i] < 0` şərti müsbət rəqəmlər yerinə səhvən mənfi rəqəmləri seçir.
- `range(0, len(valid_readings) - 1)` sonuncu indeksi hesablamadan kənarda qoyur.
- Əgər siyahıda müsbət ədəd yoxdursa, `total / len(valid_readings)` sıfıra bölmə xətası törədir.

## Bug 2 – bug2.js (JavaScript)
**Intended Behavior**: İstifadəçi qeydiyyatı zamanı yaş, şifrə uzunluğu və istifadəçi rolunu doğrulamalıdır.
**Issue Type**: Syntax Error, Reference Error, Logical Error.
**Notes**:
- `if (user.age < 18 {` hissəsində mötərizə bağlanmayıb (Syntax).
- `minLenght` dəyişəni `minLength` yerinə səhv yazılıb (Reference).
- `if (user.role = "admin")` sətri yoxlama deyil, mənimsətmə edir, nəticədə şərt həmişə doğru olur.

## Bug 3 – bug3.cpp (C++)
**Intended Behavior**: Tam ədədlərdən ibarət massivdə ən böyük (maximum) elementi tapıb ekrana çap etməlidir.
**Issue Type**: Logical Error, Runtime Error (Out of Bounds), Syntax Error.
**Notes**:
- `max_val` başlanğıc olaraq çox böyük rəqəm götürüldüyü üçün massivdəki ədədlər ondan böyük ola bilmir.
- `i <= n` dövrü massivin 5-ci indeksinə (hansı ki yoxdur) müraciət edir.
- `cout` sətrinin sonunda nöqtəli vergül (`;`) çatışmır.

## Bug 4 – bug4.java (Java)
**Intended Behavior**: Mağaza inventarındakı məhsulları dövr edərək, tükənənləri qeyd etməli və adlarını böyük hərflə çap etməlidir.
**Issue Type**: Logical Error (Empty If), Runtime Error (Array Index Out of Bounds).
**Notes**:
- `if (counts[i] == 0);` sətrindəki nöqtəli vergül şərt blokunu dərhal bitirir, nəticədə altındakı kod şərtə baxmadan həmişə işləyir.
- `items[i+1]` müraciəti sonuncu elementdə massivin hüdudlarından kənara çıxır.
