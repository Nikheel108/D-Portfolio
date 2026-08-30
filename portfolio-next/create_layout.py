navbar_code = '''"use client";
import { useState } from "react";

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <>
      <header className="sticky top-0 z-[800] bg-[#12151A]/70 backdrop-blur-md border-b border-[#2d3139]">
        <div className="max-w-[760px] mx-auto px-4 md:px-[30px] h-14 flex items-center">
          <div className="flex gap-1.5 mr-4">
            <span className="w-3 h-3 rounded-full bg-[#ff5f56]"></span>
            <span className="w-3 h-3 rounded-full bg-[#ffbd2e]"></span>
            <span className="w-3 h-3 rounded-full bg-[#27c93f]"></span>
          </div>
          <div className="font-mono text-xs text-[#a4a9b6] flex-1">nikheel_ck_portfolio<b className="text-[#e1e4e8]">.ipynb</b></div>
          
          <button 
            className="md:hidden text-[#a4a9b6] hover:text-[#e1e4e8] p-2"
            onClick={() => setMenuOpen(!menuOpen)}
          >
            <i className="fa-solid fa-bars text-lg"></i>
          </button>
        </div>
      </header>

      {/* Mobile Menu */}
      {menuOpen && (
        <div className="md:hidden fixed top-14 left-0 w-full bg-[#12151A]/90 backdrop-blur-md border-b border-[#2d3139] z-[790]">
          {['home', 'about', 'projects', 'education', 'internships', 'publications', 'contact'].map(link => (
            <a 
              key={link} 
              href={#} 
              onClick={() => setMenuOpen(false)}
              className="block px-6 py-3 font-mono text-[13px] uppercase tracking-wider text-[#a4a9b6] border-t border-[#2d3139] hover:bg-[#1c1f26]"
            >
              {link}
            </a>
          ))}
        </div>
      )}

      {/* Desktop Sticky Nav */}
      <nav className="hidden md:block sticky top-14 z-[795] bg-[#0B0D10]/80 backdrop-blur-md border-b border-[#2d3139]">
        <div className="max-w-[760px] mx-auto px-4 md:px-[30px] flex gap-6 overflow-x-auto">
          {['home', 'about', 'projects', 'education', 'internships', 'publications', 'contact'].map(link => (
            <a 
              key={link} 
              href={#} 
              className="py-3 font-mono text-[12px] uppercase tracking-wider text-[#a4a9b6] hover:text-[#ffaa00] transition whitespace-nowrap"
            >
              {link}
            </a>
          ))}
        </div>
      </nav>
    </>
  );
}
'''
with open('src/components/Navbar.tsx', 'w', encoding='utf-8') as f:
    f.write(navbar_code)

layout_code = '''
import type { Metadata } from "next";
import { Space_Grotesk, JetBrains_Mono, Inter } from "next/font/google";
import "./globals.css";
import Navbar from "@/components/Navbar";

const spaceGrotesk = Space_Grotesk({ subsets: ["latin"], variable: "--font-space" });
const jetBrainsMono = JetBrains_Mono({ subsets: ["latin"], variable: "--font-mono" });
const inter = Inter({ subsets: ["latin"], variable: "--font-inter" });

export const metadata: Metadata = {
  title: "Nikheel C K — AI/ML Student | Portfolio",
  description: "Third-year B.Tech student in Artificial Intelligence & Machine Learning at MIT Academy of Engineering.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth">
      <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css" />
      </head>
      <body className={${spaceGrotesk.variable}   bg-[#0B0D10] text-[#e1e4e8] font-sans antialiased}>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
'''
with open('src/app/layout.tsx', 'w', encoding='utf-8') as f:
    f.write(layout_code)

print("Created Navbar and Layout")
