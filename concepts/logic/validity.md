# Validity

**Category:** logic

## Definition
An argument is valid when its conclusion follows necessarily from its premises—that is, if the premises were true, the conclusion must be true.

## Description
Validity is a structural property of arguments that concerns the logical relationship between premises and conclusion, independent of whether the premises are actually true. A valid argument preserves truth: if you start with true premises, you cannot reach a false conclusion.

Validity is about **logical form**, not content. The argument "All cats are mortal; Socrates is a cat; therefore Socrates is mortal" has the same valid form as "All humans are mortal; Socrates is a human; therefore Socrates is mortal"—even though the first has a false premise.

## Formal Definition
An argument is valid if and only if:
- In every possible situation where all the premises are true, the conclusion is also true
- There is no logical possibility of true premises with a false conclusion

## Valid Argument Forms

### Modus Ponens
- Premise 1: If P, then Q
- Premise 2: P  
- Conclusion: Therefore, Q

### Modus Tollens  
- Premise 1: If P, then Q
- Premise 2: Not Q
- Conclusion: Therefore, not P

### Hypothetical Syllogism
- Premise 1: If P, then Q
- Premise 2: If Q, then R
- Conclusion: Therefore, if P, then R

### Disjunctive Syllogism
- Premise 1: P or Q
- Premise 2: Not P
- Conclusion: Therefore, Q

## Testing for Validity
**Method 1: Logical Form**: Check if the argument matches a known valid pattern  
**Method 2: Counterexample**: Try to imagine a scenario where all premises are true but the conclusion is false  
**Method 3: Truth Tables**: For propositional logic, construct truth tables to check all possibilities  
**Method 4: Formal Proof**: Derive the conclusion from premises using logical rules  

## Validity vs Truth
**Crucial Distinction:**
- **Validity**: Concerns logical structure (If premises, then conclusion)
- **Truth**: Concerns correspondence with reality (Are the premises actually true?)

An argument can be:
- Valid with true premises and true conclusion ([Sound](soundness.md))
- Valid with false premises and false conclusion  
- Valid with false premises and true conclusion
- Invalid (never sound, regardless of truth values)

## Common Misconceptions
- **Fallacy**: "The conclusion is false, so the argument is invalid"
  - **Correction**: Invalid arguments can have true conclusions by accident
- **Fallacy**: "The premises are false, so the argument is invalid"  
  - **Correction**: Validity only requires that *if* premises were true, conclusion would follow

## Invalid Argument Forms (Fallacies)

### Affirming the Consequent
- Premise 1: If P, then Q
- Premise 2: Q
- Invalid Conclusion: Therefore, P

### Denying the Antecedent
- Premise 1: If P, then Q  
- Premise 2: Not P
- Invalid Conclusion: Therefore, not Q

## Related Concepts
- [Soundness](soundness.md): Valid arguments with true premises
- [Logic](logic.md): The broader study of reasoning
- [Inference](inference.md) ⚠️ Placeholder: The process of drawing conclusions
- [Deduction](deduction.md): Reasoning that aims for validity
- [Classical Logical Axioms](classical-logical-axioms.md): Principles underlying validity

## Philosophical Significance
Validity captures our intuitive notion that some ways of reasoning are logically compulsory. When an argument is valid, denying the conclusion while accepting the premises involves logical contradiction.

## Key Questions
- What makes logical relationships necessary rather than contingent?
- Are there different concepts of validity for different logical systems?
- How do we know that our rules of validity are correct?

## Sources
- Aristotle, *Prior Analytics*
- Modern logic textbooks
- Hurley, *A Concise Introduction to Logic*, Chapter 1

**Tags:** `#validity` `#logic` `#argument` `#deduction` `#logical-form`  
**Last Updated:** 2025-09-11  
