def analyze_motion(success_rate):
    if success_rate < 0.7:
        return "Motion performance is limited. Suggest adjusting joint range or target position."
    else:
        return "Motion is stable and feasible."
