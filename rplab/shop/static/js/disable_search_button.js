document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const searchButton = document.getElementById('search-button');

    if (searchInput && searchButton) {
        searchInput.addEventListener('input', function () {
            if (searchInput.value.trim() === '') {
                searchButton.disabled = true;  // Disabilita il pulsante se la barra è vuota
            } else {
                searchButton.disabled = false;  // Abilita il pulsante se c'è almeno un carattere
            }
        });
    } else {
        console.error("Elemento non trovato: assicurati che gli ID siano corretti.");
    }
});

