import * as React from "react"
import { cn } from "@/lib/utils"

interface CheckboxProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, "type"> {
  label?: React.ReactNode
  error?: string
}

const Checkbox = React.forwardRef<HTMLInputElement, CheckboxProps>(
  ({ className, label, error, id, ...props }, ref) => {
    return (
      <div className="space-y-1">
        <label
          htmlFor={id}
          className={cn(
            "flex items-start gap-3 cursor-pointer rounded-lg border-2 px-4 py-3 transition-all",
            props.checked
              ? "border-primary bg-primary/5"
              : "border-gray-200 bg-white hover:border-gray-300",
            error && "border-red-400"
          )}
        >
          <div className="relative mt-0.5 flex-shrink-0">
            <input
              type="checkbox"
              id={id}
              ref={ref}
              className="sr-only peer"
              {...props}
            />
            <div
              className={cn(
                "w-5 h-5 rounded border-2 flex items-center justify-center transition-all",
                props.checked
                  ? "bg-primary border-primary"
                  : "bg-white border-gray-300 peer-focus-visible:ring-2 peer-focus-visible:ring-primary"
              )}
            >
              {props.checked && (
                <svg
                  className="w-3 h-3 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  strokeWidth={3}
                >
                  <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
                </svg>
              )}
            </div>
          </div>
          {label && (
            <span className="text-sm text-gray-700 leading-relaxed">{label}</span>
          )}
        </label>
        {error && <p className="text-xs text-red-500 px-1">{error}</p>}
      </div>
    )
  }
)
Checkbox.displayName = "Checkbox"

export { Checkbox }
