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
    var links = document.querySelectorAll('.nav-links a, .nav-mobile a');
    links.forEach(function (link) {
        var href = (link.getAttribute('href') || '').replace(/\/$/, '') || '/';
        if (href === path) {
            link.classList.add('active');
        }
        if (path.indexOf('/blog/') === 0 && href === '/blog') {
            link.classList.add('active');
        }
    });
})();
