def parse_fopc(expression):
    expression = expression.replace(" ", "")
    if "->" in expression:
        antecedent, consequent = expression.split("->")
        return f"Implication: If {antecedent}, then {consequent}"
    elif "∧" in expression:
        conjuncts = expression.split("∧")
        return f"Conjunction: {conjuncts}"
    elif "∨" in expression:
        disjuncts = expression.split("∨")
        return f"Disjunction: {disjuncts}"
    else:
        return f"Atomic Proposition: {expression}"

print(parse_fopc("P ∧ Q"))
def parse_fopc(expression):
    expression = expression.replace(" ", "")
    if "->" in expression:
        antecedent, consequent = expression.split("->")
        return f"Implication: If {antecedent}, then {consequent}"
    elif "∧" in expression:
        conjuncts = expression.split("∧")
        return f"Conjunction: {conjuncts}"
    elif "∨" in expression:
        disjuncts = expression.split("∨")
        return f"Disjunction: {disjuncts}"
    else:
        return f"Atomic Proposition: {expression}"

print(parse_fopc("P ∧ Q"))
