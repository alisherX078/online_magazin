document.addEventListener('DOMContentLoaded', () => {
    console.log('Сайт загружен 👍');

    // Пример: сообщение при добавлении в корзину
    const cartButtons = document.querySelectorAll('.add-to-cart');
    cartButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            alert('Товар добавлен в корзину!');
        });
    });
});
