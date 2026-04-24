/**
 * The Black Star of Africa — a large, subtle SVG star watermark placed
 * behind all page content. Opacity 0.04 keeps it barely perceptible,
 * reinforcing the "Ghana Civic Premium" identity without distracting.
 * aria-hidden so screen readers skip it entirely.
 */
export default function BlackStarBg() {
  return (
    <div
      aria-hidden="true"
      className="pointer-events-none fixed inset-0 z-0 flex items-center justify-center overflow-hidden"
    >
      <svg
        viewBox="0 0 200 200"
        className="w-[min(80vw,80vh)] h-[min(80vw,80vh)]"
        style={{ opacity: 0.04 }}
        fill="white"
        xmlns="http://www.w3.org/2000/svg"
      >
        {/* Five-pointed star — the Black Star of Ghana's national flag */}
        <polygon points="100,10 120.6,73.5 186.6,73.5 134.4,110.3 155,173.8 100,137 45,173.8 65.6,110.3 13.4,73.5 79.4,73.5" />
      </svg>
    </div>
  );
}
