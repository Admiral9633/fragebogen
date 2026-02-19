"use client";

import { Sun, Moon, BookOpen } from "lucide-react";
import { useTheme, type Theme } from "./theme-provider";
import { Button } from "./ui/button";

const CYCLE: Theme[] = ["light", "dark", "paper-ink"];

const LABELS: Record<Theme, string> = {
  light: "Hell",
  dark: "Dunkel",
  "paper-ink": "E-Ink",
};

export function ThemeToggle() {
  const { theme, setTheme } = useTheme();

  const cycle = () => {
    const idx = CYCLE.indexOf(theme);
    setTheme(CYCLE[(idx + 1) % CYCLE.length]);
  };

  return (
    <Button
      variant="ghost"
      size="sm"
      onClick={cycle}
      title={`Modus: ${LABELS[theme]} – klicken zum Wechseln`}
      className="gap-1.5 text-xs font-medium"
    >
      {theme === "light"     && <Sun       className="w-4 h-4" />}
      {theme === "dark"      && <Moon      className="w-4 h-4" />}
      {theme === "paper-ink" && <BookOpen  className="w-4 h-4" />}
      <span className="hidden sm:inline">{LABELS[theme]}</span>
    </Button>
  );
}
