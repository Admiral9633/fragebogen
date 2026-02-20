"use client";

import { useState, useEffect, useCallback } from "react";

const STORAGE_KEY = "admin_api_key";

interface Session {
  token: string;
  patient_last_name: string;
  patient_first_name: string;
  patient_email: string;
  patient_birth_date: string;
  completed: boolean;
  completed_at: string | null;
  created_at: string;
  expires_at: string;
  invitation_sent_at: string | null;
}

// ─── Login ────────────────────────────────────────────────────────────────────

function LoginForm({ onLogin }: { onLogin: (key: string) => void }) {
  const [key, setKey] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setLoading(true);
    setError("");
    try {
      const res = await fetch("/api/admin/sessions/", {
        headers: { Authorization: `Bearer ${key}` },
      });
      if (res.status === 403 || res.status === 401) {
        setError("Falsches Passwort.");
      } else if (res.ok) {
        sessionStorage.setItem(STORAGE_KEY, key);
        onLogin(key);
      } else {
        setError("Fehler beim Verbinden.");
      }
    } catch {
      setError("Server nicht erreichbar.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center">
      <div className="bg-white rounded-xl shadow-md p-8 w-full max-w-sm">
        <h1 className="text-2xl font-bold text-[#1f3864] mb-6">Admin-Bereich</h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Admin-Passwort
            </label>
            <input
              type="password"
              value={key}
              onChange={(e) => setKey(e.target.value)}
              className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#1f3864]"
              autoFocus
              required
            />
          </div>
          {error && <p className="text-red-600 text-sm">{error}</p>}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-[#1f3864] text-white rounded-lg px-4 py-2 text-sm font-semibold hover:bg-[#162b4d] disabled:opacity-50"
          >
            {loading ? "Bitte warten…" : "Anmelden"}
          </button>
        </form>
      </div>
    </div>
  );
}

// ─── Dashboard ────────────────────────────────────────────────────────────────

function Dashboard({ apiKey, onLogout }: { apiKey: string; onLogout: () => void }) {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [loadingList, setLoadingList] = useState(true);
  const [listError, setListError] = useState("");

  // Formular
  const [lastName, setLastName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [email, setEmail] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [creating, setCreating] = useState(false);
  const [createMsg, setCreateMsg] = useState<{ text: string; ok: boolean } | null>(null);

  // Action-Feedback
  const [actionMsg, setActionMsg] = useState<{ token: string; text: string; ok: boolean } | null>(null);

  const headers = { "Content-Type": "application/json", Authorization: `Bearer ${apiKey}` };

  const loadSessions = useCallback(async () => {
    setLoadingList(true);
    setListError("");
    try {
      const res = await fetch("/api/admin/sessions/", { headers });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      setSessions(await res.json());
    } catch (e) {
      setListError(String(e));
    } finally {
      setLoadingList(false);
    }
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiKey]);

  useEffect(() => { loadSessions(); }, [loadSessions]);

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault();
    setCreating(true);
    setCreateMsg(null);
    try {
      const res = await fetch("/api/admin/sessions/", {
        method: "POST",
        headers,
        body: JSON.stringify({
          patient_last_name: lastName,
          patient_first_name: firstName,
          patient_email: email,
          patient_birth_date: birthDate || undefined,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        setCreateMsg({ text: data.error || "Fehler beim Anlegen.", ok: false });
      } else {
        const emailStatus = data.email_sent
          ? "E-Mail wurde versendet."
          : `E-Mail konnte nicht gesendet werden: ${data.email_error}`;
        setCreateMsg({ text: `Session angelegt. ${emailStatus}`, ok: data.email_sent });
        setLastName(""); setFirstName(""); setEmail(""); setBirthDate("");
        loadSessions();
      }
    } catch {
      setCreateMsg({ text: "Netzwerkfehler.", ok: false });
    } finally {
      setCreating(false);
    }
  }

  async function handleResend(token: string) {
    setActionMsg(null);
    try {
      const res = await fetch(`/api/admin/sessions/${token}/resend/`, { method: "POST", headers });
      const data = await res.json();
      setActionMsg({ token, text: res.ok ? "E-Mail erneut versendet." : (data.error || "Fehler"), ok: res.ok });
      loadSessions();
    } catch {
      setActionMsg({ token, text: "Netzwerkfehler.", ok: false });
    }
  }

  async function handleDelete(token: string, name: string) {
    if (!confirm(`Session von ${name} wirklich löschen?`)) return;
    setActionMsg(null);
    try {
      const res = await fetch(`/api/admin/sessions/${token}/delete/`, { method: "DELETE", headers });
      setActionMsg({ token, text: res.ok ? "Session gelöscht." : "Fehler beim Löschen.", ok: res.ok });
      loadSessions();
    } catch {
      setActionMsg({ token, text: "Netzwerkfehler.", ok: false });
    }
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Topbar */}
      <div className="bg-[#1f3864] text-white px-6 py-3 flex items-center justify-between">
        <span className="font-bold text-lg">Fragebogen-Admin</span>
        <button
          onClick={onLogout}
          className="text-sm text-blue-200 hover:text-white"
        >
          Abmelden
        </button>
      </div>

      <div className="max-w-5xl mx-auto px-4 py-6 space-y-8">
        {/* ── Neue Einladung ─────────────────────────────────────────── */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <h2 className="text-lg font-bold text-[#1f3864] mb-4">Neue Einladung versenden</h2>
          <form onSubmit={handleCreate} className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-medium text-gray-600 mb-1">Nachname *</label>
              <input
                type="text" value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
                className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#1f3864]"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-600 mb-1">Vorname *</label>
              <input
                type="text" value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
                className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#1f3864]"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-600 mb-1">E-Mail *</label>
              <input
                type="email" value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#1f3864]"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-600 mb-1">Geburtsdatum</label>
              <input
                type="date" value={birthDate}
                onChange={(e) => setBirthDate(e.target.value)}
                className="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-[#1f3864]"
              />
            </div>
            <div className="sm:col-span-2 flex items-center gap-4">
              <button
                type="submit"
                disabled={creating}
                className="bg-[#1f3864] text-white rounded-lg px-6 py-2 text-sm font-semibold hover:bg-[#162b4d] disabled:opacity-50"
              >
                {creating ? "Wird angelegt…" : "Einladung senden"}
              </button>
              {createMsg && (
                <span className={`text-sm ${createMsg.ok ? "text-green-700" : "text-red-600"}`}>
                  {createMsg.text}
                </span>
              )}
            </div>
          </form>
        </div>

        {/* ── Session-Übersicht ──────────────────────────────────────── */}
        <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
          <div className="flex items-center justify-between mb-4">
            <h2 className="text-lg font-bold text-[#1f3864]">Alle Sessions ({sessions.length})</h2>
            <button
              onClick={loadSessions}
              className="text-sm text-[#1f3864] hover:underline"
            >
              ↻ Aktualisieren
            </button>
          </div>

          {listError && <p className="text-red-600 text-sm mb-3">{listError}</p>}
          {loadingList ? (
            <p className="text-gray-400 text-sm">Lade…</p>
          ) : sessions.length === 0 ? (
            <p className="text-gray-400 text-sm">Noch keine Sessions vorhanden.</p>
          ) : (
            <div className="overflow-x-auto">
              <table className="w-full text-sm border-collapse">
                <thead>
                  <tr className="text-left text-xs text-gray-500 border-b border-gray-200">
                    <th className="pb-2 pr-4 font-medium">Patient</th>
                    <th className="pb-2 pr-4 font-medium">E-Mail</th>
                    <th className="pb-2 pr-4 font-medium">Geburtsdatum</th>
                    <th className="pb-2 pr-4 font-medium">Status</th>
                    <th className="pb-2 pr-4 font-medium">Erstellt</th>
                    <th className="pb-2 font-medium">Aktionen</th>
                  </tr>
                </thead>
                <tbody>
                  {sessions.map((s) => (
                    <tr key={s.token} className="border-b border-gray-100 hover:bg-gray-50">
                      <td className="py-2 pr-4 font-medium">
                        {s.patient_last_name || "—"}{s.patient_first_name ? `, ${s.patient_first_name}` : ""}
                      </td>
                      <td className="py-2 pr-4 text-gray-600">{s.patient_email || "—"}</td>
                      <td className="py-2 pr-4 text-gray-600">{s.patient_birth_date || "—"}</td>
                      <td className="py-2 pr-4">
                        {s.completed ? (
                          <span className="inline-block bg-green-100 text-green-800 text-xs px-2 py-0.5 rounded-full">
                            ✓ Ausgefüllt {s.completed_at ? `(${s.completed_at})` : ""}
                          </span>
                        ) : (
                          <span className="inline-block bg-orange-100 text-orange-700 text-xs px-2 py-0.5 rounded-full">
                            Offen (bis {s.expires_at})
                          </span>
                        )}
                      </td>
                      <td className="py-2 pr-4 text-gray-500 text-xs">{s.created_at}</td>
                      <td className="py-2">
                        <div className="flex items-center gap-2 flex-wrap">
                          {/* Fragebogen-Link kopieren */}
                          <button
                            onClick={() => {
                              navigator.clipboard.writeText(`${window.location.origin}/q/${s.token}`);
                              setActionMsg({ token: s.token, text: "Link kopiert!", ok: true });
                            }}
                            className="text-xs text-blue-600 hover:underline"
                            title="Fragebogen-Link kopieren"
                          >
                            Link
                          </button>
                          {/* PDF (Design) */}
                          {s.completed && (
                            <a
                              href={`/api/puppeteer-pdf/${s.token}`}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-xs text-[#1f3864] hover:underline"
                            >
                              PDF
                            </a>
                          )}
                          {/* E-Mail erneut senden */}
                          {!s.completed && s.patient_email && (
                            <button
                              onClick={() => handleResend(s.token)}
                              className="text-xs text-amber-600 hover:underline"
                            >
                              Einladung
                            </button>
                          )}
                          {/* Löschen */}
                          <button
                            onClick={() => handleDelete(s.token, `${s.patient_last_name} ${s.patient_first_name}`.trim() || s.token)}
                            className="text-xs text-red-500 hover:underline"
                          >
                            Löschen
                          </button>
                        </div>
                        {actionMsg?.token === s.token && (
                          <p className={`text-xs mt-1 ${actionMsg.ok ? "text-green-600" : "text-red-500"}`}>
                            {actionMsg.text}
                          </p>
                        )}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

// ─── Page ─────────────────────────────────────────────────────────────────────

export default function AdminPage() {
  const [apiKey, setApiKey] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);

  useEffect(() => {
    const stored = sessionStorage.getItem(STORAGE_KEY);
    setApiKey(stored);
    setChecked(true);
  }, []);

  function handleLogin(key: string) {
    setApiKey(key);
  }

  function handleLogout() {
    sessionStorage.removeItem(STORAGE_KEY);
    setApiKey(null);
  }

  if (!checked) return null;

  if (!apiKey) {
    return <LoginForm onLogin={handleLogin} />;
  }

  return <Dashboard apiKey={apiKey} onLogout={handleLogout} />;
}
