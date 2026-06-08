## 2026-06-04 — Session 5
**What I built:** all three repositories
**What I learned:** SQLAlchemy 2.0 modern query style (select() vs legacy query()), diference between repo and service
**What confused me:** 
**Next session goal:** Services layer

## 2026-06-08 — Session 7
**What I built:**
- Finished the service layer: stock (get_or_create), portfolio
  (create + asset_type validation), transaction (create with portfolio/stock checks)
- Restructured docs into docs/ folder, wrote the README, created TODO.md
- Made the repo public

**What I learned:**
- Difference between repository (DB access only) and service (business logic)
- Why holdings should be calculated from transactions, not stored (source of truth)
- Feature-driven development vs TDD — they're different approaches

**What confused me:**
- Pre-commit blocking commits because a half-written file was staged
- The whole exception-handling-to-HTTP question (deferred to router stage)

**Next session goal:**
- Portfolios vertical slice: read service → router → wired into main.py → testable in /docs