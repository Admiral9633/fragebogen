"use client";

import * as React from "react";
import { Check, ChevronsUpDown } from "lucide-react";
import {
  AL, AM, AT, AZ, BA, BE, BG, BY, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GE,
  GR, HR, HU, IE, IN, IS, IT, KG, KZ, LT, LU, LV, MD, ME, MK, MT, NL, NO, PK,
  PL, PT, RO, RS, RU, SE, SI, SK, SY, TJ, TM, TR, UA, UZ, XK,
  type FlagComponent,
} from "country-flag-icons/react/3x2";

import { cn } from "@/lib/utils";
import { COUNTRIES, type Country } from "@/lib/countries";
import { Button } from "@/components/ui/button";
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from "@/components/ui/command";
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover";

/** Lokal gebündelte SVG-Flaggen (country-flag-icons) – keine externen Requests. */
const FLAGS: Record<string, FlagComponent> = {
  al: AL, am: AM, at: AT, az: AZ, ba: BA, be: BE, bg: BG, by: BY, ch: CH,
  cy: CY, cz: CZ, de: DE, dk: DK, ee: EE, es: ES, fi: FI, fr: FR, gb: GB,
  ge: GE, gr: GR, hr: HR, hu: HU, ie: IE, in: IN, is: IS, it: IT, kg: KG,
  kz: KZ, lt: LT, lu: LU, lv: LV, md: MD, me: ME, mk: MK, mt: MT, nl: NL,
  no: NO, pk: PK, pl: PL, pt: PT, ro: RO, rs: RS, ru: RU, se: SE, si: SI,
  sk: SK, sy: SY, tj: TJ, tm: TM, tr: TR, ua: UA, uz: UZ, xk: XK,
};

function Flag({ code, className }: { code: string; className?: string }) {
  const Component = FLAGS[code];
  if (!Component) return null;
  return (
    <Component
      aria-hidden
      className={cn("h-4 w-6 shrink-0 rounded-[2px] border border-border/40", className)}
    />
  );
}

interface LanguageSelectProps {
  /** Ländercode (lib/countries.ts) */
  value: string;
  onSelect: (countryCode: string, lang: string) => void;
  /** Übersetztes Label für aria/Trigger ("Sprache") */
  label: string;
}

export function LanguageSelect({ value, onSelect, label }: LanguageSelectProps) {
  const [open, setOpen] = React.useState(false);
  const selected: Country | undefined = COUNTRIES.find((c) => c.code === value);

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          aria-label={label}
          className="h-9 max-w-44 justify-between gap-2 px-2.5"
        >
          {selected ? (
            <span className="flex min-w-0 items-center gap-2">
              <Flag code={selected.code} />
              <span className="hidden truncate text-sm sm:inline">{selected.name}</span>
            </span>
          ) : (
            <span className="text-sm text-muted-foreground">{label}</span>
          )}
          <ChevronsUpDown className="size-3.5 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent align="end" className="w-72 p-0">
        <Command>
          <CommandInput placeholder={`${label}…`} />
          <CommandList className="max-h-72">
            <CommandEmpty>—</CommandEmpty>
            <CommandGroup>
              {COUNTRIES.map((country) => (
                <CommandItem
                  key={country.code}
                  value={country.name}
                  keywords={[country.nameDe, country.code]}
                  onSelect={() => {
                    onSelect(country.code, country.lang);
                    setOpen(false);
                  }}
                  className="min-h-10"
                >
                  <Flag code={country.code} />
                  <span className="min-w-0 flex-1 truncate">{country.name}</span>
                  {country.nameDe !== country.name && (
                    <span className="truncate text-xs text-muted-foreground">
                      {country.nameDe}
                    </span>
                  )}
                  <Check
                    className={cn(
                      "ml-1 size-4 shrink-0",
                      value === country.code ? "opacity-100" : "opacity-0"
                    )}
                  />
                </CommandItem>
              ))}
            </CommandGroup>
          </CommandList>
        </Command>
      </PopoverContent>
    </Popover>
  );
}
