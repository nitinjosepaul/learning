def calculate_income_after_tax(state, gross_income):
    """
    Calculate income after deducting federal and state taxes
    """
    federal_tax_percent = 10 #means 10% is the federal tax
    state_tax_percent = { 'Kerala' : 10,
                          'Karnataka' : 8,
                          'Gujarat' : 5,
                          'Tamil Nadu' : 9,
                          'Delhi' : 12
                        }

    if state not in state_tax_percent:
        raise ValueError(f"Cannot calculate data for state {state}")
    federal_tax = gross_income * federal_tax_percent / 100
    state_tax = gross_income * state_tax_percent[state] / 100
    total_tax = federal_tax + state_tax
    income_after_tax = gross_income - total_tax

    print(f"Federal tax is {federal_tax}")
    print(f"State tax for {state} is {state_tax}")
    print(f"Total tax is {total_tax}")
    print(f"Income after tax is {income_after_tax}")
    print("", end="\n\n")

# calculate_income_after_tax('Kerala', 2000000)
# calculate_income_after_tax('Karnataka', 2000000)
# calculate_income_after_tax('Gujarat', 2000000)
# calculate_income_after_tax('Delhi', 2000000)
calculate_income_after_tax('Andhra Pradesh', 2000000)