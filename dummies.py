
gender_dummies={
    'Male':1,
    'Female':0
}

smoking_history_dummies={
    'current':[1,0,0,0,0,0],
    'ever':[0,1,0,0,0,0],
    'former':[0,0,1,0,0,0],
    'never':[0,0,0,1,0,0],
    'not current':[0,0,0,0,1,0],
    'NO info':[0,0,0,0,0,0]

}

initial_diagnosis_dummies ={
    'normal':[1,0,0],
    'diabetes':[0,1,0],
    'prediabetes':[0,0,0]
}


weight_type_dummies={
    'obesity':[1,0,0,0],
    'overweight':[0,1,0,0],
    'underweight':[0,0,1,0],
    'normal':[0,0,0,0]
    }
 
sugar_test_dummies={
    'normal':[1,0,0],
    'prediabetes':[0,1,0],
    'diabetes':[0,0,0]
 }
