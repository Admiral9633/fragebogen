"use client";

import * as React from "react";
import { cn } from "@/lib/utils";

// ─── Radio Group ─────────────────────────────────────────────────────────────
interface RadioOption {
  value: string;
  label: string;
}
interface RadioGroupProps {
  name: string;
  value?: string;
  onChange?: (value: string) => void;
  options: RadioOption[];
  error?: string;
  inline?: boolean;
}
export function RadioGroup({ name, value, onChange, options, error, inline = false }: RadioGroupProps) {
  return (
    <div>
      <div className={cn("flex gap-3", inline ? "flex-row flex-wrap" : "flex-col")}>
        {options.map((opt) => (
          <label
            key={opt.value}
            className={cn(
              "flex items-center gap-3 px-4 py-3 rounded-xl border-2 cursor-pointer transition-all duration-150 select-none",
              value === opt.value
                ? "border-blue-500 bg-blue-50 text-blue-900 font-medium"
                : "border-gray-200 bg-white hover:border-blue-300 hover:bg-blue-50/40",
              "text-sm"
            )}
          >
            <input
              type="radio"
              name={name}
              value={opt.value}
              checked={value === opt.value}
              onChange={() => onChange?.(opt.value)}
              className="hidden"
            />
            <span
              className={cn(
                "w-5 h-5 rounded-full border-2 flex items-center justify-center flex-shrink-0",
                value === opt.value ? "border-blue-500" : "border-gray-300"
              )}
            >
              {value === opt.value && (
                <span className="w-2.5 h-2.5 rounded-full bg-blue-500" />
              )}
            </span>
            <span>{opt.label}</span>
          </label>
        ))}
      </div>
      {error && <p className="mt-1.5 text-xs text-red-500">{error}</p>}
    </div>
  );
}

// ─── Yes/No Toggle ────────────────────────────────────────────────────────────
interface YesNoProps {
  name: string;
  value?: string;
  onChange?: (value: string) => void;
  error?: string;
}
export function YesNo({ name, value, onChange, error }: YesNoProps) {
  return (
    <div>
      <div className="inline-flex rounded-xl overflow-hidden border-2 border-gray-200">
        {[{ v: "yes", l: "Ja" }, { v: "no", l: "Nein" }].map(({ v, l }) => (
          <button
            key={v}
            type="button"
            onClick={() => onChange?.(v)}
            className={cn(
              "px-6 py-2.5 text-sm font-medium transition-all duration-150",
              value === v
                ? v === "yes"
                  ? "bg-blue-500 text-white"
                  : "bg-gray-700 text-white"
                : "bg-white text-gray-600 hover:bg-gray-50"
            )}
          >
            {l}
          </button>
        ))}
      </div>
      {error && <p className="mt-1.5 text-xs text-red-500">{error}</p>}
    </div>
  );
}

// ─── Question Row ─────────────────────────────────────────────────────────────
interface QuestionRowProps {
  label: string;
  hint?: string;
  required?: boolean;
  children: React.ReactNode;
  error?: string;
}
export function QuestionRow({ label, hint, required, children, error }: QuestionRowProps) {
  return (
    <div className="py-4 first:pt-0 last:pb-0 border-b border-gray-100 last:border-0">
      <div className="flex flex-col sm:flex-row sm:items-start gap-3">
        <div className="sm:w-1/2 flex-shrink-0">
          <p className="text-sm font-medium text-gray-800 leading-snug">
            {label}
            {required && <span className="text-red-500 ml-0.5">*</span>}
          </p>
          {hint && <p className="text-xs text-gray-500 mt-0.5">{hint}</p>}
        </div>
        <div className="sm:w-1/2">
          {children}
          {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
        </div>
      </div>
    </div>
  );
}

// ─── Section Card ─────────────────────────────────────────────────────────────
interface SectionCardProps {
  title: string;
  subtitle?: string;
  icon?: React.ReactNode;
  children: React.ReactNode;
  accentColor?: string;
}
export function SectionCard({ title, subtitle, icon, children, accentColor = "bg-blue-500" }: SectionCardProps) {
  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden mb-5">
      <div className={cn("px-6 py-4 flex items-center gap-3", accentColor)}>
        {icon && <div className="text-white/90">{icon}</div>}
        <div>
          <h2 className="font-semibold text-white text-base">{title}</h2>
          {subtitle && <p className="text-white/80 text-xs mt-0.5">{subtitle}</p>}
        </div>
      </div>
      <div className="px-6 py-2">{children}</div>
    </div>
  );
}

// ─── Text Input ───────────────────────────────────────────────────────────────
interface TextInputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  error?: string;
}
export function TextInput({ error, className, ...props }: TextInputProps) {
  return (
    <div>
      <input
        className={cn(
          "w-full px-3 py-2.5 rounded-xl border-2 border-gray-200 text-sm bg-white",
          "focus:outline-none focus:border-blue-400 transition-colors",
          error && "border-red-400",
          className
        )}
        {...props}
      />
      {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
    </div>
  );
}

// ─── Textarea ───────────────────────────────────────────────────────────────
interface TextAreaProps extends React.TextareaHTMLAttributes<HTMLTextAreaElement> {
  error?: string;
}
export function TextArea({ error, className, ...props }: TextAreaProps) {
  return (
    <div>
      <textarea
        className={cn(
          "w-full px-3 py-2.5 rounded-xl border-2 border-gray-200 text-sm bg-white resize-none",
          "focus:outline-none focus:border-blue-400 transition-colors",
          error && "border-red-400",
          className
        )}
        rows={3}
        {...props}
      />
      {error && <p className="mt-1 text-xs text-red-500">{error}</p>}
    </div>
  );
}

// ─── Progress Bar ─────────────────────────────────────────────────────────────
interface ProgressBarProps {
  current: number;
  total: number;
  label?: string;
}
export function ProgressBar({ current, total, label }: ProgressBarProps) {
  const pct = Math.round((current / total) * 100);
  return (
    <div className="mb-6">
      <div className="flex justify-between items-center mb-1.5">
        <span className="text-xs font-medium text-gray-500">{label ?? `Abschnitt ${current} von ${total}`}</span>
        <span className="text-xs font-semibold text-blue-600">{pct}%</span>
      </div>
      <div className="w-full h-2 bg-gray-100 rounded-full overflow-hidden">
        <div
          className="h-full bg-blue-500 rounded-full transition-all duration-500"
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  );
}

// ─── ESS Scale Button ─────────────────────────────────────────────────────────
interface ESSButtonGroupProps {
  name: string;
  value?: string;
  onChange?: (value: string) => void;
  error?: string;
}
export function ESSButtonGroup({ name, value, onChange, error }: ESSButtonGroupProps) {
  const opts = [
    { v: "0", l: "0", sub: "Nie" },
    { v: "1", l: "1", sub: "Gering" },
    { v: "2", l: "2", sub: "Mittel" },
    { v: "3", l: "3", sub: "Hoch" },
  ];
  return (
    <div>
      <div className="grid grid-cols-4 gap-2">
        {opts.map(({ v, l, sub }) => (
          <button
            key={v}
            type="button"
            onClick={() => onChange?.(v)}
            className={cn(
              "flex flex-col items-center py-3 px-2 rounded-xl border-2 transition-all duration-150",
              value === v
                ? "border-blue-500 bg-blue-500 text-white shadow-sm"
                : "border-gray-200 bg-white text-gray-700 hover:border-blue-300"
            )}
          >
            <span className="text-lg font-bold leading-none">{l}</span>
            <span className={cn("text-xs mt-1", value === v ? "text-white/80" : "text-gray-400")}>{sub}</span>
          </button>
        ))}
      </div>
      {error && <p className="mt-1.5 text-xs text-red-500">{error}</p>}
    </div>
  );
}

// ─── Checkbox ─────────────────────────────────────────────────────────────────
interface CheckboxProps {
  id: string;
  label: React.ReactNode;
  checked?: boolean;
  onChange?: (v: boolean) => void;
  error?: string;
}
export function Checkbox({ id, label, checked, onChange, error }: CheckboxProps) {
  return (
    <div>
      <label htmlFor={id} className="flex items-start gap-3 cursor-pointer group">
        <span
          className={cn(
            "mt-0.5 w-5 h-5 rounded flex items-center justify-center border-2 flex-shrink-0 transition-all",
            checked ? "bg-blue-500 border-blue-500" : "border-gray-300 group-hover:border-blue-400"
          )}
          onClick={() => onChange?.(!checked)}
        >
          {checked && (
            <svg className="w-3 h-3 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
            </svg>
          )}
        </span>
        <input
          type="checkbox"
          id={id}
          checked={checked}
          onChange={(e) => onChange?.(e.target.checked)}
          className="sr-only"
        />
        <span className="text-sm text-gray-700 leading-snug">{label}</span>
      </label>
      {error && <p className="mt-1 text-xs text-red-500 ml-8">{error}</p>}
    </div>
  );
}
