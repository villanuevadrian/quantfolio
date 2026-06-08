# ADR-001: Holdings calculated at runtime

## Status
Accepted

## Context
Need to track current positions per asset.

## Decision
Calculate holdings from transactions at read time rather than storing them in the db.

## Consequences
+ No risk of holding/transaction desync
+ Transactions remain single source of truth
− Read performance cost: recalculates from full transaction history on every read, including assets no longer held
− Mitigation path: materialized view if needed later