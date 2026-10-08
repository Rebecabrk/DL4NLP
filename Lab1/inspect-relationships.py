from nltk.corpus import wordnet as wn

print(wn.synsets('doctor'))
# output: [Synset('doctor.n.01'), Synset('doctor_of_the_church.n.01'), Synset('doctor.n.03'), Synset('doctor.n.04'), Synset('sophisticate.v.03'), Synset('doctor.v.02'), Synset('repair.v.01')]

print(wn.synsets('doctor', pos=wn.NOUN)) # POS = PART OF SPEECH
# output: [Synset('doctor.n.01'), Synset('doctor_of_the_church.n.01'), Synset('doctor.n.03'), Synset('doctor.n.04')]

print(wn.synset('doctor.n.01').definition())
# output: a licensed medical practitioner
print(wn.synset('doctor.n.02').definition())
# output: (Roman Catholic Church) a title conferred on 33 saints who distinguished themselves through the orthodoxy of their theological teaching
print(wn.synset('doctor.n.03').definition())
# output: children take the roles of physician or patient or nurse and pretend they are at the physician's office
print(wn.synset('doctor.n.04').definition())
# output: a person who holds Ph.D. degree (or the equivalent) from an academic institution

print(wn.synsets('physician'))
# outpus: [Synset('doctor.n.01')] => relationship = doctor & physician belong to the same synset => synonyms


common_synsets_kid_child = set(wn.synsets('kid', pos=wn.NOUN)).intersection(wn.synsets('child', pos=wn.NOUN))
print(common_synsets_kid_child)
# # output: {Synset('child.n.01'), Synset('child.n.02')} => relationship = synonym

for syn in common_synsets_kid_child:
    print(syn.definition())
# # output: a young person of either sex
# # a human offspring (son or daughter) of any age
