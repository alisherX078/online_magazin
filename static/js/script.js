document.addEventListener('DOMContentLoaded', () => {
    console.log('Сайт загружен 👍');

    // Проверяем наличие кнопок на странице
    const cartButtons = document.querySelectorAll('.add-to-cart');
    if (cartButtons.length > 0) {
        cartButtons.forEach(btn => {
            btn.addEventListener('click', (event) => {
                event.preventDefault();  // Отменяем стандартное поведение (например, перезагрузку страницы)

                // Пример использования красивого уведомления (можно использовать любую библиотеку, например, Toast)
                const message = document.createElement('div');
                message.classList.add('toast');
                message.textContent = 'Товар добавлен в корзину!';
                document.body.appendChild(message);

                // Удаляем уведомление через несколько секунд
                setTimeout(() => {
                    message.remove();
                }, 3000);
            });
        });
    }
});
