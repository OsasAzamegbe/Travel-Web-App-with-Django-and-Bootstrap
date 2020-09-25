const spanMap = (favButton) => favButton.nextElementSibling;
const currentFavoritesMap = (sp) => parseInt(sp.textContent.split(" ")[0]);
const urlMap = (favButton) => favButton.getAttribute('data-favorite-url');

const favButtons = document.querySelectorAll('.favorite-button');
const span = Array.from(favButtons, spanMap);
let currentFavorites = Array.from(span, currentFavoritesMap);
let STATE = new Array(favButtons.length).fill(false);
const url = Array.from(favButtons, urlMap);


const likedIcon = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="red" width="18px" height="18px"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>`
const unlikedIcon = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="black" width="18px" height="18px"><path d="M0 0h24v24H0z" fill="none"/><path d="M16.5 3c-1.74 0-3.41.81-4.5 2.09C10.91 3.81 9.24 3 7.5 3 4.42 3 2 5.42 2 8.5c0 3.78 3.4 6.86 8.55 11.54L12 21.35l1.45-1.32C18.6 15.36 22 12.28 22 8.5 22 5.42 19.58 3 16.5 3zm-4.4 15.55l-.1.1-.1-.1C7.14 14.24 4 11.39 4 8.5 4 6.5 5.5 5 7.5 5c1.54 0 3.04.99 3.57 2.36h1.87C13.46 5.99 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5 0 2.89-3.14 5.74-7.9 10.05z"/></svg>`


const toggleLike = (favorites, index, favButton) => {
    STATE[index] = !STATE[index]
    favButton.classList.toggle('liked')
    if (favButton.classList.contains('liked')) {
        favButton.innerHTML = likedIcon
        favorites ++
    } else{
        favButton.innerHTML = unlikedIcon
        favorites --
    }
    currentFavorites[index] = favorites
    span[index].textContent = `${favorites} favorites`
}

const sendRequest = async (index, favButton) => {
    if (STATE[index]){
        STATE[index] = false
        const response = await fetch(url[index]);
        const data = await response.json();
        if (!response.ok){
            const favorites = parseInt(span[index].textContent.split(" ")[0])
            toggleLike(favorites, index, favButton)

        }
        else{
            span[index].textContent = `${data.number_of_favorites} favorites`
        }
    }
}

[].slice.call(favButtons).forEach((favButton, index) => {favButton.addEventListener('click', (e) => {
    e.preventDefault();
    toggleLike(currentFavorites[index], index, favButton);
    window.setTimeout(() => {sendRequest(index, favButton)}, 500);
});
});