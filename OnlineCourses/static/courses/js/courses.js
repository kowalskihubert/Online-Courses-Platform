
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const presentationCards = document.querySelectorAll('.presentation-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const subject = this.dataset.subject;

            //DEBUG
            console.log(subject);

            // Update button states
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            // Filter presentations
            presentationCards.forEach(card => {
                const cardSubject = card.dataset.subject;
                if (subject === 'all' || cardSubject === subject) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    });
});