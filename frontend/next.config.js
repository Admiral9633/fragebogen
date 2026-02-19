/** @type {import('next').NextConfig} */
const nextConfig = {
  trailingSlash: false,
  // puppeteer runs server-side in API routes – don't bundle it
  serverExternalPackages: ['puppeteer'],
  async rewrites() {
    const backendUrl = process.env.BACKEND_URL || 'http://backend:8000'
    return [
      {
        source: '/api/:path*/',
        destination: backendUrl + '/api/:path*/',
      },
      {
        source: '/api/:path*',
        destination: backendUrl + '/api/:path*/',
      },
    ]
  },
}

module.exports = nextConfig
