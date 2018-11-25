from firebase import firebase
firebase=firebase.FirebaseApplication('https://musictube-75f00.firebaseio.com/')
result=firebase.post('/English',{'t':'D112i1ZMEzI','d':'Anitta - Não Perco Meu Tempo (Official Music Video)','s':1543175864})
print(result)
