from sklearn import tree

#[height, weight, shoe size]
X = [[181,80,44], [184,74,42], [190,77,43], [175, 72,41]]

Y = ['male', 'female', 'male','female']

#Genders


clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([170,73,41])