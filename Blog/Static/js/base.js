const themeSlider = document.querySelector('.slider');
const navBar = document.querySelector('.navbar-nav');
themeSlider.addEventListener('click', function(e) {
    // e.preventDefault();
    
    document.body.classList.toggle('dark');
    if(navBar.classList.contains('navbar-light')) {
        document.nav.classList.toggle('navbar-light');
        navBar.classList.remove('navbar-light');
        navBar.classList.add('navbar-dark');
    
    } else if(navBar.classList.contains('navbar-dark')) {
        navBar.classList.remove('navbar-dark');
        navBar.classList.add('navbar-light');
    }
});