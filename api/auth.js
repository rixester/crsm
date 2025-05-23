export default async function handler(req, res) {
  if (req.method === 'POST') {
    const { username, password } = req.body;
    
    // Verifica credenciais (use suas variáveis de ambiente do Vercel)
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
