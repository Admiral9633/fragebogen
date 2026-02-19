import * as React from "react"
import { cn } from "@/lib/utils"

interface RadioGroupContextValue {
  value?: string
  onValueChange?: (value: string) => void
  name?: string
}

const RadioGroupContext = React.createContext<RadioGroupContextValue>({})

interface RadioGroupProps extends React.HTMLAttributes<HTMLDivElement> {
  value?: string
  onValueChange?: (value: string) => void
  name?: string
  orientation?: "horizontal" | "vertical"
  error?: string
}

const RadioGroup = React.forwardRef<HTMLDivElement, RadioGroupProps>(
  ({ className, value, onValueChange, name, orientation = "vertical", error, children, ...props }, ref) => {
    return (
      <RadioGroupContext.Provider value={{ value, onValueChange, name }}>
        <div
          ref={ref}
          role="radiogroup"
          className={cn(
            "flex gap-2",
            orientation === "horizontal" ? "flex-row flex-wrap" : "flex-col",
            className
          )}
          {...props}
        >
          {children}
        </div>
        {error && <p className="mt-1.5 text-xs text-red-500">{error}</p>}
      </RadioGroupContext.Provider>
    )
  }
)
RadioGroup.displayName = "RadioGroup"

interface RadioGroupItemProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "type"> {
  value: string
  label?: React.ReactNode
}

const RadioGroupItem = React.forwardRef<HTMLInputElement, RadioGroupItemProps>(
  ({ className, value, label, id, ...props }, ref) => {
    const ctx = React.useContext(RadioGroupContext)
    const isChecked = ctx.value === value
    const inputId = id ?? `radio-${ctx.name}-${value}`

    return (
      <label
        htmlFor={inputId}
        className={cn(
          "flex items-center gap-3 px-4 py-3 rounded-xl border-2 cursor-pointer transition-all duration-150 select-none text-sm",
          isChecked
            ? "border-primary bg-primary/5 text-primary font-medium"
            : "border-gray-200 bg-white text-gray-700 hover:border-gray-300 hover:bg-gray-50",
          className
        )}
      >
        <input
          type="radio"
          id={inputId}
          ref={ref}
          name={ctx.name}
          value={value}
          checked={isChecked}
          onChange={() => ctx.onValueChange?.(value)}
          className="sr-only"
          {...props}
        />
        <span
          className={cn(
            "w-4 h-4 rounded-full border-2 flex-shrink-0 flex items-center justify-center",
            isChecked ? "border-primary" : "border-gray-300"
          )}
        >
          {isChecked && <span className="w-2 h-2 rounded-full bg-primary" />}
        </span>
        {label && <span>{label}</span>}
      </label>
    )
  }
)
RadioGroupItem.displayName = "RadioGroupItem"

export { RadioGroup, RadioGroupItem }
