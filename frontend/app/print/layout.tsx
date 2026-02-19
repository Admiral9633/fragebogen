export default function PrintLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div
      style={{
        background: "#ffffff",
        fontFamily: "Helvetica, Arial, sans-serif",
        color: "#1a1a1a",
        WebkitPrintColorAdjust: "exact",
      }}
    >
      <style
        dangerouslySetInnerHTML={{
          __html: `
            body { background: #fff !important; }
            * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
            @media print { .page-break { page-break-before: always; } }
          `,
        }}
      />
      {children}
    </div>
  );
}
