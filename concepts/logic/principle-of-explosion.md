# Principle of Explosion

**Category:** logic

## Definition
The principle of explosion (Latin: *ex falso quodlibet*) states that from a contradiction, any statement can be validly derived in classical logic.

## Description
If you accept both a statement and its negation as true, then every possible statement becomes provable. This principle shows why [contradiction](contradiction.md) is so dangerous in classical logic—it makes the entire logical system useless by making everything "true."

## Formal Statement
From P and ¬P, any statement Q follows:
- (P ∧ ¬P) → Q

## Proof Sketch
1. Assume: P and ¬P (contradiction)
2. From P, derive: P ∨ Q (for any statement Q)
3. From ¬P and (P ∨ Q), derive: Q
4. Therefore: Q (any arbitrary statement)

## Why This Matters
Explosion explains why classical logic treats contradictions as absolutely forbidden—they destroy the system's ability to distinguish true from false statements.

## Responses
- **[Paraconsistent Logic](paraconsistent-logic.md)**: Rejects explosion, allows some contradictions
- **Relevance Logic**: Restricts explosion to relevant connections
- **Classical Defense**: Maintains explosion as essential to logical rigor

## Related Concepts
- [Contradiction](contradiction.md)
- [Classical Logical Axioms](classical-logical-axioms.md)
- [Paraconsistent Logic](paraconsistent-logic.md)
- [Validity](validity.md)

## Historical Context
Known since ancient times but formalized in modern logic. Drives much of the development of non-classical logical systems.

## Key Questions
- Should logic allow any contradictions to be true?
- Is explosion a bug or a feature of classical logic?

## Sources
- Priest, Graham. *In Contradiction*
- Routley, Richard. *Relevant Logics and Their Rivals*

**Tags:** `#explosion` `#contradiction` `#classical-logic` `#paraconsistent`  
**Last Updated:** 2025-09-15  
