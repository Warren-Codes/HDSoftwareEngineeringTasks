def moon_weight(weight, extra_weight, years):
    for year in range(1, years):
        weight = weight + extra_weight
        weight_on_moon = weight * 0.165

        print(f"After {year} years your moon weight will be {weight_on_moon:.2f} lb.")


moon_weight(180, 2, 16)
