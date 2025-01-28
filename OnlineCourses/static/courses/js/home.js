
document.addEventListener('DOMContentLoaded', function() {
    // Number animation configuration
    const animationDuration = 3000; // 2 seconds
    const statsSection = document.querySelector('.stats-section');
    const statNumbers = document.querySelectorAll('.stat-number');

    // Only animate once
    let animated = false;

    const animateNumbers = () => {
        if (animated) return;
        animated = true;

        statNumbers.forEach(element => {
            const originalText = element.textContent;
            const suffix = originalText.replace(/\d+/g, ''); // Get + or % if exists
            const target = parseInt(originalText) || 0;
            let current = 0;

            const increment = target / (animationDuration / 16); // ~60fps

            const updateNumber = () => {
                current = Math.min(target, current + increment);
                element.textContent = `${Math.floor(current)}${suffix}`;

                if (current < target) {
                    requestAnimationFrame(updateNumber);
                }
            };

            requestAnimationFrame(updateNumber);
        });
    };

    // Intersection Observer to trigger animation
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateNumbers();
                observer.unobserve(statsSection);
            }
        });
    }, { threshold: 0.5 }); // Trigger when 50% visible

    observer.observe(statsSection);
});