"use client";

import { createContext, useContext, useEffect, useState } from "react";

export type Theme = "light" | "dark" | "paper-ink";

interface ThemeContextValue {
  theme: Theme;
  setTheme: (t: Theme) => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  theme: "light",
  setTheme: () => {},
});

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setTheme] = useState<Theme>("light");

  // Restore saved preference on mount
  useEffect(() => {
    const saved = localStorage.getItem("theme") as Theme | null;
    if (saved === "dark" || saved === "paper-ink") {
      setTheme(saved);
    }
  }, []);

  // Apply class to <html> whenever theme changes
  useEffect(() => {
    const root = document.documentElement;
    root.classList.remove("dark", "paper-ink");
    if (theme !== "light") root.classList.add(theme);
    localStorage.setItem("theme", theme);
  }, [theme]);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

export const useTheme = () => useContext(ThemeContext);
