export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Método não permitido' });
  }

  const { username, password } = req.body;

  // Verifica contra variáveis de ambiente
  if (username === process.env.ADMIN_USER && 
      password === process.env.ADMIN_PASS) {
    
    // Gera um token seguro (simplificado - em produção use JWT)
    const token = Buffer.from(`${username}:${Date.now()}`).toString('base64');
    
    // Armazena o token em um "banco de dados" em memória (simplificado)
    // Em produção, use um banco de dados real
    process.env.AUTH_TOKENS = process.env.AUTH_TOKENS 
      ? `${process.env.AUTH_TOKENS},${token}` 
      : token;

    return res.status(200).json({ 
      token,
      user: username
    });
  }

  return res.status(401).json({ error: 'Credenciais inválidas' });
}
