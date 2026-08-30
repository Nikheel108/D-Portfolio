page_code = """
import BootScreen from "@/components/BootScreen";
import CursorGlow from "@/components/CursorGlow";
import NotebookCell from "@/components/NotebookCell";
import HeroTilt from "@/components/HeroTilt";
import { portfolioData } from "@/data/portfolio";

export default function Home() {
  return (
    <main className="min-h-screen">
      <BootScreen />
      <CursorGlow />
      
      {/* Background Icons */}
      <div className="fixed inset-0 pointer-events-none z-[-1] overflow-hidden">
        <i className="fa-brands fa-python absolute text-[#ffaa00] opacity-15 text-5xl parallax-icon" style={{ top: '15%', left: '8%', animation: 'floatAnim 15s infinite ease-in-out alternate' }}></i>
        <i className="fa-solid fa-microchip absolute text-[#ffaa00] opacity-15 text-5xl parallax-icon" style={{ top: '75%', left: '85%', animation: 'floatAnim 15s infinite ease-in-out alternate 1.5s' }}></i>
        <i className="fa-solid fa-robot absolute text-[#ffaa00] opacity-15 text-5xl parallax-icon" style={{ top: '40%', left: '80%', animation: 'floatAnim 15s infinite ease-in-out alternate 3s' }}></i>
        <i className="fa-solid fa-code absolute text-[#ffaa00] opacity-15 text-5xl parallax-icon" style={{ top: '60%', left: '5%', animation: 'floatAnim 15s infinite ease-in-out alternate 1s' }}></i>
      </div>

      <div className="max-w-[760px] mx-auto px-4 md:px-[30px] pt-[80px]">
        {/* Home */}
        <NotebookCell id="home" cellNumber={1}>
          <div className="flex flex-col sm:flex-row sm:items-start gap-5">
            <div>
              <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider">portfolio.load(<span className="text-[#ffaa00]">"nikheel_ck"</span>)</div>
              <h1 className="text-3xl font-bold mb-4">Hi, I'm <span className="text-[#ffaa00]">Nikheel C K.</span></h1>
              <p className="text-[#a4a9b6] mb-5 text-[15px] leading-relaxed max-w-[500px]">{portfolioData.hero.tagline}</p>
              <div className="flex flex-wrap items-center gap-3 mt-4">
                <a href="#about" className="px-4 py-2 bg-[#ffaa00] text-[#0B0D10] font-mono text-xs rounded hover:bg-[#ffbd2e] transition">about --me</a>
                <a href="#contact" className="px-4 py-2 border border-[#2d3139] text-[#e1e4e8] font-mono text-xs rounded hover:border-[#ffaa00] transition">contact --send</a>
              </div>
            </div>
            <HeroTilt src="https://nikheel108.github.io/Digital-Portfolio/images/profile.jpg" alt="Profile" />
          </div>
        </NotebookCell>

        {/* About */}
        <NotebookCell id="about" cellNumber={2}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># about</div>
          <h2 className="text-2xl font-bold mb-3">Hello, I'm Nikheel C Khadakabhavi.</h2>
          {portfolioData.about.description.map((p, i) => (
            <p key={i} className="text-[#a4a9b6] mb-4 text-[15px] leading-relaxed">{p}</p>
          ))}
          <div className="flex flex-wrap gap-2 mt-4">
            {portfolioData.skills.core.slice(0,4).map(t => (
              <span key={t} className="px-2 py-1 bg-[#1c1f26] border border-[#2d3139] rounded text-[11px] font-mono text-[#a4a9b6]">{t}</span>
            ))}
          </div>
        </NotebookCell>

        <NotebookCell cellNumber={3}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># print(nikheel.stats)</div>
          <div className="font-mono text-[13px] bg-[#12151A] border border-[#2d3139] p-4 rounded text-[#e1e4e8]">
            <div className="text-[#a4a9b6]">&#123;</div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">'10th_grade'</span>: <span className="text-[#27c93f]">'{portfolioData.about.stats["10th_grade"]}'</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">'12th_grade'</span>: <span className="text-[#27c93f]">'{portfolioData.about.stats["12th_grade"]}'</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">'cgpa'</span>: <span className="text-[#79b8ff]">{portfolioData.about.stats.cgpa}</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">'languages'</span>: <span className="text-[#e1e4e8]">[ {portfolioData.about.stats.languages.map(l => `'${l}'`).join(', ')} ]</span>,
            </div>
            <div className="text-[#a4a9b6]">&#125;</div>
          </div>
        </NotebookCell>

        {/* Projects */}
        <NotebookCell id="projects" cellNumber={7}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># projects</div>
          <p className="text-[#a4a9b6] mb-6 text-[15px]">A couple of things I've shipped — AI and web, end to end.</p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            {portfolioData.projects.map((proj, i) => (
              <div key={i} className="border border-[#2d3139] rounded-[6px] overflow-hidden bg-[#12151A] flex flex-col">
                <div className="h-7 bg-[#0B0D10] border-b border-[#2d3139] flex items-center px-3 gap-1.5 font-mono text-[10.5px] text-[#a4a9b6]">
                  <span className="w-2.5 h-2.5 rounded-full bg-[#ff5f56]"></span>
                  <span className="w-2.5 h-2.5 rounded-full bg-[#ffbd2e]"></span>
                  <span className="w-2.5 h-2.5 rounded-full bg-[#27c93f]"></span>
                  <span className="ml-2">{proj.filename}</span>
                </div>
                {proj.image && (
                  <img src={proj.image} alt={proj.title} className="w-full h-32 object-cover border-b border-[#2d3139]" />
                )}
                <div className="p-5 flex flex-col flex-1">
                  <h3 className="font-semibold text-[17px] mb-2">{proj.title}</h3>
                  <p className="text-[#a4a9b6] text-[13.5px] leading-relaxed mb-4 flex-1">{proj.description}</p>
                  <div className="flex flex-wrap gap-1.5 mb-4">
                    {proj.tags.map(t => <span key={t} className="px-2 py-0.5 bg-[#1c1f26] border border-[#2d3139] rounded text-[10px] font-mono text-[#a4a9b6]">{t}</span>)}
                  </div>
                  <div className="flex gap-2">
                    {proj.github && <a href={proj.github} className="text-[12px] font-mono border border-[#2d3139] px-3 py-1.5 rounded hover:border-[#ffaa00] transition">view code</a>}
                    {proj.drive && <a href={proj.drive} className="text-[12px] font-mono border border-[#2d3139] px-3 py-1.5 rounded hover:border-[#ffaa00] transition">view drive</a>}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </NotebookCell>
      </div>
    </main>
  );
}
"""
with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(page_code)
