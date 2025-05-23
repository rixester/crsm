import { NextResponse } from 'next/server';

export function middleware(request) {
  const path = request.nextUrl.pathname;
  
  // Protege todas as rotas /protected
  if (path.startsWith('/protected')) {
    const token = request.cookies.get('authToken');
    
    if (!token) {
      return NextResponse.redirect(new URL('/login', request.url));
    }
    
    // Verificação adicional do token pode ser feita aqui
  }
  
  return NextResponse.next();
}
