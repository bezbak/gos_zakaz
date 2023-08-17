// $('.news_slider').slick();
$(document).ready(function() {
    $('.news_slider').slick({
        dots: false,
        arrows: true,
        infinite: false,
        speed: 300,
        slidesToShow: 1,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 1,
                }
            }
        ]
    });

    const modalOverlay = document.querySelector('.modal-overlay');
    const modalImage = document.querySelector('.modal-image');
    const closeBtn = document.querySelector('.close-btn');

    $('.slider-item').on('click', function() {
        const imgSrc = $(this).find('img').attr('src');
        modalImage.setAttribute('src', imgSrc);
        modalOverlay.style.display = 'flex';
    });

    $(closeBtn).on('click', function() {
        modalOverlay.style.display = 'none';
    });
});
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        // Здесь выполняйте действия при нажатии клавиши "Esc"
        // Например, закрытие модального окна
        closeModal();
    }
});

function closeModal() {
    // Ваш код для закрытия модального окна
    // Например:
    const modalOverlay = document.querySelector('.modal-overlay');
    modalOverlay.style.display = 'none';
}
