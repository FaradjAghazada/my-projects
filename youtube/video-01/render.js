// Renders scene.html frame by frame into a 1080x1920 MP4 (YouTube Shorts format).
// Usage: node render.js [out.mp4]
const { chromium } = require("playwright");
const { spawn } = require("child_process");
const path = require("path");

const FPS = 30, DURATION = 25;
const out = process.argv[2] || path.join(__dirname, "video-01.mp4");

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.goto("file://" + path.join(__dirname, "scene.html"));
  await page.evaluate(() => document.fonts.ready);

  const ff = spawn("ffmpeg", [
    "-y", "-f", "image2pipe", "-framerate", String(FPS), "-i", "-",
    "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "medium",
    "-c:a", "aac", "-shortest", "-movflags", "+faststart", out,
  ], { stdio: ["pipe", "inherit", "inherit"] });

  const total = FPS * DURATION;
  for (let i = 0; i < total; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await page.screenshot({ type: "png" });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once("drain", r));
  }
  ff.stdin.end();
  await new Promise(r => ff.on("close", r));
  await browser.close();
  console.log("wrote", out);
})();
