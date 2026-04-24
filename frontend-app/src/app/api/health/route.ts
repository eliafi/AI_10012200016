const BACKEND = process.env.API_URL ?? "http://localhost:8000";

export async function GET() {
  try {
    const upstream = await fetch(`${BACKEND}/health`, { method: "GET" });
    const data = await upstream.json();
    return Response.json(data, { status: upstream.status });
  } catch {
    return Response.json({ status: "unavailable" }, { status: 503 });
  }
}
