import type { RetrievedDocument } from "@/lib/types";
import SourceCard from "./SourceCard";
import { SkeletonText } from "@/components/ui/Skeleton";
import Skeleton from "@/components/ui/Skeleton";

interface Props {
  docs: RetrievedDocument[];
  isLoading?: boolean;
}

function SkeletonCard() {
  return (
    <div className="ballot-glass p-4 flex flex-col gap-3">
      <div className="flex justify-between">
        <div className="flex gap-2 items-center">
          <Skeleton width="w-6" height="h-6" pill />
          <Skeleton width="w-28" height="h-3" />
        </div>
        <div className="flex gap-1.5">
          <Skeleton width="w-14" height="h-5" pill />
          <Skeleton width="w-14" height="h-5" pill />
        </div>
      </div>
      <Skeleton height="h-1.5" />
      <SkeletonText lines={3} />
    </div>
  );
}

/**
 * Renders the full list of retrieved chunks.
 * Shows skeleton cards while the backend is responding.
 */
export default function SourceList({ docs, isLoading = false }: Props) {
  if (isLoading) {
    return (
      <div className="flex flex-col gap-3">
        {[1, 2, 3].map((i) => <SkeletonCard key={i} />)}
      </div>
    );
  }

  if (docs.length === 0) {
    return (
      <p className="text-sm text-text-muted text-center py-6">
        No sources retrieved.
      </p>
    );
  }

  return (
    <div className="flex flex-col gap-3">
      {docs.map((doc) => (
        <SourceCard key={doc.chunk_id} doc={doc} />
      ))}
    </div>
  );
}
