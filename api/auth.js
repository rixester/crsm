export default async function handler(req, res) {
  // Configura cabeçalhos CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method === 'POST') {
    const { username, password } = req.body;
    
    if (username === process.env.ADMIN_USER && 
        password === process.env.ADMIN_PASS) {
      return res.status(200).json({ 
        success: true,
        token: 'seu-token-gerado-aqui' 
      });
    }
    
    return res.status(401).json({ error: 'Credenciais inválidas' });
  }
  
  return res.status(405).json({ error: 'Método não permitido' });
}
