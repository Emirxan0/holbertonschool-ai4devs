## Bug 1 – bug1.py
**Intended Behavior**: Funksiya sensor məlumatlarını qəbul etməli və yalnız müsbət temperaturların ortalamasını hesablamalıdır.
**Issue Type**: Logical Error, Off-by-one, Runtime Exception.
**Notes**: Şərt operatoru mənfiləri seçir, dövr sonuncu elementi qaçırır və boş siyahıda sıfıra bölmə baş verir.

## Bug 2 – bug2.js
**Intended Behavior**: İstifadəçi qeydiyyatı zamanı yaş həddini, şifrə uzunluğunu və istifadəçi rolunu doğrulamalıdır.
**Issue Type**: Syntax Error, Reference Error, Logical Error.
**Notes**: Mötərizə bağlanmayıb, dəyişən adı yanlışdır və yoxlama əvəzinə mənimsətmə istifadə edilib.

## Bug 3 – bug3.cpp
**Intended Behavior**: Massivdəki ən böyük elementi tapıb çap etməlidir.
**Issue Type**: Logical Error, Runtime Error, Syntax Error.
**Notes**: Max başlanğıc dəyəri yanlışdır, dövr massiv sərhədlərini aşır və nöqtəli vergül çatışmır.

## Bug 4 – bug4.java
**Intended Behavior**: Stokda tükənmiş (0 olan) məhsulları müəyyən edib xəbərdarlıq çap etməlidir.
**Issue Type**: Logical Error, Array Index Out of Bounds.
**Notes**: i <= length şərti massivdən kənara çıxır. If şərtindən dərhal sonra qoyulan nöqtəli vergül məntiqi pozur.
