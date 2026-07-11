from __future__ import annotations

import argparse
from pathlib import Path

from src.vectorless_rag import (
    DEFAULT_DATA_DIR,
    DEFAULT_INDEX_PATH,
    VectorlessRAG,
    build_index,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Vectorless RAG for insurance plan facts"
    )
    parser.add_argument(
        "question", nargs="?", help="Question to ask against the insurance data"
    )
    parser.add_argument(
        "--rebuild-index",
        action="store_true",
        help="Rebuild the lexical index before answering",
    )
    parser.add_argument(
        "--index-path",
        default=str(DEFAULT_INDEX_PATH),
        help="Path to the SQLite index file",
    )
    parser.add_argument(
        "--data-dir",
        default=str(DEFAULT_DATA_DIR),
        help="Path to the CSV data directory",
    )
    parser.add_argument(
        "--max-rows-per-table",
        type=int,
        default=None,
        help="Optional cap for quick smoke tests while indexing",
    )
    parser.add_argument(
        "--top-k", type=int, default=5, help="Number of evidence rows to retrieve"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    index_path = Path(args.index_path)
    data_dir = Path(args.data_dir)
    rag = VectorlessRAG(index_path=index_path)

    if args.rebuild_index or not index_path.exists():
        print(f"Building lexical index at {index_path} from {data_dir}...")
        build_index(
            data_dir=data_dir,
            index_path=index_path,
            max_rows_per_table=args.max_rows_per_table,
        )

    if not args.question:
        print(
            "Provide a question, for example: python main.py 'What is the age determination rule?'"
        )
        return

    print(rag.answer(args.question, limit=args.top_k))


if __name__ == "__main__":
    main()
