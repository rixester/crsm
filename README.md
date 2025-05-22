# CRSM
<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Card Exemplo</title>
  <style>
    .card {
      width: 300px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.15);
      overflow: hidden;
      cursor: pointer;
      transition: transform 0.1s;
      text-decoration: none;
      color: inherit;
      display: inline-block;
    }
    .card:hover {
      transform: scale(1.02);
      box-shadow: 0 4px 16px rgba(0,0,0,0.22);
    }
    .card-image {
      width: 100%;
      height: 160px;
      object-fit: cover;
      display: block;
    }
    .card-title {
      padding: 16px;
      font-size: 1.2em;
      font-weight: bold;
      background: #fff;
    }
  </style>
</head>
<body>
  <a class="card" href="pagina_destino.html">
     <div class="card-title">Título do Card</div>
    <img class="card-image" src="exemplo.jpg" alt="Imagem do Card">
   
  </a>

  
  <a class="card" href="pagina_destino.html">
     <div class="card-title">Título do Card</div>
    <img class="card-image" src="exemplo.jpg" alt="Imagem do Card">
   
  </a>

  
  <a class="card" href="pagina_destino.html"> 
    <div class="card-title">Título do Card</div>
    <img class="card-image" src="exemplo.jpg" alt="Imagem do Card">
   
  </a>
</body>
</html>
