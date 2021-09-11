from switch import Switch


def simple_example_with_default(val):
    values = []

    with Switch(val) as case:
        if case(1):
            values.append('Found 1')

        if case(2, 3):
            values.append('Found 2 or 3')

        if case.default:
            values.append('No love for 1, 2 or 3?')

    return values


assert simple_example_with_default(1) == ['Found 1']
assert simple_example_with_default(2) == ['Found 2 or 3']
assert simple_example_with_default(3) == ['Found 2 or 3']
assert simple_example_with_default('anything else') == ['No love for 1, 2 or 3?']