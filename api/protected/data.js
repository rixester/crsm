export default async function handler(req, res) {
  // Verifica o token
  const authHeader = req.headers.authorization;
  
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Não autorizado' });
  }

  const token = authHeader.split(' ')[1];
  const validTokens = process.env.AUTH_TOKENS?.split(',') || [];

  if (!validTokens.includes(token)) {
    return res.status(401).json({ error: 'Token inválido' });
  }

  // Se chegou aqui, está autenticado - retorna os dados protegidos
  try {
    // Aqui você pode conectar a sua planilha ou banco de dados
    // Exemplo simplificado:
    const protectedData = {
      portos: "dados dos portos",
      areas: "dados das áreas",
      casos: "dados dos casos"
    };

    return res.status(200).json(protectedData);
  } catch (error) {
    return res.status(500).json({ error: 'Erro ao buscar dados' });
  }
}
