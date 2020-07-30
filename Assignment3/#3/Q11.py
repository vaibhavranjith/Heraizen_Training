#Q11
cd={
        "Cricket": {"PKM", "ALN", "GLN", "NVR", "PVR", "KM", "VP", "CS", "MCS"},
        "Football":{ "PKM", "ALN","RMZ","CS", "MCS"},
        "Badminton":{"PKM", "ALN", "NV", "KM","RMV"}
    }
lst=list(cd['Cricket'].intersection(cd['Football']).intersection(cd['Badminton']))
print(f"Players playing all three games: {lst}")
crk=cd["Cricket"]-cd["Football"].union(cd["Badminton"])
ftb=cd['Football']-cd['Cricket'].union(cd["Badminton"])
bad=cd['Badminton']-cd['Cricket'].union(cd['Football'])
print("Players playing cricket football and badminton respectively:")
print(f"{crk}\n{ftb}\n{bad}")



















