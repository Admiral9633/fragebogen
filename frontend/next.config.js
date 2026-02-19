/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: false,
  // puppeteer runs server-side in API routes – don't bundle it
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
    ]
  },
}

module.exports = nextConfig
