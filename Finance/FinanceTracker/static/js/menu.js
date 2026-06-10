(function() {

    function initMenu() {
        const menuToggle = document.querySelector('.menu-toggle');
        const nav = document.querySelector('.nav');

        if (!menuToggle || !nav) {
            console.error('Бургер или меню не найдены');
            return;
        }

        console.log('Бургер меню инициализировано');


        let overlay = document.querySelector('.menu-overlay');
        if (!overlay) {
            overlay = document.createElement('div');
            overlay.className = 'menu-overlay';
            document.body.appendChild(overlay);
        }


        function openMenu() {
            nav.classList.add('active');
            menuToggle.classList.add('active');
            overlay.classList.add('active');
            document.body.classList.add('menu-open');
            menuToggle.setAttribute('aria-expanded', 'true');
            console.log('Меню открыто');
        }


        function closeMenu() {
            nav.classList.remove('active');
            menuToggle.classList.remove('active');
            overlay.classList.remove('active');
            document.body.classList.remove('menu-open');
            menuToggle.setAttribute('aria-expanded', 'false');
            console.log('Меню закрыто');
        }


        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();

            if (nav.classList.contains('active')) {
                closeMenu();
            } else {
                openMenu();
            }
        });


        const links = nav.querySelectorAll('a');
        links.forEach(function(link) {
            link.addEventListener('click', function() {
                closeMenu();
            });
        });


        overlay.addEventListener('click', function() {
            closeMenu();
        });


        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && nav.classList.contains('active')) {
                closeMenu();
            }
        });


        window.addEventListener('resize', function() {
            if (window.innerWidth > 760 && nav.classList.contains('active')) {
                closeMenu();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMenu);
    } else {
        initMenu();
    }
})();