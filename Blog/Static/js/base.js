const themeSlider = document.querySelector('.slider');
themeSlider.addEventListener('click', function(e) {
    // e.preventDefault();
    
    document.body.classList.toggle('dark');
    // if(document.body.classList.contains('dark')) {
    //     document.body.classList.remove('dark');
    
    // } else {
    //     document.body.classList.add('dark');
    // }
});