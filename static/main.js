document.addEventListener('DOMContentLoaded', () => {
    // 1. Clock functionality
    const timeDisplay = document.getElementById('current-time');
    
    function updateTime() {
        const now = new Date();
        const timeString = now.toLocaleTimeString('en-US', {
            hour12: false,
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        });
        timeDisplay.textContent = timeString;
    }
    
    setInterval(updateTime, 1000);
    updateTime(); // initial call

    // 2. Search & Filter functionality
    const searchTitle = document.getElementById('search-title');
    const searchSpeaker = document.getElementById('search-speaker');
    const searchCategory = document.getElementById('search-category');
    const scheduleItems = document.querySelectorAll('.schedule-item.talk');
    const noResults = document.getElementById('no-results');

    function filterSchedule() {
        const titleQuery = searchTitle.value.toLowerCase().trim();
        const speakerQuery = searchSpeaker.value.toLowerCase().trim();
        const categoryQuery = searchCategory.value;

        let visibleCount = 0;

        scheduleItems.forEach(item => {
            const itemTitle = item.getAttribute('data-title') || '';
            const itemSpeakers = item.getAttribute('data-speakers') || '';
            const itemCategory = item.getAttribute('data-category') || '';

            const matchesTitle = titleQuery === '' || itemTitle.includes(titleQuery);
            const matchesSpeaker = speakerQuery === '' || itemSpeakers.includes(speakerQuery);
            const matchesCategory = categoryQuery === '' || itemCategory === categoryQuery;

            if (matchesTitle && matchesSpeaker && matchesCategory) {
                item.style.display = 'flex';
                // Remove inline animation to restart if needed, or just let it be
                item.style.animation = 'none';
                item.offsetHeight; // trigger reflow
                item.style.animation = null;
                visibleCount++;
            } else {
                item.style.display = 'none';
            }
        });

        // The break is usually shown unless user is filtering
        const breakItems = document.querySelectorAll('.schedule-item.break');
        if (titleQuery !== '' || speakerQuery !== '' || categoryQuery !== '') {
            breakItems.forEach(item => item.style.display = 'none');
        } else {
            breakItems.forEach(item => {
                item.style.display = 'flex';
                visibleCount++;
            });
        }

        if (visibleCount === 0) {
            noResults.style.display = 'block';
        } else {
            noResults.style.display = 'none';
        }
    }

    searchTitle.addEventListener('input', filterSchedule);
    searchSpeaker.addEventListener('input', filterSchedule);
    searchCategory.addEventListener('change', filterSchedule);
});