"use client"

import * as React from "react"
import {
  ClipboardListIcon,
  FileTextIcon,
  LayoutDashboardIcon,
  MailIcon,
  ShieldIcon,
} from "lucide-react"

import { NavMain } from "@/components/nav-main"
import { NavSecondary } from "@/components/nav-secondary"
import { NavUser } from "@/components/nav-user"
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
} from "@/components/ui/sidebar"

const navMain = [
  {
    title: "Übersicht",
    url: "#overview",
    icon: LayoutDashboardIcon,
  },
  {
    title: "Neue Einladung",
    url: "#create",
    icon: MailIcon,
  },
  {
    title: "Alle Sessions",
    url: "#sessions",
    icon: ClipboardListIcon,
  },
  {
    title: "PDF-Berichte",
    url: "#sessions",
    icon: FileTextIcon,
  },
]

interface AppSidebarProps extends React.ComponentProps<typeof Sidebar> {
  onLogout?: () => void
}

export function AppSidebar({ onLogout, ...props }: AppSidebarProps) {
  return (
    <Sidebar collapsible="offcanvas" {...props}>
      <SidebarHeader>
        <SidebarMenu>
          <SidebarMenuItem>
            <SidebarMenuButton
              asChild
              className="data-[slot=sidebar-menu-button]:!p-1.5"
            >
              <a href="/admin">
                <ShieldIcon className="h-5 w-5" />
                <span className="text-base font-semibold">Fragebogen Admin</span>
              </a>
            </SidebarMenuButton>
          </SidebarMenuItem>
        </SidebarMenu>
      </SidebarHeader>
      <SidebarContent>
        <NavMain items={navMain} />
        <NavSecondary items={[]} className="mt-auto" />
      </SidebarContent>
      <SidebarFooter>
        <NavUser
          user={{ name: "Administrator", email: "admin", avatar: "" }}
          onLogout={onLogout}
        />
      </SidebarFooter>
    </Sidebar>
  )
}

