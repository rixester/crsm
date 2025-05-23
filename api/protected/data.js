export default async function handler(req, res) {
  // Verifica o token
  const token = req.headers.authorization?.split(' ')[1];
  
  if (token !== 'seu-token-de-acesso') {
    return res.status(401).json({ error: 'Não autorizado' });
  }
  
  // Retorna os dados protegidos
  return res.status(200).json({
    portos: [...],
    areas: [...],
    casos: [...]
  });
}
