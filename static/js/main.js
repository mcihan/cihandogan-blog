// Mobile menu toggle
(function () {
    var toggle = document.querySelector('.nav-toggle');
    var menu = document.querySelector('.nav-mobile');
    if (!toggle || !menu) return;

    toggle.addEventListener('click', function () {
        var expanded = toggle.getAttribute('aria-expanded') === 'true';
        toggle.setAttribute('aria-expanded', String(!expanded));
        menu.classList.toggle('open');
    });
})();

// Active nav link highlighting
(function () {
    var path = window.location.pathname.replace(/\/$/, '') || '/';
    var filename = path.split('/').pop() || 'index.html';
    if (filename === '') filename = 'index.html';

    var links = document.querySelectorAll('.nav-links a, .nav-mobile a');
    links.forEach(function (link) {
        var href = link.getAttribute('href');
        if (!href) return;
        var linkFile = href.split('/').pop() || 'index.html';
        if (linkFile === filename || (filename === 'index.html' && (linkFile === '/' || linkFile === ''))) {
            link.classList.add('active');
        }
        // Mark Articles as active for individual article pages
        if (path.indexOf('/articles/') !== -1 && linkFile === 'blog.html') {
            link.classList.add('active');
        }
    });
})();
