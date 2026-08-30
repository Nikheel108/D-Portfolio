import os
os.makedirs('src/components', exist_ok=True)
os.makedirs('src/app', exist_ok=True)

# BootScreen
with open('src/components/BootScreen.tsx', 'w', encoding='utf-8') as f:
    f.write(""""use client";
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

export default function BootScreen() {
  const [lines, setLines] = useState<string[]>([]);
  const [show, setShow] = useState(true);

  useEffect(() => {
    const sequence = [
      "> Loading Nikheel_CK.ipynb...",
      "> Initializing AI Models...",
      "> Fetching Edge Sensors...",
      "> Access Granted."
    ];
    let delay = 0;
    
    sequence.forEach((line) => {
      setTimeout(() => {
        setLines((prev) => [...prev, line]);
      }, delay);
      delay += 600 + Math.random() * 400;
    });

    setTimeout(() => {
      setShow(false);
    }, delay + 500);
  }, []);

  return (
    <AnimatePresence>
      {show && (
        <motion.div 
          initial={{ opacity: 1 }}
          exit={{ opacity: 0, transition: { duration: 0.6 } }}
          className="fixed inset-0 z-[99999] bg-[#0B0D10] text-[#4af626] flex flex-col justify-center items-start p-10 font-mono text-sm pointer-events-none"
        >
          {lines.map((line, i) => (
            <motion.div 
              key={i}
              initial={{ maxWidth: 0 }}
              animate={{ maxWidth: "100%" }}
              transition={{ duration: 0.5, ease: "linear" }}
              className="mb-2 whitespace-nowrap overflow-hidden border-r-2 border-[#4af626] pr-1"
              style={{ animation: "blink-caret 0.5s step-end infinite" }}
            >
              {line}
            </motion.div>
          ))}
        </motion.div>
      )}
    </AnimatePresence>
  );
}
""")

# CursorGlow
with open('src/components/CursorGlow.tsx', 'w', encoding='utf-8') as f:
    f.write(""""use client";
import { useEffect, useState } from "react";
import { useTheme } from "next-themes";

export default function CursorGlow() {
  const [position, setPosition] = useState({ x: -1000, y: -1000 });
  const { theme, resolvedTheme } = useTheme();

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setPosition({ x: e.clientX, y: e.clientY });
    };
    window.addEventListener("mousemove", handleMouseMove);
    return () => window.removeEventListener("mousemove", handleMouseMove);
  }, []);

  const currentTheme = theme === "system" ? resolvedTheme : theme;
  const isLight = currentTheme === "light";

  return (
    <div 
      className="fixed inset-0 pointer-events-none z-[9999] transition-colors duration-100"
      style={{
        background: `radial-gradient(circle 400px at ${position.x}px ${position.y}px, ${isLight ? 'rgba(0,0,0,0.03)' : 'rgba(255,170,0,0.05)'}, transparent 80%)`,
        mixBlendMode: isLight ? 'multiply' : 'screen'
      }}
    />
  );
}
""")

# NotebookCell
with open('src/components/NotebookCell.tsx', 'w', encoding='utf-8') as f:
    f.write(""""use client";
import { useState } from "react";
import { motion } from "framer-motion";

interface NotebookCellProps {
  id?: string;
  cellNumber: number | string;
  children: React.ReactNode;
}

export default function NotebookCell({ id, cellNumber, children }: NotebookCellProps) {
  const [executed, setExecuted] = useState(false);
  const [loading, setLoading] = useState(true);

  return (
    <section id={id} className="py-[30px] border-b border-[#2d3139] last:border-0 scroll-mt-[120px]">
      <motion.div 
        initial={{ opacity: 0, y: 18 }}
        whileInView={{ opacity: 1, y: 0 }}
        viewport={{ once: true, amount: 0.15 }}
        onViewportEnter={() => {
          if(!executed) {
            setExecuted(true);
            setTimeout(() => setLoading(false), 600 + Math.random() * 400);
          }
        }}
        transition={{ duration: 0.6, ease: "easeOut" }}
        className="grid grid-cols-[var(--gutter)_1fr] gap-[6px_20px]"
      >
        <div className={`font-mono text-xs pt-1 whitespace-nowrap transition-colors ${loading && executed ? 'text-[#ffaa00]' : 'text-[rgba(255,170,0,0.5)]'}`}>
          In [{loading && executed ? '*' : cellNumber}]:
        </div>
        
        <div>
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: loading ? 0 : 1 }}
            transition={{ duration: 0.3 }}
          >
            {children}
          </motion.div>
        </div>
      </motion.div>
    </section>
  );
}
""")

# HeroTilt
with open('src/components/HeroTilt.tsx', 'w', encoding='utf-8') as f:
    f.write(""""use client";
import { useRef } from "react";
import { motion, useMotionValue, useSpring, useTransform } from "framer-motion";

export default function HeroTilt({ src, alt }: { src: string, alt: string }) {
  const ref = useRef<HTMLDivElement>(null);
  
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  const mouseXSpring = useSpring(x, { stiffness: 300, damping: 30 });
  const mouseYSpring = useSpring(y, { stiffness: 300, damping: 30 });

  const rotateX = useTransform(mouseYSpring, [-0.5, 0.5], ["10deg", "-10deg"]);
  const rotateY = useTransform(mouseXSpring, [-0.5, 0.5], ["-10deg", "10deg"]);

  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if (!ref.current) return;
    const rect = ref.current.getBoundingClientRect();
    const width = rect.width;
    const height = rect.height;
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    const xPct = mouseX / width - 0.5;
    const yPct = mouseY / height - 0.5;
    x.set(xPct);
    y.set(yPct);
  };

  const handleMouseLeave = () => {
    x.set(0);
    y.set(0);
  };

  return (
    <div className="mt-[20px] mb-[15px] sm:mt-0 max-w-[200px]" style={{ perspective: 1000 }}>
      <motion.div
        ref={ref}
        onMouseMove={handleMouseMove}
        onMouseLeave={handleMouseLeave}
        style={{
          rotateX,
          rotateY,
          transformStyle: "preserve-3d",
        }}
        className="border border-[#2d3139] rounded-[6px] overflow-hidden bg-[#12151A]"
      >
        <div className="h-6 bg-[#0B0D10] border-b border-[#2d3139] flex items-center px-2 gap-1.5" style={{ transform: "translateZ(30px)" }}>
          <span className="w-2.5 h-2.5 rounded-full bg-[#ff5f56]"></span>
          <span className="w-2.5 h-2.5 rounded-full bg-[#ffbd2e]"></span>
          <span className="w-2.5 h-2.5 rounded-full bg-[#27c93f]"></span>
        </div>
        <img 
          src={src} 
          alt={alt} 
          className="w-full h-auto block filter grayscale transition-all duration-300 hover:grayscale-0 hover:brightness-110" 
          style={{ transform: "translateZ(20px)" }}
        />
      </motion.div>
    </div>
  );
}
""")

# Layout
with open('src/app/layout.tsx', 'w', encoding='utf-8') as f:
    f.write("""import type { Metadata } from "next";
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
      <body className={`${spaceGrotesk.variable} ${jetBrainsMono.variable} ${inter.variable} bg-[#0B0D10] text-[#e1e4e8] font-sans antialiased`}>
        <Navbar />
        {children}
      </body>
    </html>
  );
}
""")
