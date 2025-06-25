fetch('http://localhost:3000/api/imoveis')
  .then(response => response.json())
  .then(data => {
    const lista = document.getElementById('lista-imoveis');
    data.forEach(imovel => {
      const li = document.createElement('li');
      li.textContent = imovel.titulo;
      lista.appendChild(li);
    });
  })
  .catch(err => console.error('Erro ao carregar imóveis:', err));