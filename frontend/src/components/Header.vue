<template>
    <header class="app-header">
      <div class="header-content">
        <div class="titles">
          <h1 class="main-title">Universidad Internacional de La Rioja</h1>
          <h2 class="subtitle">Sistema de Detección Temprana de Diabetes</h2>
        </div>
        <img 
          src="@/assets/logo_unir.png" 
          alt="Logo UNIR" 
          class="logo"
        >
      </div>
    </header>
  </template>
  
  <style scoped>
  .app-header {
    background: white;
    padding: 0.8rem 2rem;
    border-bottom: 1px solid #e0e0e0;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }
  
  .header-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.5rem;
  }
  
  .logo {
    height: 50px;
    width: auto;
    order: 2; /* Posiciona el logo al final (derecha) */
  }
  
  .titles {
    line-height: 1.3;
    order: 1;
  }
  
  .main-title {
    font-size: 1.3rem;
    color: #003366; /* Azul UNIR */
    margin: 0;
    font-weight: 700;
  }
  
  .subtitle {
    font-size: 0.95rem;
    color: #666;
    margin: 0;
    font-weight: 400;
    font-style: italic;
  }
  
  /* Versión responsive para móviles */
  @media (max-width: 768px) {
    .header-content {
      flex-direction: column;
      text-align: center;
      gap: 0.5rem;
    }
    
    .logo {
      order: 0;
      height: 40px;
    }
    
    .main-title {
      font-size: 1.1rem;
    }
    
    .subtitle {
      font-size: 0.85rem;
    }
  }
  </style>