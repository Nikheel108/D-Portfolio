"use client";
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
        background: 
adial-gradient(circle 400px at px px, , transparent 80%),
        mixBlendMode: isLight ? 'multiply' : 'screen'
      }}
    />
  );
}
