/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: false,
  serverExternalPackages: ['puppeteer-core'],
  async rewrites() {
    const backendUrl = process.env.BACKEND_URL || 'http://backend:8000'
    return [
      // session
      { source: '/api/session/:token', destination: `${backendUrl}/api/session/:token/` },
      { source: '/api/session/:token/', destination: `${backendUrl}/api/session/:token/` },
      // submit
      { source: '/api/submit/:token', destination: `${backendUrl}/api/submit/:token/` },
      { source: '/api/submit/:token/', destination: `${backendUrl}/api/submit/:token/` },
      // pdf (klassisch)
      { source: '/api/pdf/:token', destination: `${backendUrl}/api/pdf/:token/` },
      { source: '/api/pdf/:token/', destination: `${backendUrl}/api/pdf/:token/` },
      // answers (für Puppeteer print-page)
      { source: '/api/answers/:token', destination: `${backendUrl}/api/answers/:token/` },
      { source: '/api/answers/:token/', destination: `${backendUrl}/api/answers/:token/` },
      // admin
      { source: '/api/admin/sessions', destination: `${backendUrl}/api/admin/sessions/` },
      { source: '/api/admin/sessions/', destination: `${backendUrl}/api/admin/sessions/` },
      { source: '/api/admin/sessions/:token/resend', destination: `${backendUrl}/api/admin/sessions/:token/resend/` },
      { source: '/api/admin/sessions/:token/resend/', destination: `${backendUrl}/api/admin/sessions/:token/resend/` },
      { source: '/api/admin/sessions/:token/delete', destination: `${backendUrl}/api/admin/sessions/:token/delete/` },
      { source: '/api/admin/sessions/:token/delete/', destination: `${backendUrl}/api/admin/sessions/:token/delete/` },
      { source: '/api/admin/sessions/:token/update', destination: `${backendUrl}/api/admin/sessions/:token/update/` },
      { source: '/api/admin/sessions/:token/update/', destination: `${backendUrl}/api/admin/sessions/:token/update/` },
      // gdt
      { source: '/api/gdt/session', destination: `${backendUrl}/api/gdt/session/` },
      { source: '/api/gdt/session/', destination: `${backendUrl}/api/gdt/session/` },
      { source: '/api/gdt/result/:token', destination: `${backendUrl}/api/gdt/result/:token/` },
      { source: '/api/gdt/result/:token/', destination: `${backendUrl}/api/gdt/result/:token/` },
    ]
  },
}

module.exports = nextConfig
