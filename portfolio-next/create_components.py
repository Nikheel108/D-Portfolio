import os

os.makedirs('src/components', exist_ok=True)

boot_screen_code = '''"use client";
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
'''
with open('src/components/BootScreen.tsx', 'w', encoding='utf-8') as f:
    f.write(boot_screen_code)

print("Created BootScreen.tsx")
