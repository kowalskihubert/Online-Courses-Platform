
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navCenter = document.querySelector('.nav-center');

    mobileMenuToggle.addEventListener('click', function() {
        // Toggle menu visibility
        navCenter.classList.toggle('active');

        // Animate hamburger icon
        this.classList.toggle('active');
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        if (!event.target.closest('.nav-center') &&
            !event.target.closest('.mobile-menu-toggle')) {
            navCenter.classList.remove('active');
            mobileMenuToggle.classList.remove('active');
        }
    });
});

// For Form Validation in Contact Page
// document.querySelectorAll('.form-input, .form-textarea').forEach(input => {
//     input.addEventListener('input', () => {
//         input.reportValidity()
//         input.parentElement.classList.toggle('invalid', !input.checkValidity())
//     })
// })