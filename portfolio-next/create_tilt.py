hero_tilt_code = '''"use client";
import { useState, useRef } from "react";
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
'''
with open('src/components/HeroTilt.tsx', 'w', encoding='utf-8') as f:
    f.write(hero_tilt_code)
print("Created HeroTilt.tsx")
