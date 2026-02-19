"use client";

import { useState } from "react";
import { useForm } from "react-hook-form";
import { ESSBlock } from "@/components/ess-block";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { cn } from "@/lib/utils";

interface QuestionnaireFormProps {
  token: string;
  onSubmitSuccess: (data: any) => void;
}

export function QuestionnaireForm({ token, onSubmitSuccess }: QuestionnaireFormProps) {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    control,
    formState: { errors },
  } = useForm({
    defaultValues: {
      ess_1: "",
      ess_2: "",
      ess_3: "",
      ess_4: "",
      ess_5: "",
      ess_6: "",
      ess_7: "",
      ess_8: "",
      consent_complete: false,
      consent_privacy: false,
    },
  });

  const onSubmit = async (data: any) => {
    setIsSubmitting(true);
    setError(null);

    try {
      // Konvertiere ESS Werte zu Zahlen
      const formattedData = {
        ...data,
        ess_1: parseInt(data.ess_1),
        ess_2: parseInt(data.ess_2),
        ess_3: parseInt(data.ess_3),
        ess_4: parseInt(data.ess_4),
        ess_5: parseInt(data.ess_5),
        ess_6: parseInt(data.ess_6),
        ess_7: parseInt(data.ess_7),
        ess_8: parseInt(data.ess_8),
      };

      const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const response = await fetch(`${apiUrl}/api/submit/${token}/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formattedData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Fehler beim Absenden des Fragebogens");
      }

      const result = await response.json();
      onSubmitSuccess(result);
    } catch (err: any) {
      setError(err.message || "Ein Fehler ist aufgetreten");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      {/* ESS Scale */}
      <ESSBlock control={control} register={register} errors={errors} />

      {/* Zusätzliche Fragen können hier hinzugefügt werden */}
      
      {/* Einwilligungen */}
      <Card>
        <CardHeader>
          <CardTitle>Einwilligung</CardTitle>
          <CardDescription>
            Bitte bestätigen Sie die folgenden Angaben
          </CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-start space-x-2">
            <input
              type="checkbox"
              id="consent_complete"
              {...register("consent_complete", {
                required: "Bitte bestätigen Sie die Vollständigkeit Ihrer Angaben",
              })}
              className="mt-1 h-4 w-4 rounded border-gray-300"
            />
            <div className="flex-1">
              <Label htmlFor="consent_complete" className="cursor-pointer">
                Ich bestätige, dass meine Angaben vollständig und wahrheitsgemäß sind.
              </Label>
              {errors.consent_complete && (
                <p className="text-sm text-red-600 mt-1">{errors.consent_complete.message}</p>
              )}
            </div>
          </div>

          <div className="flex items-start space-x-2">
            <input
              type="checkbox"
              id="consent_privacy"
              {...register("consent_privacy", {
                required: "Bitte akzeptieren Sie die Datenschutzhinweise",
              })}
              className="mt-1 h-4 w-4 rounded border-gray-300"
            />
            <div className="flex-1">
              <Label htmlFor="consent_privacy" className="cursor-pointer">
                Ich habe die Datenschutzhinweise gelesen und willige in die Verarbeitung meiner Daten ein.
              </Label>
              {errors.consent_privacy && (
                <p className="text-sm text-red-600 mt-1">{errors.consent_privacy.message}</p>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Error Display */}
      {error && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4">
          <p className="text-red-800 font-medium">{error}</p>
        </div>
      )}

      {/* Submit Button */}
      <div className="flex justify-end">
        <Button
          type="submit"
          disabled={isSubmitting}
          size="lg"
          className="px-8"
        >
          {isSubmitting ? "Wird gesendet..." : "Fragebogen absenden"}
        </Button>
      </div>
    </form>
  );
}
