# Change log

## 2026-10-21 — Local publication preparation

- Created a new project from the two supplied instructor packages; originals remain untouched.
- Inspected all four notebooks, five accompanying data files, source readmes/email, seven DOCX handouts, and their seven PDF counterparts. A private source inventory with SHA-256 hashes is retained outside this repository.
- Organized the real lessons into `python-basics` and `working-with-apis`, each with separate `student.ipynb` and `instructor.ipynb` files.
- Restored Python student fill-ins from the original TODO prompts. Removed saved responses, debug remnants, and the inconsistent first-index, HR-sort, and top-10 OPS answers; instructor solutions retain the correct operations.
- Removed completed instructor TODO comments. Retained original lesson sequence, examples, supplied helper function, mini challenges, and teaching voice.
- Cleared all notebook outputs, execution counts, and machine-specific metadata; added stable cell IDs. Replaced adjacent-file assumptions with relative `data/` paths that support the project root and workshop folder.
- Defaulted API notebooks to offline mode; guarded the optional 404 request. Added a small in-session cache for successful Pokémon responses. Clarified fixed offline-resource limits and illustrative weather chart labels.
- Withheld the original MLB CSV because redistribution rights are unconfirmed; qualified unverified season/source claims. Preserved the CSV schema and explicit local-data instructions without inventing replacement records.
- Retained all four original API fallback assets byte-for-byte. Added provenance, provider attribution, and third-party license notices.
- Converted the useful cheat sheets, instructor keys, and teaching itineraries to Markdown, updating notebook references and data paths. Replaced the old environment check with one shared setup guide. Omitted duplicate PDF/DOCX exports and the dated meeting announcement/email, including its signature and room schedule.
- Added exact direct dependency versions, Windows/VS Code/Jupyter instructions, ignore rules, and an offline notebook verification script. Optional Excel-export handout patterns are identified as requiring a separate optional dependency.
- Recorded verification scope, privacy scan results, and unresolved publication decisions in `docs/VERIFICATION.md`. No GitHub repository, remote, commit, or push was created.

## 2026-10-21 — Private repository preparation

- Owner authorized pushing the DAC workshops to a new private GitHub repository.
- Retained the MLB exclusion and all documented licensing limitations.
- Rechecked the publication privacy scan and original-file hashes before staging.
