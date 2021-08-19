import gensim as gn
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from .forms import ExamForm1
import pandas as pd

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def test(request):
    if request.method=='POST':
        form = ExamForm1(request.POST)
        if form.is_valid():
            arr=[]
            field=[]
            field.append(form.data['agriculture'])
            field.append(form.data['photography'])
            field.append(form.data['hotel_management'])
            field.append(form.data['gaming'])
            field.append(form.data['commerce'])
            field.append(form.data['business_management'])
            field.append(form.data['biology'])
            field.append(form.data['animation'])
            field.append(form.data['computer_engineering'])
            field.append(form.data['journalism'])
            courses={}
            courses[0]="agriculture"
            courses[1]="photography"
            courses[2]="hotel_management"
            courses[3]="gaming"
            courses[4]="commerce"
            courses[5]="business_management"
            courses[6]="biology"
            courses[7]="animation"
            courses[8]="computer_engineering"
            courses[9]="journalism"


            degrees={0:{"Diploma in Agriculture","Diploma in Agriculture Engineering","Diploma in Organic Agriculture"}}
            degrees[1]={"Diploma in Photography"}
            degrees[2]={"Diploma in Hotel Management","Diploma in Food & Beverage Production","Diploma in Front Office Operations"}
            degrees[3]={"Diploma in Game designing","Diploma in Graphic designing"}
            degrees[4]={"Commerce(CEC)","Commerce(MEC)","eCommerce","Diploma in Accounting "}
            degrees[5]={"Diploma in Business Adminstration"}
            degrees[6]={"Biology(BPC)","Diploma in Pharmacy","Diploma in Dental Mechanics"}
            degrees[7]={"Diploma in Animation","Diploma in 3D animation","Diploma in animation,art and design"}
            degrees[8]={"Science(MPC)","Diploma in Computer Programming","Diploma in Information Technology"}
            degrees[9]={"Diploma in Journalism and Mass Communication","Diploma in Development Journalism","Diploma in Mass Media Communication"}
            # lis=open("C:/Users/Magesh/Desktop/career_counselling/blog/static/inference/agriculture.txt", encoding="UTF-8",errors="ignore").replace(",","").split()
            headers=["College Name","Location"]
            with open("C:/Users/Magesh/Desktop/career_counselling/blog/static/inference/agriculture.txt", "r", encoding="UTF-8") as f:
                stri=f.read()
            lis=stri.replace(",","").split('\n')
            li=[i.split() for i in lis]
            maxScore=0
            course=0
            for i in range(10):
                p=summarize(field[i], ratio=0.9)
                lis2=set(list(set(p.split())))
                result=len(set(li[i]).intersection(lis2))
                if( maxScore < result):
                    maxScore=result
                    course=i
            src="/media/output/"+"img"+str(course)+".jpg"
            colleges={5:[["INDIAN INSTITUTE OF MANAGEMENT - [IIMB]","Banglore"],["INDIAN INSTITUTE OF MANAGEMENT - [IIMA]","Gujarat"],["INDIAN INSTITUTE OF MANAGEMENT - [IIMC]","West Bengal"],["INDIAN INSTITUTE OF MANAGEMENT - [IIM]","Uttar Pradesh"],["VGSoM Indian Institute of Technology Kharagpur","West Bengal"]]}
            colleges[0]=[["Oberoi Centre for Learning & Development","Hyderabad"],["ICAR-National Dairy Research Institute (NDRI)","Haryana"],["ICAR-Indian Agricultural Research Institute","New Delhi"],["GB Pant University of Agriculture & Technology","Uttarkhand"],["Chaudhary Charan Singh, Haryana Agriculture University","Haryana"]]
            colleges[1]=[["Sir J.J. Institute of Applied Arts","Mumbai"],["Pixel Institute of Photography","New Delhi"],["The One Goa School","Goa"],["Asian Academy of Film and Television","Noida"],["Light and Life Academy","Ooty"]]
            colleges[2]=[["Oberoi Centre for Learning & Development","New Delhi"],["Institute of Hotel Management, Catering Technology & Applied Nutrition (IHM)","Mumbai"],["Institute of Hotel Management, Catering & Nutrition","New Delhi"],["Institute of Hotel Management","Aurangabad"],["Institute of Hotel Management","Banglore"]]
            colleges[3]=[["Academy of Animation and Gaming (AAG)","Uttar Pradesh"],["Animaster Academy","Banglore"],["Areana Animation","Mumbai"],["Asian Institute of Gaming & Animation","Banglore"],["Global School of Animation & Games","New Delhi"]]
            colleges[4]=[["SHRI RAM COLLEGE OF COMMERCE - [SRCC]","New Delhi"],["Lady Shriram College for Women (LSR)","New Delhi"],["Hansraj College","New Delhi"],["Hindu College","New Delhi"],["Loyola College","Chennai"]]
            colleges[6]=[["Hindu College","New Delhi"],["Miranda House","New Delhi"],["MCC - Madras Christian College","Chennai"],["Hansraj College","New Delhi"],["Loyola College","Chennai"]]
            colleges[7]=[["National Institute of Film and Fine Arts","Kolkata"],["St. Xavier’s College (Autonomous)","Kolkata"],["Maya Institute of Advanced Cinematic","Mumbai"],["Arena Animation","New Delhi"],["FX School","Mumbai"]]
            colleges[8]=[["IIT-Delhi","New Delhi"],["IIT-Kharagpur","Kharagpur"],["IIT-Bombay","Mumbai"],["IIT-Chennai","Chennai"],["IIT-Kanpur","Kanpur"]]
            colleges[9]=[["INDIAN INSTITUTE OF MASS COMMUNICATION - [IIMC]","New Delhi"],["ASIAN COLLEGE OF JOURNALISM - [ACJ]","Chennai"],["AJK MASS COMMUNICATION RESEARCH CENTRE","New Delhi"],["SAVITRIBAI PHULE PUNE UNIVERSITY - [SPPU]","Pune"],["CHANDIGARH UNIVERSITY - [CU]","CHANDIGARH"]]
            return render(request,'blog/output.html',{'arr':courses[course],'src':src,'degrees':degrees[course],'headers':headers,'colleges':colleges[course]})
    else:
        form = ExamForm1()
    return render(request,'blog/test.html',{'form':form})
