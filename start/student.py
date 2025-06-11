students = [
               {'num':'1','name':'김철수','kor':90,'eng':80,'math':85,'total':0,'avg':0.0,'order':0 },
               {'num':'2','name':'박제동','kor':90,'eng':85,'math':90,'total':0,'avg':0.0,'order':0 },
               {'num':'3','name':'홍길동','kor':80,'eng':80,'math':80,'total':0,'avg':0.0,'order':0 }
           ]

#students order
for student in students :  #students[0] 자료를 꺼낸 것이 student
    rank = 1
    for other in students :
        if other['total'] > student['total'] :
            rank += 1
    student['order'] = rank
print(student['name'], student['order'])
