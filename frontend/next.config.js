/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: false,
  // puppeteer runs server-side in API routes – don't bundle it
  serverExternalPackages: ['puppeteer-core'],
  async rewrites() {
    const backendUrl = process.env.BACKEND_URL || 'http://backend:8000'
    return [
      {
        source: '/api/session/:path*',
        destination: backendUrl + '/api/session/:path*',
      },
      {
        source: '/api/submit/:path*',
        destination: backendUrl + '/api/submit/:path*',
      },
      {
        source: '/api/pdf/:path*',
        destination: backendUrl + '/api/pdf/:path*',
      },
      {
        source: '/api/answers/:path*',
        destination: backendUrl + '/api/answers/:path*',
      },
    ]
  },
}

module.exports = nextConfig
