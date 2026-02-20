"use client"

import * as React from "react"
import * as CheckboxPrimitive from "@radix-ui/react-checkbox"
import { Check } from "lucide-react"

import { cn } from "@/lib/utils"

type CheckboxProps = Omit<React.ComponentPropsWithoutRef<typeof CheckboxPrimitive.Root>, "onChange" | "checked"> & {
  label?: React.ReactNode
  error?: string
  checked?: boolean | "indeterminate"
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void
}

const Checkbox = React.forwardRef<
  React.ElementRef<typeof CheckboxPrimitive.Root>,
  CheckboxProps
>(({ className, label, error, checked, onChange, id, ...props }, ref) => {
  const box = (
    <CheckboxPrimitive.Root
      ref={ref}
      id={id}
      checked={checked}
      onCheckedChange={(val) => {
        if (onChange) {
          const syntheticEvent = { target: { checked: val === true } } as React.ChangeEvent<HTMLInputElement>
          onChange(syntheticEvent)
        }
      }}
      className={cn(
        "grid place-content-center peer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground",
        className
      )}
      {...props}
    >
      <CheckboxPrimitive.Indicator className={cn("grid place-content-center text-current")}>
        <Check className="h-4 w-4" />
      </CheckboxPrimitive.Indicator>
    </CheckboxPrimitive.Root>
  )

  if (!label && !error) return box

  return (
    <div className="space-y-1">
      <div className="flex items-start gap-2">
        {box}
        {label && (
          <label htmlFor={id} className="text-sm leading-snug cursor-pointer">
            {label}
          </label>
        )}
      </div>
      {error && <p className="text-sm text-destructive">{error}</p>}
    </div>
  )
})
Checkbox.displayName = CheckboxPrimitive.Root.displayName

export { Checkbox }
