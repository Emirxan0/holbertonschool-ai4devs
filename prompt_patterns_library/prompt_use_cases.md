# Prompt Use Cases

## Code Quality (Kod Keyfiyyəti)
### **Refactoring**
* **Goal**: Mövcud kodun oxunaqlılığını və performansını artırmaq.
* **Input**: Python və ya JavaScript dilində yazılmış funksiya.
* **Output**: Optimallaşdırılmış kod və dəyişikliklərin izahı.

### **Style Enforcement**
* **Goal**: Layihə boyu vahid adlandırma və formatlaşdırma standartlarını təmin etmək.
* **Input**: Kod bloku.
* **Output**: Müəyyən edilmiş stil qaydalarına (məsələn, PEP 8) uyğun yenidən yazılmış kod.

## Debugging (Xətaların Aradan Qaldırılması)
### **Error Identification**
* **Goal**: Sintaksis və ya işləmə zamanı (runtime) yaranan xətaların kökünü tapmaq.
* **Input**: Kod parçası və xəta mesajı (stack trace).
* **Output**: Xətanın müəyyən edilməsi və həll təklifi.

### **Log Analysis**
* **Goal**: Böyük loq fayllarından mənalı xəta modellərini çıxarmaq.
* **Input**: Xam loq (raw log) faylı.
* **Output**: Təkrarlanan xətaların və ya performans darboğazlarının xülasəsi.

## Documentation (Sənədləşdirmə)
### **Docstring Generation**
* **Goal**: Funksiya və klaslar üçün aydın sənədləşmə yaratmaq.
* **Input**: Funksiyanın gövdəsi.
* **Output**: Standartlaşdırılmış docstring-lər (məsələn, JSDoc və ya Google stili).

### **README Creation**
* **Goal**: Peşəkar layihə təsviri və quraşdırma təlimatı hazırlamaq.
* **Input**: Layihənin xüsusiyyətləri və fayl siyahısı.
* **Output**: Strukturlaşdırılmış README.md faylı.

### **API Documentation**
* **Goal**: API son nöqtələrini (endpoints) və cavab formatlarını sənədləşdirmək.
* **Input**: Server tərəfindəki marşrut (route) tərifləri.
* **Output**: Rəsmi API sənədləşməsi (Swagger/OpenAPI stili).

## Testing (Testləşdirmə)
### **Unit Test Generation**
* **Goal**: Kodun fərdi hissələri üçün testlər yaratmaq.
* **Input**: Funksiya və ya klas tərifi.
* **Output**: Pytest və ya Jest kimi çərçivələrdə yazılmış test dəsti.

### **Edge Case Discovery**
* **Goal**: Proqramı sıradan çıxara biləcək kənar vəziyyətləri tapmaq.
* **Input**: Kodun məntiqi təsviri.
* **Output**: Test edilməsi vacib olan sərhəd vəziyyətlərinin siyahısı.

### **Integration Testing**
* **Goal**: Müxtəlif modulların bir-biri ilə düzgün işlədiyini yoxlamaq.
* **Input**: İki qarşılıqlı əlaqədə olan komponentin təsviri.
* **Output**: İnteqrasiya testi üçün ardıcıl addımlar.
