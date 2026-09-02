/** @type {import('next').NextConfig} */
// Hinweis: Änderungen an dieser Datei starten den Dev-Server automatisch neu.
const nextConfig = {
  trailingSlash: false,
  serverExternalPackages: ['puppeteer-core'],
  async rewrites() {
    // Default: lokale Entwicklung. Docker-Compose setzt BACKEND_URL=http://backend:8000 explizit.
    // (Turbopack wertet next.config.js vor .env.local aus - deshalb kein Docker-Hostname als Default.)
    const backendUrl = process.env.BACKEND_URL || 'http://localhost:8000'
    return [
      // session
      { source: '/api/session/:token', destination: `${backendUrl}/api/session/:token/` },
      { source: '/api/session/:token/', destination: `${backendUrl}/api/session/:token/` },
      // submit
      { source: '/api/submit/:token', destination: `${backendUrl}/api/submit/:token/` },
      { source: '/api/submit/:token/', destination: `${backendUrl}/api/submit/:token/` },
      // Hinweis: /api/answers/:token wird bewusst NICHT öffentlich durchgereicht —
      // die Print-Page holt die Daten serverseitig direkt vom Backend.
      // i18n (Sprachdateien für den Patienten-Fragebogen)
      { source: '/api/i18n', destination: `${backendUrl}/api/i18n/` },
      { source: '/api/i18n/:lang', destination: `${backendUrl}/api/i18n/:lang/` },
      { source: '/api/i18n/:lang/', destination: `${backendUrl}/api/i18n/:lang/` },
      // admin
      { source: '/api/admin/templates', destination: `${backendUrl}/api/admin/templates/` },
      { source: '/api/admin/templates/', destination: `${backendUrl}/api/admin/templates/` },
      { source: '/api/admin/sessions', destination: `${backendUrl}/api/admin/sessions/` },
      { source: '/api/admin/sessions/', destination: `${backendUrl}/api/admin/sessions/` },
      { source: '/api/admin/sessions/:token/detail', destination: `${backendUrl}/api/admin/sessions/:token/detail/` },
      { source: '/api/admin/sessions/:token/detail/', destination: `${backendUrl}/api/admin/sessions/:token/detail/` },
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
