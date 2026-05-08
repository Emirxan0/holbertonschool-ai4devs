/* Bu proqram bir mağazadakı endirimləri hesablamalıdır.
   Sintaksis və məntiqi səhvləri var.
*/

function applyDiscount(price, discountRate) {
    console.log("Hesablanır: " + price + " manat");

    if (discountRate > 100 || discountRate < 0) {
        // Sintaksis xətası: dırnaq işarəsi yarımçıq qalıb
        console.log("Xəta: Endirim faizi yanlışdır);
        return;
    }

    // Məntiqi xəta: Endirimi çıxmaq əvəzinə qiymətə əlavə edir
    let finalPrice = price + (price * (discountRate / 100));

    // Dəyişən adında xəta (ReferenceError)
    console.log("Yekun qiymət: " + finalPriceValue); 
    
    return finalPrice;
}

const originalPrice = 200;
const rate = 15;

const result = applyDiscount(originalPrice, rate);
console.log("Nəticə: " + result);
