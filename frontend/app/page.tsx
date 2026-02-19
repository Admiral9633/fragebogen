export default function Home() {
  return (
    <main className="min-h-screen flex items-center justify-center p-8">
      <div className="max-w-2xl text-center">
        <h1 className="text-4xl font-bold mb-4">
          Verkehrsmedizinischer Fragebogen
        </h1>
        <p className="text-lg text-muted-foreground mb-8">
          Willkommen zum digitalen Fragebogen-System.
          Bitte verwenden Sie den Link, der Ihnen per E-Mail zugesandt wurde.
        </p>
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-6 text-left">
          <h2 className="font-semibold mb-2">Hinweise:</h2>
          <ul className="list-disc list-inside space-y-1 text-sm">
            <li>Der Link ist 7 Tage gültig</li>
            <li>Der Fragebogen kann nur einmal ausgefüllt werden</li>
            <li>Alle Angaben werden vertraulich behandelt</li>
            <li>Nach dem Absenden erhalten Sie eine PDF-Zusammenfassung</li>
          </ul>
        </div>
      </div>
    </main>
  );
}
