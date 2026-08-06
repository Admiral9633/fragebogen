import coreWebVitals from "eslint-config-next/core-web-vitals";
import typescript from "eslint-config-next/typescript";

const eslintConfig = [
  ...coreWebVitals,
  ...typescript,
  {
    ignores: ["node_modules/**", ".next/**", "out/**"],
  },
  {
    rules: {
      // Formulardaten sind bewusst ein flexibler Record; harte Typisierung lohnt hier nicht
      "@typescript-eslint/no-explicit-any": "warn",
      // Strenge react-hooks-v7-Regeln melden etablierte shadcn-Muster (use-mobile,
      // theme-provider, sidebar) — nicht refactoren, nur warnen
      "react-hooks/set-state-in-effect": "warn",
      "react-hooks/purity": "warn",
    },
  },
  {
    // CommonJS-Konfigdateien (tailwind.config.js, postcss.config.js) nutzen require()
    files: ["*.config.js"],
    rules: {
      "@typescript-eslint/no-require-imports": "off",
    },
  },
];

export default eslintConfig;
