var elements = document.querySelectorAll('.desc');  // Seleziona tutti gli elementi con la classe 'desc'

elements.forEach(function(p) {
  var textContent = p.textContent;  // Ottieni il contenuto

  // Verifica la lunghezza del testo e aggiungi i puntini di sospensione se supera i 150 caratteri
  if (textContent.length > 150) {
    p.textContent = textContent.substring(0, 150) + '...';
  }
});