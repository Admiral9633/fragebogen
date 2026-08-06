import { NextRequest, NextResponse } from "next/server";

export const dynamic = "force-dynamic";
export const maxDuration = 60;

export async function GET(
  request: NextRequest,
  context: { params: Promise<{ token: string }> }
) {
  const { token } = await context.params;

  // Internal app URL: Puppeteer runs inside the same container
  const appUrl = process.env.NEXT_PUBLIC_APP_URL || "http://localhost:3000";
  const printUrl = `${appUrl}/print/${token}`;

  // Session erst validieren, bevor eine Chromium-Instanz gestartet wird
  const backendUrl = process.env.BACKEND_URL || "http://backend:8000";
  try {
    const check = await fetch(`${backendUrl}/api/answers/${token}/`, {
      cache: "no-store",
    });
    if (!check.ok) {
      return NextResponse.json(
        { error: "Fragebogen nicht gefunden oder noch nicht abgeschlossen" },
        { status: check.status === 400 ? 409 : 404 }
      );
    }
  } catch {
    return NextResponse.json(
      { error: "Backend nicht erreichbar" },
      { status: 502 }
    );
  }

  // webpackIgnore verhindert dass webpack diesen Import analysiert/bundelt
  const puppeteer = (await import(/* webpackIgnore: true */ "puppeteer-core")).default;

  let browser;
  try {
    browser = await puppeteer.launch({
      executablePath:
        process.env.PUPPETEER_EXECUTABLE_PATH ||
        "/usr/bin/chromium-browser",
      headless: true,
      args: [
        "--no-sandbox",
        "--disable-setuid-sandbox",
        "--disable-dev-shm-usage",
        "--disable-gpu",
        "--no-first-run",
        "--no-zygote",
        "--single-process",
        "--font-render-hinting=none",
      ],
    });

    const page = await browser.newPage();
    await page.setViewport({ width: 794, height: 1123 }); // A4 @ 96dpi

    const gotoResponse = await page.goto(printUrl, {
      waitUntil: "networkidle0",
      timeout: 30000,
    });
    if (!gotoResponse || gotoResponse.status() !== 200) {
      return NextResponse.json(
        { error: "Fragebogen nicht gefunden" },
        { status: 404 }
      );
    }

    // Wait for fonts
    await page.evaluate(() => document.fonts.ready);

    const pdf = await page.pdf({
      format: "A4",
      printBackground: true,
      margin: {
        top: "13mm",
        right: "12mm",
        bottom: "11mm",
        left: "12mm",
      },
    });

    // Buffer → ArrayBuffer für NextResponse TypeScript-Kompatibilität
    const arrayBuffer = pdf.buffer.slice(
      pdf.byteOffset,
      pdf.byteOffset + pdf.byteLength
    ) as ArrayBuffer;

    return new NextResponse(arrayBuffer, {
      headers: {
        "Content-Type": "application/pdf",
        "Content-Disposition": `attachment; filename="fragebogen_design_${token}.pdf"`,
      },
    });
  } catch (error) {
    console.error("Puppeteer PDF error:", error);
    return NextResponse.json(
      { error: "PDF-Generierung fehlgeschlagen", detail: String(error) },
      { status: 500 }
    );
  } finally {
    if (browser) await browser.close();
  }
}
