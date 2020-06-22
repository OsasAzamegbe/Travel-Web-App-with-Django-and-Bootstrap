const themeSlider = document.querySelector('.slider');
const navBar = document.nav;
themeSlider.addEventListener('click', function(e) {
    // e.preventDefault();
    
    document.body.classList.toggle('dark');
    if(navBar.classList.contains('navbar-light')) {
        navBar.classList.remove('navbar-light');
        navBar.classList.add('navbar-dark');
    }
});