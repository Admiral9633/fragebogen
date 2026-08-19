"use client";

import { useState, useEffect, useCallback } from "react";
import { toast } from "sonner";
import {
  Link2, Mail, Pencil, Trash2, RefreshCw,
  FileText, Plus, CheckCircle2, Clock, Loader2,
} from "lucide-react";

import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from "@/components/ui/alert-dialog";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogFooter } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip";
import { Separator } from "@/components/ui/separator";
import { Skeleton } from "@/components/ui/skeleton";
import { DatePicker } from "@/components/ui/date-picker";
import { SidebarProvider, SidebarInset } from "@/components/ui/sidebar";
import { AppSidebar } from "@/components/app-sidebar";
import { SiteHeader } from "@/components/site-header";

// ─── Types ────────────────────────────────────────────────────────────────────

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
  gdt_patient_id: string;
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
    <div className="min-h-screen bg-muted/40 flex items-center justify-center p-4">
      <Card className="w-full max-w-sm">
        <CardHeader>
          <CardTitle className="text-xl">Admin-Bereich</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div className="space-y-1.5">
              <Label htmlFor="apikey">Passwort</Label>
              <Input id="apikey" type="password" value={key} onChange={(e) => setKey(e.target.value)} autoFocus required />
            </div>
            {error && <p className="text-sm text-destructive">{error}</p>}
            <Button type="submit" className="w-full" disabled={loading}>
              {loading && <Loader2 className="mr-2 size-4 animate-spin" />}
              Anmelden
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}

// ─── Edit Dialog ──────────────────────────────────────────────────────────────

interface EditDialogProps {
  session: Session | null;
  onClose: () => void;
  onSaved: () => void;
  headers: Record<string, string>;
}

function EditDialog({ session, onClose, onSaved, headers }: EditDialogProps) {
  const [lastName, setLastName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [email, setEmail] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    if (!session) return;
    setLastName(session.patient_last_name || "");
    setFirstName(session.patient_first_name || "");
    setEmail(session.patient_email || "");
    if (session.patient_birth_date) {
      const p = session.patient_birth_date.split(".");
      setBirthDate(p.length === 3 ? `${p[2]}-${p[1]}-${p[0]}` : session.patient_birth_date);
    } else setBirthDate("");
  }, [session]);

  async function handleSave() {
    if (!session) return;
    setSaving(true);
    try {
      const res = await fetch(`/api/admin/sessions/${session.token}/update/`, {
        method: "PATCH",
        headers,
        body: JSON.stringify({
          patient_last_name: lastName,
          patient_first_name: firstName,
          patient_email: email,
          patient_birth_date: birthDate || "",
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        toast.error(data.error || "Fehler beim Speichern.");
      } else {
        toast.success("Patientendaten gespeichert.");
        onSaved();
        onClose();
      }
    } catch {
      toast.error("Netzwerkfehler.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <Dialog open={!!session} onOpenChange={(open) => !open && onClose()}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Patient bearbeiten</DialogTitle>
        </DialogHeader>
        <div className="grid grid-cols-2 gap-3 py-2">
          <div className="space-y-1.5">
            <Label>Nachname</Label>
            <Input value={lastName} onChange={(e) => setLastName(e.target.value)} />
          </div>
          <div className="space-y-1.5">
            <Label>Vorname</Label>
            <Input value={firstName} onChange={(e) => setFirstName(e.target.value)} />
          </div>
          <div className="col-span-2 space-y-1.5">
            <Label>E-Mail <span className="text-muted-foreground text-xs">(optional)</span></Label>
            <Input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="—" />
          </div>
          <div className="col-span-2 space-y-1.5">
            <Label>Geburtsdatum</Label>
            <DatePicker value={birthDate} onChange={(v) => setBirthDate(v)} />
          </div>
        </div>
        <DialogFooter>
          <Button variant="outline" onClick={onClose}>Abbrechen</Button>
          <Button onClick={handleSave} disabled={saving}>
            {saving && <Loader2 className="mr-2 size-4 animate-spin" />}
            Speichern
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
}

// ─── Dashboard ────────────────────────────────────────────────────────────────

function Dashboard({ apiKey, onLogout }: { apiKey: string; onLogout: () => void }) {
  const [sessions, setSessions] = useState<Session[]>([]);
  const [loading, setLoading] = useState(true);
  const [listError, setListError] = useState("");

  const [lastName, setLastName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [email, setEmail] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [creating, setCreating] = useState(false);

  const [editSession, setEditSession] = useState<Session | null>(null);
  const [deleteSession, setDeleteSession] = useState<Session | null>(null);

  const headers = {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  };

  const loadSessions = useCallback(async () => {
    setLoading(true);
    setListError("");
    try {
      const res = await fetch("/api/admin/sessions/", { headers });
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      setSessions(await res.json());
    } catch (e) {
      setListError(String(e));
    } finally {
      setLoading(false);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [apiKey]);

  useEffect(() => { loadSessions(); }, [loadSessions]);

  async function handleCreate(e: React.FormEvent) {
    e.preventDefault();
    setCreating(true);
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
        toast.error(data.error || "Fehler beim Anlegen.");
      } else {
        if (!email) {
          toast.success("Session angelegt (keine E-Mail).");
        } else if (data.email_sent) {
          toast.success("Session angelegt, E-Mail versendet.");
        } else {
          toast.warning(`Session angelegt. E-Mail-Fehler: ${data.email_error}`);
        }
        setLastName(""); setFirstName(""); setEmail(""); setBirthDate("");
        loadSessions();
      }
    } catch {
      toast.error("Netzwerkfehler.");
    } finally {
      setCreating(false);
    }
  }

  function copyLink(token: string) {
    const url = `${window.location.origin}/q/${token}`;
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(url).then(() => toast.success("Link kopiert!"));
    } else {
      const ta = document.createElement("textarea");
      ta.value = url;
      ta.style.cssText = "position:fixed;opacity:0";
      document.body.appendChild(ta);
      ta.select();
      document.execCommand("copy");
      document.body.removeChild(ta);
      toast.success("Link kopiert!");
    }
  }

  async function handleResend(token: string) {
    try {
      const res = await fetch(`/api/admin/sessions/${token}/resend/`, { method: "POST", headers });
      const data = await res.json();
      if (res.ok) {
        toast.success("Einladung erneut versendet.");
      } else {
        toast.error(data.error || "Fehler");
      }
    } catch {
      toast.error("Netzwerkfehler.");
    }
  }

  async function handleDelete(token: string) {
    try {
      const res = await fetch(`/api/admin/sessions/${token}/delete/`, { method: "DELETE", headers });
      if (res.ok) {
        toast.success("Session gelöscht.");
        loadSessions();
      } else {
        toast.error("Fehler beim Löschen.");
      }
    } catch {
      toast.error("Netzwerkfehler.");
    }
  }

  return (
    <SidebarProvider>
      <AppSidebar onLogout={onLogout} />
      <SidebarInset>
        <SiteHeader title="Fragebogen-Admin" />
        <TooltipProvider delayDuration={300}>
          <div className="flex flex-1 flex-col gap-6 p-4 md:p-6">
          {/* Übersicht */}
          <div id="overview" className="grid grid-cols-2 sm:grid-cols-3 gap-4 scroll-mt-16">
            <Card>
              <CardContent className="pt-6">
                <p className="text-2xl font-bold">{sessions.length}</p>
                <p className="text-sm text-muted-foreground">Sessions gesamt</p>
              </CardContent>
            </Card>
            <Card>
              <CardContent className="pt-6">
                <p className="text-2xl font-bold text-green-600">{sessions.filter(s => s.completed).length}</p>
                <p className="text-sm text-muted-foreground">Abgeschlossen</p>
              </CardContent>
            </Card>
            <Card className="col-span-2 sm:col-span-1">
              <CardContent className="pt-6">
                <p className="text-2xl font-bold text-amber-500">{sessions.filter(s => !s.completed).length}</p>
                <p className="text-sm text-muted-foreground">Offen</p>
              </CardContent>
            </Card>
          </div>

          {/* Neue Einladung */}
          <Card id="create" className="scroll-mt-16">
            <CardHeader className="pb-3">
              <CardTitle className="text-base flex items-center gap-2">
                <Plus className="size-4" />
                Neue Einladung
              </CardTitle>
            </CardHeader>
            <Separator />
            <CardContent className="pt-4">
              <form onSubmit={handleCreate} className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 items-end">
                <div className="space-y-1.5">
                  <Label htmlFor="c-ln">Nachname <span className="text-destructive">*</span></Label>
                  <Input id="c-ln" value={lastName} onChange={(e) => setLastName(e.target.value)} required />
                </div>
                <div className="space-y-1.5">
                  <Label htmlFor="c-fn">Vorname <span className="text-destructive">*</span></Label>
                  <Input id="c-fn" value={firstName} onChange={(e) => setFirstName(e.target.value)} required />
                </div>
                <div className="space-y-1.5">
                  <Label htmlFor="c-em">
                    E-Mail <span className="text-muted-foreground text-xs">(optional)</span>
                  </Label>
                  <Input id="c-em" type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="—" />
                </div>
                <div className="space-y-1.5">
                  <Label htmlFor="c-bd">Geburtsdatum</Label>
                  <DatePicker value={birthDate} onChange={(v) => setBirthDate(v)} />
                </div>
                <div className="sm:col-span-2 lg:col-span-4">
                  <Button type="submit" disabled={creating}>
                    {creating
                      ? <><Loader2 className="mr-2 size-4 animate-spin" />Wird angelegt…</>
                      : <><Mail className="mr-2 size-4" />Einladung senden</>
                    }
                  </Button>
                </div>
              </form>
            </CardContent>
          </Card>

          {/* Session-Liste */}
          <Card id="sessions" className="scroll-mt-16">
            <CardHeader className="pb-3">
              <div className="flex items-center justify-between">
                <CardTitle className="text-base">
                  Alle Sessions
                  {sessions.length > 0 && (
                    <Badge variant="secondary" className="ml-2 font-normal">{sessions.length}</Badge>
                  )}
                </CardTitle>
                <Button variant="ghost" size="icon" onClick={loadSessions}>
                  <RefreshCw className="size-4" />
                </Button>
              </div>
            </CardHeader>
            <Separator />
            <CardContent className="p-0">
              {listError && <p className="text-sm text-destructive p-4">{listError}</p>}
              {loading ? (
                <div className="space-y-2 p-4">
                  {[...Array(3)].map((_, i) => <Skeleton key={i} className="h-10 w-full" />)}
                </div>
              ) : sessions.length === 0 ? (
                <p className="text-sm text-muted-foreground p-4 text-center">Keine Sessions vorhanden.</p>
              ) : (
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead>Patient</TableHead>
                      <TableHead>GDT</TableHead>
                      <TableHead>E-Mail</TableHead>
                      <TableHead>Geburtsdatum</TableHead>
                      <TableHead>Status</TableHead>
                      <TableHead>Erstellt</TableHead>
                      <TableHead className="text-right">Aktionen</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {sessions.map((s) => (
                      <TableRow key={s.token}>
                        <TableCell className="font-medium">
                          {s.patient_last_name || "—"}
                          {s.patient_first_name ? `, ${s.patient_first_name}` : ""}
                        </TableCell>

                        <TableCell>
                          {s.gdt_patient_id ? (
                            <Tooltip>
                              <TooltipTrigger asChild>
                                <Badge variant="secondary" className="cursor-default font-mono text-[10px]">
                                  GDT
                                </Badge>
                              </TooltipTrigger>
                              <TooltipContent>GDT-ID: {s.gdt_patient_id}</TooltipContent>
                            </Tooltip>
                          ) : (
                            <span className="text-muted-foreground">—</span>
                          )}
                        </TableCell>

                        <TableCell className="text-muted-foreground text-xs">{s.patient_email || "—"}</TableCell>

                        <TableCell className="text-muted-foreground text-xs">{s.patient_birth_date || "—"}</TableCell>

                        <TableCell>
                          {s.completed ? (
                            <Badge variant="success" className="gap-1">
                              <CheckCircle2 className="size-3" />
                              {s.completed_at ?? "Ausgefüllt"}
                            </Badge>
                          ) : (
                            <Badge variant="warning" className="gap-1">
                              <Clock className="size-3" />
                              Offen bis {s.expires_at}
                            </Badge>
                          )}
                        </TableCell>

                        <TableCell className="text-muted-foreground text-xs whitespace-nowrap">{s.created_at}</TableCell>

                        <TableCell>
                          <div className="flex items-center justify-end gap-1">
                            <Tooltip>
                              <TooltipTrigger asChild>
                                <Button variant="ghost" size="icon" onClick={() => copyLink(s.token)}>
                                  <Link2 className="size-4" />
                                </Button>
                              </TooltipTrigger>
                              <TooltipContent>Link kopieren</TooltipContent>
                            </Tooltip>

                            {s.completed && (
                              <Tooltip>
                                <TooltipTrigger asChild>
                                  <a
                                    href={`/api/puppeteer-pdf/${s.token}`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="inline-flex items-center justify-center h-9 w-9 rounded-md text-sm hover:bg-accent hover:text-accent-foreground"
                                  >
                                    <FileText className="size-4" />
                                  </a>
                                </TooltipTrigger>
                                <TooltipContent>PDF öffnen</TooltipContent>
                              </Tooltip>
                            )}

                            {!s.completed && s.patient_email && (
                              <Tooltip>
                                <TooltipTrigger asChild>
                                  <Button variant="ghost" size="icon" onClick={() => handleResend(s.token)}>
                                    <Mail className="size-4" />
                                  </Button>
                                </TooltipTrigger>
                                <TooltipContent>Einladung erneut senden</TooltipContent>
                              </Tooltip>
                            )}

                            <Tooltip>
                              <TooltipTrigger asChild>
                                <Button variant="ghost" size="icon" onClick={() => setEditSession(s)}>
                                  <Pencil className="size-4" />
                                </Button>
                              </TooltipTrigger>
                              <TooltipContent>Bearbeiten</TooltipContent>
                            </Tooltip>

                            <Tooltip>
                              <TooltipTrigger asChild>
                                <Button
                                  variant="ghost"
                                  size="icon"
                                  className="text-destructive hover:text-destructive"
                                  onClick={() => setDeleteSession(s)}
                                >
                                  <Trash2 className="size-4" />
                                </Button>
                              </TooltipTrigger>
                              <TooltipContent>Session löschen</TooltipContent>
                            </Tooltip>
                          </div>
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              )}
            </CardContent>
          </Card>
          </div>

          <EditDialog
            session={editSession}
            onClose={() => setEditSession(null)}
            onSaved={loadSessions}
            headers={headers}
          />

          <AlertDialog open={!!deleteSession} onOpenChange={(open) => !open && setDeleteSession(null)}>
            <AlertDialogContent>
              <AlertDialogHeader>
                <AlertDialogTitle>Session löschen?</AlertDialogTitle>
                <AlertDialogDescription>
                  Die Session
                  {deleteSession && (
                    <> von{" "}
                      <span className="font-medium text-foreground">
                        {`${deleteSession.patient_last_name} ${deleteSession.patient_first_name}`.trim() || deleteSession.token}
                      </span>
                    </>
                  )}{" "}
                  wird mitsamt allen Antworten unwiderruflich gelöscht.
                </AlertDialogDescription>
              </AlertDialogHeader>
              <AlertDialogFooter>
                <AlertDialogCancel>Abbrechen</AlertDialogCancel>
                <AlertDialogAction
                  className="bg-destructive text-destructive-foreground hover:bg-destructive/90"
                  onClick={() => {
                    if (deleteSession) handleDelete(deleteSession.token);
                    setDeleteSession(null);
                  }}
                >
                  Löschen
                </AlertDialogAction>
              </AlertDialogFooter>
            </AlertDialogContent>
          </AlertDialog>
        </TooltipProvider>
      </SidebarInset>
    </SidebarProvider>
  );
}

// ─── Page ─────────────────────────────────────────────────────────────────────

export default function AdminPage() {
  const [apiKey, setApiKey] = useState<string | null>(null);
  const [checked, setChecked] = useState(false);

  useEffect(() => {
    setApiKey(sessionStorage.getItem(STORAGE_KEY));
    setChecked(true);
  }, []);

  if (!checked) return null;
  if (!apiKey) return <LoginForm onLogin={(k) => { sessionStorage.setItem(STORAGE_KEY, k); setApiKey(k); }} />;
  return <Dashboard apiKey={apiKey} onLogout={() => { sessionStorage.removeItem(STORAGE_KEY); setApiKey(null); }} />;
}
