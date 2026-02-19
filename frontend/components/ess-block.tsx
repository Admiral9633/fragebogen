"use client";

import { useWatch } from "react-hook-form";
import { calcESS, ESS_QUESTIONS, ESS_OPTIONS } from "@/lib/ess";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { cn } from "@/lib/utils";

interface ESSBlockProps {
  control: any;
  register: any;
  errors?: any;
}

export function ESSBlock({ control, register, errors }: ESSBlockProps) {
  const values = useWatch({ control });
  const { total, bandLabel, bandColor } = calcESS(values ?? {});

  return (
    <Card className="mb-6">
      <CardHeader>
        <CardTitle>Epworth Sleepiness Scale (ESS)</CardTitle>
        <CardDescription>
          Wie hoch ist die Wahrscheinlichkeit, dass Sie in den folgenden Situationen einnicken oder einschlafen würden? 
          Gemeint ist das übliche Alltagsleben in letzter Zeit.
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {ESS_QUESTIONS.map((question, index) => (
          <div key={question.id} className="space-y-2">
            <Label htmlFor={question.id} className="font-medium">
              {index + 1}. {question.text}
            </Label>
            <select
              id={question.id}
              {...register(question.id, { 
                required: "Bitte wählen Sie eine Option",
                valueAsNumber: false 
              })}
              className={cn(
                "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background",
                "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
                "disabled:cursor-not-allowed disabled:opacity-50",
                errors?.[question.id] && "border-red-500"
              )}
            >
              <option value="">Bitte wählen...</option>
              {ESS_OPTIONS.map((option) => (
                <option key={option.value} value={option.value}>
                  {option.label}
                </option>
              ))}
            </select>
            {errors?.[question.id] && (
              <p className="text-sm text-red-600">{errors[question.id].message}</p>
            )}
          </div>
        ))}

        <div className="mt-8 p-6 bg-blue-50 border border-blue-200 rounded-lg">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-700">Ihr aktueller ESS-Score:</p>
              <p className="text-3xl font-bold text-blue-600">{total} / 24</p>
            </div>
            <div className="text-right">
              <p className="text-sm font-medium text-gray-700">Bewertung:</p>
              <p className={cn("text-xl font-semibold", bandColor)}>
                {bandLabel}
              </p>
            </div>
          </div>
          <div className="mt-4 text-sm text-gray-600">
            <p className="font-medium mb-2">Interpretation:</p>
            <ul className="space-y-1 list-disc list-inside">
              <li><span className="text-green-600 font-medium">Normal (0-9):</span> Keine erhöhte Tagesschläfrigkeit</li>
              <li><span className="text-orange-600 font-medium">Erhöht (10-15):</span> Erhöhte Tagesschläfrigkeit, weitere Abklärung empfohlen</li>
              <li><span className="text-red-600 font-medium">Ausgeprägt (≥16):</span> Stark erhöhte Tagesschläfrigkeit, ärztliche Abklärung erforderlich</li>
            </ul>
          </div>
        </div>
      </CardContent>
    </Card>
  );
}
