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
              <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider">portfolio.load(&quot;nikheel_ck&quot;)</div>
              <h1 className="text-3xl font-bold mb-4">Hi, I&apos;m <span className="text-[#ffaa00]">Nikheel C K.</span></h1>
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
          <h2 className="text-2xl font-bold mb-3">Hello, I&apos;m Nikheel C Khadakabhavi.</h2>
          {portfolioData.about.description.map((p, i) => (
            <p key={i} className="text-[#a4a9b6] mb-4 text-[15px] leading-relaxed">{p}</p>
          ))}
          <div className="flex flex-wrap gap-2 mt-4">
            {portfolioData.skills.core.slice(0,4).map(t => (
              <span key={t} className="px-2 py-1 bg-[#1c1f26] border border-[#2d3139] rounded text-[11px] font-mono text-[#a4a9b6]">{t}</span>
            ))}
          </div>
        </NotebookCell>

        {/* Stats */}
        <NotebookCell cellNumber={3}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># print(nikheel.stats)</div>
          <div className="font-mono text-[13px] bg-[#12151A] border border-[#2d3139] p-4 rounded text-[#e1e4e8]">
            <div className="text-[#a4a9b6]">&#123;</div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">&apos;10th_grade&apos;</span>: <span className="text-[#27c93f]">&apos;{portfolioData.about.stats["10th_grade"]}&apos;</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">&apos;12th_grade&apos;</span>: <span className="text-[#27c93f]">&apos;{portfolioData.about.stats["12th_grade"]}&apos;</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">&apos;cgpa&apos;</span>: <span className="text-[#79b8ff]">{portfolioData.about.stats.cgpa}</span>,
            </div>
            <div className="pl-4">
              <span className="text-[#ff5f56]">&apos;languages&apos;</span>: <span className="text-[#e1e4e8]">[ {portfolioData.about.stats.languages.map(l => `\'${l}\'`).join(', ')} ]</span>,
            </div>
            <div className="text-[#a4a9b6]">&#125;</div>
          </div>
        </NotebookCell>

        {/* Education */}
        <NotebookCell id="education" cellNumber={4}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># education</div>
          <div className="space-y-6">
            {portfolioData.education.map((edu, i) => (
              <div key={i} className="border-l-2 border-[#2d3139] pl-4 relative">
                <div className="absolute w-3 h-3 bg-[#ffaa00] rounded-full -left-[7px] top-1.5"></div>
                <h3 className="font-semibold text-lg">{edu.title}</h3>
                <div className="text-[#ffaa00] font-mono text-xs mb-2">{edu.date} <span className="ml-2 px-2 py-0.5 bg-[#1c1f26] border border-[#2d3139] rounded text-[10px]">{edu.tag}</span></div>
                <p className="text-[#a4a9b6] text-[14px] leading-relaxed">{edu.description}</p>
              </div>
            ))}
          </div>
        </NotebookCell>

        {/* Internships */}
        <NotebookCell id="internships" cellNumber={5}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># internships</div>
          <div className="space-y-6">
            {portfolioData.internships.map((intern, i) => (
              <div key={i} className="border-l-2 border-[#2d3139] pl-4 relative">
                <div className="absolute w-3 h-3 bg-[#ffaa00] rounded-full -left-[7px] top-1.5"></div>
                <h3 className="font-semibold text-lg">{intern.title}</h3>
                <div className="text-[#ffaa00] font-mono text-xs mb-2">{intern.date}</div>
                <p className="text-[#a4a9b6] text-[14px] leading-relaxed mb-3">{intern.description}</p>
                <div className="flex flex-wrap gap-1.5">
                  {intern.tags.map(t => <span key={t} className="px-2 py-0.5 bg-[#1c1f26] border border-[#2d3139] rounded text-[10px] font-mono text-[#a4a9b6]">{t}</span>)}
                </div>
              </div>
            ))}
          </div>
        </NotebookCell>

        {/* Publications */}
        <NotebookCell id="publications" cellNumber={6}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># publications & research</div>
          <div className="grid gap-4">
            {portfolioData.publications.map((pub, i) => (
              <div key={i} className="bg-[#12151A] border border-[#2d3139] p-5 rounded-[6px]">
                <h3 className="font-semibold text-md mb-1">{pub.title}</h3>
                <div className="text-[#ffaa00] font-mono text-xs mb-3">{pub.date}</div>
                <p className="text-[#a4a9b6] text-[14px] leading-relaxed mb-3">{pub.description}</p>
                <div className="flex flex-wrap gap-1.5">
                  {pub.tags.map(t => <span key={t} className="px-2 py-0.5 bg-[#1c1f26] border border-[#2d3139] rounded text-[10px] font-mono text-[#a4a9b6]">{t}</span>)}
                </div>
              </div>
            ))}
          </div>
        </NotebookCell>

        {/* Projects */}
        <NotebookCell id="projects" cellNumber={7}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># projects</div>
          <p className="text-[#a4a9b6] mb-6 text-[15px]">A couple of things I&apos;ve shipped — AI and web, end to end.</p>
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

        {/* Contact */}
        <NotebookCell id="contact" cellNumber={8}>
          <div className="font-mono text-[12px] text-[#ffaa00] mb-2 uppercase tracking-wider"># contact</div>
          <div className="bg-[#12151A] border border-[#2d3139] p-6 rounded-[6px]">
            <h2 className="text-xl font-bold mb-4">Let&apos;s Connect</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
              <a href={`mailto:${portfolioData.contact.email}`} className="flex items-center gap-3 text-[#a4a9b6] hover:text-[#ffaa00] transition">
                <i className="fa-solid fa-envelope w-5"></i>
                <span className="text-[14px]">{portfolioData.contact.email}</span>
              </a>
              <div className="flex items-center gap-3 text-[#a4a9b6]">
                <i className="fa-solid fa-phone w-5"></i>
                <span className="text-[14px]">{portfolioData.contact.phone}</span>
              </div>
              <div className="flex items-center gap-3 text-[#a4a9b6]">
                <i className="fa-solid fa-location-dot w-5"></i>
                <span className="text-[14px]">{portfolioData.contact.location}</span>
              </div>
            </div>
            
            <div className="flex gap-4 border-t border-[#2d3139] pt-4">
              <a href={portfolioData.contact.github} target="_blank" rel="noreferrer" className="w-10 h-10 rounded-full bg-[#1c1f26] border border-[#2d3139] flex items-center justify-center text-[#a4a9b6] hover:text-[#ffaa00] hover:border-[#ffaa00] transition">
                <i className="fa-brands fa-github text-lg"></i>
              </a>
              <a href={portfolioData.contact.linkedin} target="_blank" rel="noreferrer" className="w-10 h-10 rounded-full bg-[#1c1f26] border border-[#2d3139] flex items-center justify-center text-[#a4a9b6] hover:text-[#ffaa00] hover:border-[#ffaa00] transition">
                <i className="fa-brands fa-linkedin text-lg"></i>
              </a>
              <a href={portfolioData.contact.instagram} target="_blank" rel="noreferrer" className="w-10 h-10 rounded-full bg-[#1c1f26] border border-[#2d3139] flex items-center justify-center text-[#a4a9b6] hover:text-[#ffaa00] hover:border-[#ffaa00] transition">
                <i className="fa-brands fa-instagram text-lg"></i>
              </a>
            </div>
          </div>
        </NotebookCell>
        
        {/* Footer */}
        <div className="py-8 text-center font-mono text-[11px] text-[#a4a9b6]">
          &gt; Execution completed successfully. <br/>
          &copy; {new Date().getFullYear()} Nikheel C K.
        </div>
      </div>
    </main>
  );
}
"""
with open('src/app/page.tsx', 'w', encoding='utf-8') as f:
    f.write(page_code)
