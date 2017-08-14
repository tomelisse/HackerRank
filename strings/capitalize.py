def capitalize(text):
    text = text.replace(' ','-')
    cap = [s.capitalize() for s in text.split('-')]
    cap = ' '.join(cap)
    cap = cap.replace('-',' ')
    return cap
