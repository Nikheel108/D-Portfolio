"use client";
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
