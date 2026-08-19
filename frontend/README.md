# Verkehrsmedizin Frontend

Next.js Frontend für das Verkehrsmedizin Fragebogen-System.

## Features

- Next.js 16 App Router + React 19
- Shadcn/ui Components, sonner-Toasts, Dark Mode
- Tailwind CSS
- TypeScript
- Puppeteer-PDF-Route (`/api/puppeteer-pdf/[token]`)

## Setup

1. Dependencies installieren:
```bash
npm install
```

2. Umgebungsvariablen konfigurieren:
```bash
cp .env.example .env.local
# Bearbeite .env.local mit deinen Werten
```

3. Development Server starten:
```bash
npm run dev
```

4. Build für Produktion:
```bash
npm run build
npm start
```

## Struktur

- `/app` - Next.js App Router Pages
- `/components` - React Components
- `/lib` - Utility Functions
- `/components/ui` - Shadcn/ui Components

## URLs

- Startseite: `http://localhost:3000`
- Fragebogen: `http://localhost:3000/q/[token]`
- Praxis-Admin: `http://localhost:3000/admin` (Login mit `ADMIN_API_KEY`)
