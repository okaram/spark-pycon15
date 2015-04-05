from person import Person

fi=open("../data/people.txt")
fo=open("../data/people1.json","w")
l=map(lambda l: Person().parse(l.strip('\r\n')).to_json()+'\n',fi)
fo.writelines(l)
